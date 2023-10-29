#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_mt_detr_camera_only_weather_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_mt_detr_camera_only_weather_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate mt_detr

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start testing MT-DETR Camera only model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

#############
### NOTE: change checkpoint path accordingly
#############
weather_list=(test_clear_day test_clear_night light_fog_day light_fog_night dense_fog_day dense_fog_night snow_day snow_night)

for w in "${weather_list[@]}"
do
    python tools/test.py \
        configs/mt_detr/camera_only.py \
        checkpoint/model/camera_only.pth \
        --weather ${w} \
        --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/camera_only_weather_provided \
        --eval bbox \
        --show \
        --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/camera_only_weather_provided \
        --cfg-options data.test.samples_per_gpu=1
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