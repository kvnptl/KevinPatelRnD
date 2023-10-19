#!/bin/bash
#SBATCH --partition=gpu          # partition (queue)
#SBATCH --nodes=1                # number of nodes
#SBATCH --ntasks-per-node=64     # number of cores per node
#SBATCH --mem=100G                # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time=40:00:00          # total runtime of job allocation ((format D-HH:MM:SS; first parts optional)
#SBATCH --output=slurm.%j.out    # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error=slurm.%j.err     # filename for STDERR

. "/home/sshind2s/anaconda3/etc/profile.d/conda.sh"
conda activate torchtime-gpu 
python3 model_training_torchtime.py