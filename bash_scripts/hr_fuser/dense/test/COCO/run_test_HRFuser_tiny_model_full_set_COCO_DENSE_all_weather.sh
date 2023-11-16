#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=32    # cores
#SBATCH --mem 100GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_hrfuser_TINY_dense_r640_l_r_fusion_orig_COCO_day_night_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_hrfuser_TINY_dense_r640_l_r_fusion_orig_COCO_day_night_output.%j.err  # filename for STDERR

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

echo "[bash] Start testing HRFuser TINY model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

#############
### NOTE: change checkpoint path accordingly
#############
weather_list=(test_clear_day test_clear_night light_fog_day light_fog_night dense_fog_day dense_fog_night snow_day snow_night)

for w in "${weather_list[@]}"
do
        python tools/test.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_bn.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/work_dirs/hrfuser_TINY_stf_r1248_4mod_orig_setting_A100_gpu_4_2023-11-10_17-51-55_218951/epoch_60.pth \
                --weather dense_infos_${w} \
                --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/coco/hrfuser_TINY_stf_r1248_4mod_orig_setting_A100_gpu_4_2023-11-10_17-51-55_218951_COCO_day_night_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
                --eval bbox \
                --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/coco/hrfuser_TINY_stf_r1248_4mod_orig_setting_A100_gpu_4_2023-11-10_17-51-55_218951_COCO_day_night_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
                # --cfg-options data.test.samples_per_gpu=32 # 214449 job is with 16
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