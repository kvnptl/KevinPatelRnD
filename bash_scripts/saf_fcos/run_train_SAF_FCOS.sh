#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-20:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error output.%j.err  # filename for STDERR

module load gcc/10.1.0 cuda/11.6

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate saf_fcos_cuda11p6

cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/SAF-FCOS

python tools/train_net.py \
    --config-file configs/fcos_nuscenes/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07.yaml \
    --norm-info-folder /scratch/kpatel2s/datasets/nuScenes/v1.0-trainval/norm_info \
    DATALOADER.NUM_WORKERS 8 \
    OUTPUT_DIR tmp/fcos_imprv_R_50_FPN_1x

# how to run:
# cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/bash_scripts
# sbatch run_train_SAF_FCOS.sh