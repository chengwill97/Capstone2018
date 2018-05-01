#!/bin/bash
#SBATCH -N 1
#SBATCH -p RM-shared
#SBATCH -t 02:00:00
#SBATCH --ntasks-per-node 2

# echo commands to stdout
echo 'JOB START'
set -x

module load mono
module load OSGeo

# move to working directory
cd $SCRATCH

#run StreamExtraction program
mono StreamExtraction.exe
