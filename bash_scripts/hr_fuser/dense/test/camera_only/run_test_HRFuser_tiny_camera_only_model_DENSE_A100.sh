#!/bin/sh
#SBATCH --partition gpu4test       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=32    # cores
#SBATCH --mem 150GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_hrfuser_TINY_dense_camera_only_fusion_A100_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_hrfuser_TINY_dense_camera_only_fusion_A100_output.%j.err  # filename for STDERR

export MODULEPATH=/usr/local/modules/modulesfiles_8:$MODULEPATH
. /etc/profile.d/modules.sh
. /usr/local/etc/profile

echo "[bash] My HOSTNAME is "
echo `hostname`

# Capture start time
START_TIME=$(date +%s)

CURRENT_DATE_TIME=$(date +"%Y-%m-%d_%H-%M-%S")
echo "[bash] CURRENT_DATE_TIME is ${CURRENT_DATE_TIME}"

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/11.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda11p1

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start training HRFuser TINY model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

#############
### NOTE: change checkpoint path accordingly
#############
python tools/test.py configs/hrformer/cascade_rcnn_hrformer_t_1x_stf_c1248.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/work_dirs/camera_only/hrfuser_TINY_stf_c1248_camera_only_orig_setting_multi_gpu_4_2023-11-10_21-57-56_218957/epoch_60.pth \
        --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/camera_only/ground_truth_images_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        --gpu-ids 1 \
        --eval bbox \
        --show \
        --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/camera_only/ground_truth_images_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} \
        --cfg-options data.test.samples_per_gpu=128 # 214449 job is with 16

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