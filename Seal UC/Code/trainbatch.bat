#!/bin/bash
#SBATCH -N 2
#SBATCH -p GPU
#SBATCH --ntasks-per-node 28
#SBATCH -t 5:00:00
#SBATCH --gres=gpu:p100:2

echo "========JOB START========"
set -x

module load python3
module load cuda
module load pytorch
module load gcc

::move to working directory
cd $SCRATCH/SealCode

::run GPU program
python3 terminalsetup.py