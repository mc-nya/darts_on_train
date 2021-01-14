import numpy as np
import os,sys
network_type='small_dataset'
script_output_dir=f'scripts/{network_type}/'
config_dir=f'configs/search_phase/{network_type}/'
if not os.path.exists(script_output_dir):
    os.makedirs(script_output_dir)
for root,dir,file_list in os.walk(config_dir):
    for filename in file_list:
        print(filename)
        file_prefix=filename.split('.')[0]
        save_path=f'results/{network_type}/{file_prefix}/'
        out_file=f'{script_output_dir}/{file_prefix}.sh'
        if not os.path.exists(save_path+'/logs'):
            os.makedirs(save_path+'/logs')
        with open(out_file,mode='w',newline='\n') as script_file:
            script_file.write('#!/bin/bash -l\n')
            script_file.write('#SBATCH --nodes=1\n')
            script_file.write('#SBATCH --cpus-per-task=8\n')
            script_file.write('#SBATCH --mem=16G\n')
            script_file.write('#SBATCH --time=1-12:0:0\n')
            script_file.write('#SBATCH --partition=gputest,gpu\n')
            script_file.write('#SBATCH --gres=gpu:2\n')
            script_file.write(f'#SBATCH --job-name={file_prefix}_{network_type}\n')
            script_file.write(f'#SBATCH --output={save_path}/logs/search.txt\n')
            #script_file.write(f'#SBATCH --mail-user= mail@ucr.edu\n')
            #script_file.write(f'#SBATCH --mail-type=FAIL\n')
            script_file.write('source ~/.bashrc\n')
            script_file.write('conda activate pytorch\n')
            script_file.write('export PYTHONPATH=.\n')
            script_file.write(f'python tools/train_net.py --cfg {config_dir}/{filename} OUT_DIR results/{network_type}/{file_prefix}/search/')
        #os.system(f'sbatch {out_file}')