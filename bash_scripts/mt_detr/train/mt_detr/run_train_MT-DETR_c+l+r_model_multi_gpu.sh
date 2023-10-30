#!/bin/sh
#SBATCH --partition gpu4       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 3-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output train_mt_detr_c+l+r_multi_gpu_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error train_mt_detr_c+l+r_multi_gpu_output.%j.err  # filename for STDERR

echo "[bash] My HOSTNAME is "
echo `hostname`

# Capture start time
START_TIME=$(date +%s)

CURRENT_DATE_TIME=$(date +"%Y-%m-%d_%H-%M-%S")
echo "[bash] CURRENT_DATE_TIME is ${CURRENT_DATE_TIME}"

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate mt_detr

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start training MT-DETR Camera + Lidar + Radar model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

tools/dist_train.sh configs/mt_detr/mt_detr_c+l+r.py \
                    4 \
                    --seed 0 \
                    --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/work_dirs/camera_lidar_radar_multi_gpu_${CURRENT_DATE_TIME}_${SLURM_JOB_ID}


echo "[bash] Training completed..."

echo -e "[bash] --------------------------------------------\n"

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