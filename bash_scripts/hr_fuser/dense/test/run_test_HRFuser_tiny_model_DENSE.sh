#!/bin/sh
#SBATCH --partition gpu       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-24:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output test_cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error test_cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start testing HRFuser TINY model on DENSE dataset..."

#############
### NOTE: change checkpoint path accordingly
#############
python tools/test.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod.py checkpoints/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_latest.pth \
        --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/work_dirs/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_Provided_Inference \
        --eval bbox \
        --show \
        --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/work_dirs/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_Provided_Inference \
        --cfg-options data.test.samples_per_gpu=1

echo "[bash] Testing completed..."

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