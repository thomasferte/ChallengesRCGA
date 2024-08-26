import pandas as pd
from flock import Flock
from genetic_algorithm.parallelise_to_csv import *

def reevaluate_previous_trials(previous_perf_path, perf_folder, date, data_path, Npop, scenari, array_id, units = 500):
    print("get features")
    forecast_days, features, global_optimizer, nb_esn = features_nbesn_optimizer_from_scenari(scenari)
    
    ##### select best trials from previous results
    print("get file perf = " + previous_perf_path)
    with open(previous_perf_path, 'r') as file:
           fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
           df_previous_perf = pd.read_csv(previous_perf_path, on_bad_lines = "skip").dropna()
           fcntl.flock(file, fcntl.LOCK_UN)
    top_trials = df_previous_perf.sort_values('value', ascending=False).tail(Npop)
    top_trials["value"] = "todo"
    
    # if file didn't exist, read it to check and write with header if needed
    new_perf_file = perf_folder+date+".csv"
    # if file does not exist yet, create it with previous values to "todo"
    if(not os.path.exists(new_perf_file)):
            with open(new_perf_file, 'a+') as file:
                    fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
                    # Check the number of lines
                    file_size = file.tell()  # Move to the beginning of the file
                    if file_size == 0:
                        top_trials.to_csv(new_perf_file, index=False, mode = "a", header = True)
                    else :
                        top_trials.to_csv(new_perf_file, index=False, mode = "a", header = False)
                    fcntl.flock(file, fcntl.LOCK_UN)
            
#         with Flock(new_perf_file_lock, 'w'):
#             top_trials.to_csv(new_perf_file, index=False, mode = "w", header = True)
#         with open(new_perf_file, 'a+') as file:
#             fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
#             file_size = file.tell()  # Move to the beginning of the file
#             if file_size == 0:
#                 top_trials.to_csv(new_perf_file, index=False, mode = "w", header = True)
#             fcntl.flock(file, fcntl.LOCK_UN)
    
    # open file, set value to in progress, close file, evaluate job, update file
    nb_trials_to_reevaluate = 1
    while nb_trials_to_reevaluate>0:
        params = {}
        # try to write on file several times
        file_ok = 1
        while file_ok != 0 and file_ok < 100 :
            try:
                with open(new_perf_file, 'r') as file:
                    fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
                    df_perf = pd.read_csv(new_perf_file)
                    fcntl.flock(file, fcntl.LOCK_UN)
                
                dftodo = df_perf[df_perf["value"] == "todo"]
                nb_trials_to_reevaluate = len(dftodo)
                print("nb_trials_to_reevaluate = " + str(nb_trials_to_reevaluate))
                if(nb_trials_to_reevaluate > 0):
                    random_row = dftodo.sample(n=1, random_state=random.seed())
                    job_id_to_do = random_row.iloc[0]["job_id"]
                file_ok = 0
                #with open(new_perf_file, 'a+') as file:
                #    fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
                #    df_perf = pd.read_csv(new_perf_file)
                #    dftodo = df_perf[df_perf["value"] == "todo"]
                #    nb_trials_to_reevaluate = len(dftodo)
                #    print("nb_trials_to_reevaluate = " + str(nb_trials_to_reevaluate))
                #    # set in progress value and save file
                #    if(nb_trials_to_reevaluate > 0):
                #        random_row = dftodo.sample(n=1, random_state=random.seed())
                #        job_id_to_do = random_row.iloc[0]["job_id"]
                #        # job_id_to_do = df_perf[df_perf["value"] == "todo"].iloc[0]["job_id"]
                #        # set to in progress to inform other nodes
                #        # df_perf.loc[df_perf["job_id"] == job_id_to_do, "value"] = "inprogress"
                #        # df_perf.to_csv(new_perf_file, index = False, mode = "w", header = True)
                #    # close file
                #    fcntl.flock(file, fcntl.LOCK_UN)
                #    file_ok = 0
            except:
                print(str(file_ok) + " failed attempt to access main file, retry")
                file_ok += 1
                time.sleep(5)
            
        # compiute the objective value for the job_id_todo
        if nb_trials_to_reevaluate > 0:
            value = 1000
            nb_try = 0
            while value > 999 and nb_try < 500:
              print("trial = " + str(nb_try))
              try:
                  params = df_perf[df_perf["job_id"] == job_id_to_do].to_dict(orient = "records")[0]
                  temp = params.pop("value")
                  temp = params.pop("job_id")
                  current_time = datetime.now().strftime("%d_%m_%H_%M_%S")
                  value = eval_objective_function(
                    forecast_days = forecast_days,
                    units = units,
                    min_date_eval = date,
                    params = params,
                    features = features,
                    data_path = data_path,
                    job_id = job_id_to_do+"_at_" + date + "_by_" + array_id,
                    output_path=perf_folder+"csv_parallel/"+date+"/"
                  )
                  if value < 999:
                      with open(new_perf_file, 'a+') as file:
                          fcntl.flock(file, fcntl.LOCK_EX)  # Acquire an exclusive lock
                          df_perf = pd.read_csv(new_perf_file)
                          df_perf.dropna(inplace=True)
                          df_perf.loc[df_perf["job_id"] == job_id_to_do, "value"] = value
                          df_perf.loc[df_perf["job_id"] == job_id_to_do, "optimizer"] = "reevaluate"
                          df_perf.to_csv(new_perf_file, index = False, mode = "w", header = True)
                          fcntl.flock(file, fcntl.LOCK_UN)
              
              except pd.errors.EmptyDataError:
                  print("Failed to reevaluate objective function, retry")
                  value = 1000
                  nb_try += 1
                  time.sleep(2)
    
    return new_perf_file

