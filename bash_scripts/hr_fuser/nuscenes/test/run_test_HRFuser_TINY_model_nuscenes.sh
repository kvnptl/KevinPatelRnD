#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_hrfuser_TINY_nus_r640_l_r_fusion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_hrfuser_TINY_nus_r640_l_r_fusion_output.%j.err  # filename for STDERR

echo "[bash] My HOSTNAME is "
echo `hostname`

# Capture start time
START_TIME=$(date +%s)

CURRENT_DATE_TIME=$(date +"%Y-%m-%d_%H-%M-%S")
echo "[bash] CURRENT_DATE_TIME is ${CURRENT_DATE_TIME}"

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start testing HRFuser TINY model on nuScenes dataset..."

echo -e "[bash] --------------------------------------------\n"

#############
### NOTE: change checkpoint path accordingly
#############
python tools/test.py /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/configs/hrfuser/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_orig_saf_fcos.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/camera_radar/hrfuser_TINY_nuScenes_c_r_fusion_epoch_12_batch_12_orig_config_SAF_FCOS_multi_gpu_2023-11-20_03-38-51_223106/epoch_12.pth \
        --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/inference/camera_radar/hrfuser_TINY_nuScenes_c_r_fusion_epoch_12_batch_12_orig_config_SAF_FCOS_multi_gpu_2023-11-20_03-38-51_223106_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        --eval bbox \
        --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/inference/camera_radar/hrfuser_TINY_nuScenes_c_r_fusion_epoch_12_batch_12_orig_config_SAF_FCOS_multi_gpu_2023-11-20_03-38-51_223106_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        # --cfg-options data.test.samples_per_gpu=32

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