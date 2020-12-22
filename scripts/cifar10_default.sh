#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=1-12:0:0
#SBATCH --partition=gpu,gputest
#SBATCH --gres=gpu:2
#SBATCH --job-name=cifar10_default
#SBATCH --output=results/cifar10_default/log.txt
source ~/.bashrc
conda activate pytorch
export PYTHONPATH=.
python tools/train_net.py --cfg configs/search_phase/cifar10_default.yaml
python tools/train_net.py --cfg configs/eval_phase/cifar10_default.yaml

