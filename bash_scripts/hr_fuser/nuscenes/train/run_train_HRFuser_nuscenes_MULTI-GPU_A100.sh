#!/bin/sh
#SBATCH --partition gpu4test       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=128    # cores
#SBATCH --mem 500GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output train_multi-gpu_cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error train_multi-gpu_cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start training HRFuser TINY model on nuScenes dataset..."

tools/dist_train.sh configs/hrfuser/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion.py 4 --seed 0

echo "[bash] Training completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

HOURS=$(printf "%02d" $((TOTAL_TIME / 3600)))
MINUTES=$(printf "%02d" $(((TOTAL_TIME % 3600) / 60)))

echo "[bash] Total time taken (HH:MM): ${HOURS}:${MINUTES}"

# how to run:
# cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/bash_scripts
# sbatch run_train_SAF_FCOS.sh