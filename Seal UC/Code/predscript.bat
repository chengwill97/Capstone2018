#!/bin/bash
#SBATCH -N 2
#SBATCH -p GPU
#SBATCH --ntasks-per-node 28
#SBATCH -t 1:00:00
#SBATCH --gres=gpu:p100:2

echo "========JOB START========"
set -x

module load python3
module load cuda
module load opencv
module load gcc

cd $SCRATCH/predict_temp4

python3 predictionsetup.py

python3 pt_predict.py -class_names 'crabeater' 'weddel' 'pack-ice' 'other'

python3 blob_detector.py