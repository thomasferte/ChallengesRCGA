from train_test_api.utils import *
from genetic_algorithm.parallelise_to_csv import *
from genetic_algorithm.monthly_update_from_csv import *
from genetic_algorithm.get_GA_parameters_from_scenari import *
import os

##### define objective function #####
slurm_job = os.getenv('SLURM_ARRAY_JOB_ID')
# slurm_job = "2536874"
slurm_scenari = os.getenv('SLURM_JOB_NAME')
# slurm_scenari = "GeneticSingleIs_GA_GAHPDEF_pmutQuant100_pmutCat10_sigmahalv5"
array_id = os.getenv('SLURM_ARRAY_TASK_ID')
# array_id = 1

### Define folders
folder_path = "/beegfs/tferte/output/" + slurm_scenari + "/"
# folder_path = "output/" + slurm_scenari + "/"
first_perf_file = slurm_scenari + "_" + str(slurm_job) + ".csv"
output_path = folder_path + "csv_parallel/"

### Define GA parameters
dict_GA_parameters = get_GA_parameters_from_scenari(slurm_scenari = slurm_scenari)
slurm_scenari = dict_GA_parameters["scenari"]
pmutQuant = dict_GA_parameters["pmutQuant"]
pmutCat = dict_GA_parameters["pmutCat"]
sigmahalv = dict_GA_parameters["sigmahalv"]

print(glue::glue("------- GA HP : pmutQuant = {pmutQuant}, pmutCat = {pmutCat}, sigmahalv = {sigmahalv} ------------"))

### Define population size if needed
if slurm_scenari in ["GeneticSingleIs_GA_1000"]:
    units = 2000
else :
    units = 500

if slurm_scenari in ["GeneticSingleIs_GA_10esn_fourth", "GeneticSingleIs_RS_10esn_fourth"]:
    Npop = 100
    Ne = 50
    nb_trials_first = 800
    nb_trials_update = 300
else :
    Npop = 200
    Ne = 100
    nb_trials_first = 3200
    nb_trials_update = 1200

## days forecast
if slurm_scenari in ["GeneticSingleIs_GA_21", "xgb_pred_RS_21"]:
    data_path="data_obfuscated_forecast_21days/"
elif slurm_scenari in ["GeneticSingleIs_GA_7", "xgb_pred_RS_7"]:
    data_path="data_obfuscated_forecast_7days/"
else :
    data_path="../high_dimension_reservoir/data_obfuscated/"

data_path="../high_dimension_reservoir/data_obfuscated_short/"

## frequency update
if slurm_scenari in ["GeneticSingleIs_GA_20esn_week"]:
    update = "week"
else :
    update = "month"

# Npop = 2
# Ne = 1
# nb_trials_first = 3
# nb_trials_update = 3

print("------- first optimisation ------------")
csv_sampler(
  units = units,
  path_file= folder_path + first_perf_file,
  data_path=data_path,
  output_path= output_path+"first_optimisation/",
  scenari = slurm_scenari,
  array_id = str(array_id),
  Npop=Npop,
  Ne=Ne,
  nb_trials=nb_trials_first,
  pmutQuant = pmutQuant,
  pmutCat = pmutCat,
  sigmahalv = sigmahalv
  )

if slurm_scenari not in ["GeneticSingleIs_GA_1000", "GeneticSingleIs_GA_21", "xgb_pred_RS_21", "GeneticSingleIs_GA_7", "xgb_pred_RS_7", "GeneticSingleIs_GA_noGironde", "GeneticSingleIs_GA_noWeather", "GeneticSingleIs_GA_noUrgSamu", "GeneticSingleIs_GA_noDeriv"]:
    print("------- monthly update ------------")
    evolutive_hp_csv(
      update = update,
      units = units,
      array_id = str(array_id),
      perf_folder = folder_path,
      first_perf_file = first_perf_file,
      data_path = data_path,
      scenari=slurm_scenari,
      Npop = Npop,
      Ne = Ne,
      nb_trials = nb_trials_update,
      pmutQuant = pmutQuant,
      pmutCat = pmutCat,
      sigmahalv = sigmahalv
      )
