#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_early_c+l+r_10_perc_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_early_c+l+r_10_perc_output.%j.err  # filename for STDERR

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

echo "[bash] Start testing early Camera + Lidar + Radar model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

#############
### NOTE: change checkpoint path accordingly
#############
weather_list=(test_clear_day test_clear_night light_fog_day_test_set light_fog_night_test_set dense_fog_day_test_set dense_fog_night_test_set snow_day_test_set snow_night_test_set)

for w in "${weather_list[@]}"
do
    python tools/test.py \
        configs/mt_detr/early_c+l+r.py \
        /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/work_dirs/early_fusion/early_camera_lidar_radar_single_gpu_2023-10-30_03-28-55_214253/epoch_36.pth \
        --weather ${w} \
        --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/early_fusion/early_camera_lidar_radar_single_gpu_2023-10-30_03-28-55_214253_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        --eval bbox \
        --show \
        --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/early_fusion/early_camera_lidar_radar_single_gpu_2023-10-30_03-28-55_214253_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        # --cfg-options data.test.samples_per_gpu=16
done

echo "[bash] Testing completed..."

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