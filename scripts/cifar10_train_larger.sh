#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=1-12:0:0
#SBATCH --partition=gpu,gputest
#SBATCH --gres=gpu:2
#SBATCH --job-name=cifar10_train_larger
#SBATCH --output=results/cifar10_train_larger/log.txt
source ~/.bashrc
conda activate pytorch
export PYTHONPATH=.
python tools/train_net.py --cfg configs/search_phase/cifar10_train_larger.yaml
#python tools/train_net.py --cfg configs/eval_phase/cifar10_train_larger.yaml