def evolutive_hp_csv(array_id, perf_folder, first_perf_file, data_path, scenari, Npop = 200, Ne = 100, nb_trials = 1200, min_date_eval = datetime.strptime('2021-03-01', '%Y-%m-%d'), units = 500, update = "month", pmutQuant = .5, pmutCat = .25, sigma = 1, sigma_halv_thresh = 6, sigmahalv = 10, NbFeaturesPenalty = 0, TournamentFeaturesPenalty = False, Ntournament = 2):
    ##### get all dates files
    files = pd.DataFrame(glob.glob(data_path + '*.csv'),columns = ['full_path'])
    files['file_name'] = files.full_path.str.split(data_path,n=1).str[-1]
    files['date'] = pd.to_datetime(files.file_name.str.split('.csv').str[0],format='%Y%m%d')
    files = files[files['date'] > min_date_eval]
    files['day'] = files['date'].dt.day
    files = files.sort_values("date")
    files = files.reset_index(drop=True)
    
    ##### iterate through date and reestimate hp if date day is 1 or 2
    previous_perf_path = perf_folder + first_perf_file
    for ind in files.index:
        day = files['day'][ind]
        date = files['date'][ind]
        
        if(update == "month"):
            bool_update = day in [1,2]
        elif(update == "week"):
            bool_update = date.weekday() in [0,1]
        else:
            raise ValueError("update argument must be week or month")
        
        date = date.strftime("%Y-%m-%d")
        
        if(bool_update):
            print("------------------" + date + "---------------------")
            ### import previous results and reevaluate them
            trial_ok = 1
            while trial_ok != 0 and trial_ok < 1000 :
                try:
                    previous_perf_path = reevaluate_previous_trials(
                        units = units,
                        previous_perf_path=previous_perf_path,
                        perf_folder=perf_folder,
                        date=date,
                        data_path=data_path,
                        Npop=Npop,
                        array_id = array_id,
                        scenari=scenari
                        )
                    trial_ok = 0
                except pd.errors.EmptyDataError:
                    print(str(trial_ok) + " attempt, retry")
                    trial_ok += 1
                    time.sleep(1)
            ### GA for x interation with new min_date, isTraining = True and save results
            trial_sampler_ok = 1
            while trial_sampler_ok != 0 and trial_sampler_ok < 1000 :
                try:
                    csv_sampler(
                        units = units,
                        path_file=previous_perf_path,
                        date=date,
                        data_path=data_path,
                        output_path=perf_folder+"csv_parallel/"+date+"/",
                        scenari = scenari,
                        array_id = array_id,
                        Npop=Npop,
                        Ne=Ne,
                        nb_trials=nb_trials,
                        pmutQuant = pmutQuant,
                        pmutCat = pmutCat,
                        sigma = sigma,
                        sigmahalv = sigmahalv,
                        NbFeaturesPenalty = NbFeaturesPenalty,
                        TournamentFeaturesPenalty = TournamentFeaturesPenalty,
                        Ntournament = Ntournament
                        )
                    trial_sampler_ok = 0
                except pd.errors.EmptyDataError:
                    print(str(trial_ok) + " attempt csv_sampler, retry")
                    trial_sampler_ok += 1
                    time.sleep(1)
            
            
    return None

# perf_folder = "output/"
# first_perf_file = "GeneticMultipleIsBin_11044201.csv"
# Npop = 2
# Ne = 1
# nb_trials = 3
# data_path = "data/"
# min_date_eval = datetime.strptime('2021-03-01', '%Y-%m-%d')
# scenari = "GeneticMultipleIsBin"
# array_id = 1
# evolutive_hp_csv(
#   array_id = array_id,
#   perf_folder = perf_folder,
#   first_perf_file = first_perf_file,
#   data_path = data_path,
#   scenari=scenari,
#   Npop = Npop,
#   Ne = Ne,
#   nb_trials = nb_trials,
#   min_date_eval = min_date_eval
# )
