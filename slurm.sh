#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mwl21
# export PATH=/vol/bitbucket/${USER}/nlp-venv/bin/:$PATH

source /vol/cuda/12.0.0/setup.sh
source /vol/bitbucket/mwl21/nlp-venv/bin/activate
/usr/bin/nvidia-smi
uptime

cd /vol/bitbucket/mwl21/nlp-pcl-cw

jupyter nbconvert --execute --to notebook nlp-cw.ipynb