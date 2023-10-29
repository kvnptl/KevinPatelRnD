#!/bin/sh
#SBATCH --partition gpu4test       # partition (queue)
#SBATCH --nodelist=wr25
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 480GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 3-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output train_multi_A100_gpu_epochs_60_batch_size_12_lr_0p_hrfuser_TINY_Dense_r640_l_r_fusion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error train_multi_A100_gpu_epochs_60_batch_size_12_lr_0p_hrfuser_TINY_Dense_r640_l_r_fusion_output.%j.err  # filename for STDERR

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

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start training HRFuser TINY model on DENSE dataset..."

echo -e "[bash] --------------------------------------------\n"

python tools/train.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_ver2.py \
                    --seed 8 \
                    --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/work_dirs/hrfuser_TINY_stf_r1248_4mod_epoch_60_batch_2_lr_0p001_A100_gpu_4_${CURRENT_DATE_TIME}_${SLURM_JOB_ID} 

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