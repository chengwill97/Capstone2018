#!/bin/bash
#SBATCH -N 1
#SBATCH -p RM-shared
#SBATCH -t 5:00:00
#SBATCH --ntasks-per-node 2

# echo commands to stdout
echo 'JOB START'
set -x


module load python3
module load arcpy

# move to working directory
cd $SCRATCH/StreamExtraction

#run Morphological Thinning program
python3 Thin_multi.py
