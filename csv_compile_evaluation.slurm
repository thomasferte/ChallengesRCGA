#!/bin/bash

#############################
# les directives Slurm vont ici:

# Your job name (displayed by the queue)
#SBATCH -J COMPILECSV

# walltime (hh:mm::ss)
#SBATCH -t 05:00:00


# change working directory
# SBATCH --chdir=.

### In filenames, %j=jobid, %a=index in job array
#SBATCH -o /beegfs/tferte/std_out/%j_%a_%x.out # standard out goes to this file
#SBATCH -e /beegfs/tferte/std_err/%j_%a_%x.err # standard err goes to this file

#SBATCH --array 0-15
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem-per-cpu=3560

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

python read_test_files_after_csv_evaluate.py
