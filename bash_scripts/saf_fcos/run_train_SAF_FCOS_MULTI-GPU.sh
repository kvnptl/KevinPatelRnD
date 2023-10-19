#!/bin/sh
#SBATCH --partition gpu4       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-20:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output saf_fcos_LR_0p001_workers_16_4_GPUs_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error saf_fcos_LR_0p001_workers_16_4_GPUs_output.%j.err  # filename for STDERR

module load gcc/10.1.0 cuda/11.6

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate saf_fcos_cuda11p6

cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/SAF-FCOS

python -m torch.distributed.run \
    --nproc_per_node=4 \
    --master_port=$((RANDOM + 10000)) \
    tools/train_net.py \
    --config-file configs/fcos_nuscenes/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07.yaml \
    --norm-info-folder /scratch/kpatel2s/datasets/nuScenes/v1.0-trainval/norm_info \
    DATALOADER.NUM_WORKERS 16 \
    OUTPUT_DIR /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver3/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07_LR_0p001_workers_16_4_GPUs

# how to run:
# cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/bash_scripts
# sbatch run_train_SAF_FCOS.sh