generate_slurm_files <- function(folder, pmutQuant, pmutCat, sigmahalv, delayed){
  slurm_scenari <- glue::glue("GeneticSingleIs_GA_GAHPDEF_pmutQuant{pmutQuant*1000}_pmutCat{pmutCat*1000}_sigmahalv{sigmahalv*1000}")
  res <- glue::glue(
    '#!/bin/bash
  
  #############################
  # les directives Slurm vont ici:
  
  # Your job name (displayed by the queue)
  #SBATCH -J {slurm_scenari}
  
  # walltime (hh:mm::ss)
  #SBATCH -t 06:30:00
  #SBATCH --begin=now+{delayed}hours
  
  
  # change working directory
  # SBATCH --chdir=.
  
  ### In filenames, %j=jobid, %a=index in job array
  #SBATCH -o /beegfs/tferte/std_out/%j_%a_%x.out # standard out goes to this file
  #SBATCH -e /beegfs/tferte/std_err/%j_%a_%x.err # standard err goes to this file
  
  #SBATCH --array 0-199
  #SBATCH --ntasks 1
  #SBATCH --cpus-per-task 5
  #SBATCH --mem-per-cpu=2560
  
  # fin des directives PBS
  #############################
  
  # useful informations to print
  echo "#############################"
  echo "User:" $USER
  echo "Date:" `date`
  echo "Host:" `hostname`
  echo "Directory:" `pwd`
  echo "SLURM_JOBID:" $SLURM_JOB_ID
  echo "SLURM_ARRAY_JOB_ID:" $SLURM_ARRAY_JOB_ID
  echo "SLURM_SUBMIT_DIR:" $SLURM_SUBMIT_DIR
  echo "SLURM_JOB_NODELIST:" $SLURM_JOB_NODELIST
  echo "SLURM_JOB_NAME" : $SLURM_JOB_NAME
  echo "#############################"
  
  #############################
  export OPENBLAS_NUM_THREADS=1
  export OMP_NUM_THREADS=1
  export MKL_NUM_THREADS=1
  
  # cd /gpfs/home/tferte910e/high_dimension_reservoir
  # source /gpfs/home/tferte910e/predictcovid_api_python/testenv/bin/activate
  
  module load build/conda/4.10
  conda activate testenv
  cd /home/tferte/ChallengesRCGA
  
  ulimit -c 0
  
  python main_csv_evaluate.py
  '
  )
  
  write(x = res, file = glue::glue("{folder}/{slurm_scenari}.slurm"))
  
  return(NULL)
}

generate_slurm_files_test <- function(folder, pmutQuant, pmutCat, sigmahalv, delayed){
  slurm_scenari <- glue::glue("GeneticSingleIs_GA_GAHPDEF_pmutQuant{pmutQuant*1000}_pmutCat{pmutCat*1000}_sigmahalv{sigmahalv*1000}")
  
  res <- glue::glue(
    '#!/bin/bash
    
    #############################
    # les directives Slurm vont ici:
    
    # Your job name (displayed by the queue)
    #SBATCH -J {slurm_scenari}
    
    # walltime (hh:mm::ss)
    #SBATCH -t 15:00:00
    
    
    # change working directory
    # SBATCH --chdir=.
    
    ### In filenames, %j=jobid, %a=index in job array
    #SBATCH -o /beegfs/tferte/std_out/%j_%a_%x.out # standard out goes to this file
    #SBATCH -e /beegfs/tferte/std_err/%j_%a_%x.err # standard err goes to this file
    
    #SBATCH --array 0-10
    #SBATCH --ntasks 1
    #SBATCH --cpus-per-task 10
    #SBATCH --mem-per-cpu=2560
    
    # fin des directives PBS
    #############################
    
    # useful informations to print
    echo "#############################"
    echo "User:" $USER
    echo "Date:" `date`
    echo "Host:" `hostname`
    echo "Directory:" `pwd`
    echo "SLURM_JOBID:" $SLURM_JOB_ID
    echo "SLURM_ARRAY_JOB_ID:" $SLURM_ARRAY_JOB_ID
    echo "SLURM_SUBMIT_DIR:" $SLURM_SUBMIT_DIR
    echo "SLURM_JOB_NODELIST:" $SLURM_JOB_NODELIST
    echo "SLURM_JOB_NAME" : $SLURM_JOB_NAME
    echo "#############################"
    
    #############################
    export OPENBLAS_NUM_THREADS=1
    export OMP_NUM_THREADS=1
    export MKL_NUM_THREADS=1
    
    # cd /gpfs/home/tferte910e/high_dimension_reservoir
    # source /gpfs/home/tferte910e/predictcovid_api_python/testenv/bin/activate
    
    module load build/conda/4.10
    conda activate testenv
    cd /home/tferte/ChallengesRCGA
    
    ulimit -c 0
    
    python main_csv_test.py'
  )
  
  write(x = res, file = glue::glue("{folder}/{slurm_scenari}.slurm"))
  
  return(NULL)
}

df_exp1 <- expand.grid(pmutCat = c(0.016, 0.04, 0.1, 0.25),
                       sigmahalv = c(0.1, 0.2, 0.4, 0.8)) |> 
  tibble::rowid_to_column(var = "delayed")

df_exp1 |> 
  apply(MARGIN = 1,
        FUN = function(row){
          generate_slurm_files(folder = "slurm_experiments/explore_ga_exp1",
                               pmutQuant = 0.5,
                               pmutCat = as.numeric(row["pmutCat"]),
                               sigmahalv = as.numeric(row["sigmahalv"]),
                               delayed = (as.numeric(row["delayed"])-1)*3)
        })


df_exp1 |> 
  apply(MARGIN = 1,
        FUN = function(row){
          generate_slurm_files_test(folder = "slurm_experiments/explore_ga_exp1_test",
                                    pmutQuant = 0.5,
                                    pmutCat = as.numeric(row["pmutCat"]),
                                    sigmahalv = as.numeric(row["sigmahalv"]),
                                    delayed = (as.numeric(row["delayed"])-1)*3)
        })


