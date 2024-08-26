import numpy as np
import random

class CsvGeneticAlgorithm(object):
    def __init__(self, hp_df, perf_df, Npop = 200, Ne = 100, Ntournament = 2, pmutQuant = .5, pmutCat = .25, sigma = 1, sigma_halv_thresh = 6, sigmahalv = 1/10, NbFeaturesPenalty = 0, TournamentFeaturesPenalty = False):
        self._rng = np.random.RandomState()
        self._current_trial = None  # Current state.
        # add genetic algorithm hyperparam
        # # genetic algo hp
        self.hp_df = hp_df
        self.perf_df = perf_df
        self.Npop = Npop
        self.Ntournament = Ntournament
        self.Ne = Ne
        # self.NbGen = NbGen
        self.pmutQuant = pmutQuant
        self.pmutCat = pmutCat
        self.sigma = sigma
        self.sigma_halv_thresh = sigma_halv_thresh
        self.sigmahalv = sigmahalv
        self.NbFeaturesPenalty = NbFeaturesPenalty
        self.TournamentFeaturesPenalty = TournamentFeaturesPenalty

    # Keep top Npop best finished trials
    def keepBestNPopTrials(self):
      # All completed trials
      listOfCompletedTrials = self.perf_df
      listOfCompletedTrials['value'] = listOfCompletedTrials['value'].astype(float)
      # Number of child already computed in the current generation
      NbChildAlreadyCompleted = ((len(listOfCompletedTrials)-self.Npop) % self.Ne)
      # Sample only from population, remove children
      if(NbChildAlreadyCompleted != 0):
          listOfCompletedTrials = listOfCompletedTrials[:-NbChildAlreadyCompleted]
      # Compute the new value column
      listOfCompletedTrials['penalized_value'] = listOfCompletedTrials['value'] + self.NbFeaturesPenalty*listOfCompletedTrials['nbFeaturesSelected']
      # Get best individuals from population
      top_Npop = listOfCompletedTrials.sort_values(by = "penalized_value", ascending = True).head(self.Npop)
      return top_Npop
      
    ## 1 parent selection by tournament
    # ntournament : number of candidate for the tournament
    def tournamentSelection(self):
      # Select challengers from completed trials
      listOfCompletedTrials = self.keepBestNPopTrials()

      random_rows = listOfCompletedTrials.sample(n=self.Ntournament)
      
      if self.TournamentFeaturesPenalty :
          # remove worse performing
          row_to_remove_worse = random_rows['nbFeaturesSelected'].idxmax()
          random_rows = random_rows.drop(row_to_remove_worse)
      
      row_to_keep = random_rows['penalized_value'].idxmin()
      
      return random_rows.loc[row_to_keep]

    ## 2 parents selection by tournament
    def selection(self):

      pere = self.tournamentSelection()
      mere = self.tournamentSelection()
      return pere, mere

    def crossoverMutation(self, pere, mere):
      list_params = pere.index.to_list()
      # remove unneeded paramters
      list_params.remove("job_id")
      list_params.remove("value")
      
      params = {}
      for param_name in list_params:
          
          param_pere = pere[param_name]
          param_mere = mere[param_name]
          
          hp_dict = self.hp_df[self.hp_df['hp'] == param_name].to_dict(orient='records')[0]
          
          if(hp_dict["type_hp"] == 'int'):
              param_pere = int(param_pere)
              param_mere = int(param_mere)
              low = int(hp_dict["low"])
              high = int(hp_dict["high"])
          
          if(hp_dict["type_hp"] == 'num'):
              param_pere = float(param_pere)
              param_mere = float(param_mere)
              low = float(hp_dict["low"])
              high = float(hp_dict["high"])
          
          param_width = self.sigma_halv_thresh + 1
          # log transform if needed
          if(hp_dict["log"]):
              param_pere = np.log10(param_pere)
              param_mere = np.log10(param_mere)
              param_width = np.log10(high) - np.log10(low)
                    
          # Mother/Father equilibrium
          alp = np.random.rand(1)[0]
          # Mutation
          
          # modifiy sigma if param distribution width is small
          sigma_update = self.sigma
          if(param_width <= self.sigma_halv_thresh):
              sigma_update = self.sigma*self.sigmahalv
          
          boolMutationQuant = np.random.rand(1)[0] < self.pmutQuant
          boolMutationCat = np.random.rand(1)[0] < self.pmutCat
          
          if(hp_dict["type_hp"] == 'binary'):
              # how to update categorical parameter : either the one from father or mother
              if(alp > 0.5):
                  param_child = param_pere
              else :
                  param_child = param_mere
              if(boolMutationCat):
                  param_child = np.random.choice([hp_dict["low"], hp_dict["high"]])
              
          if(hp_dict["type_hp"] == 'int'):
              # how to update integer parameter
              # Barycentric type crossover
              # mutation plus or minus 1
              
              # handle exception seed
              if(param_name == "seed"):
                  if(alp > 0.5):
                      param_child = param_pere
                  else :
                      param_child = param_mere
                  if(boolMutationQuant):
                      param_child = random.randint(low, high)
              else :
                  param_child = np.round(alp * param_pere + (1-alp) * param_mere)
                  if(boolMutationQuant):
                      added = np.round(np.random.rand(1)[0])*2-1
                      param_child = param_child + added
              # ensure integer type
              param_child = int(param_child)
          
          if(hp_dict["type_hp"] == 'num'):
              # how to update float parameter
              # Barycentric type crossover
              # mutation gaussian
              param_child = alp * param_pere + (1-alp) * param_mere
              if(boolMutationQuant):
                  param_child = param_child + sigma_update * np.random.randn(1)[0]
          
          # log transform back if needed
          if(hp_dict["log"]):
              param_child = 10**param_child
          
          if hp_dict["type_hp"] in ["num", "int"]:
              if param_child > high:
                  param_child = high
              if param_child < low:
                  param_child = low
          
          if isinstance(param_child, list):
              params[param_name] = param_child[0]
          else :
              params[param_name] = param_child
        
      return params

    def sample_relative(self):
        # Simulated Annealing algorithm.
        # 1. Select parents by tournament
        pere, mere = self.selection()

        # 2. Crossover
        params = self.crossoverMutation(pere = pere, mere = mere)
        
        # 4. Return new children parameters
        return params
