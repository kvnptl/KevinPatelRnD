#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 20GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-10:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output dense_dataset_conversion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error dense_dataset_conversion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Start conversion of DENSE dataset..."

echo "[bash] Part 1 started..."

python SeeingThroughFog/tools/ProjectionTools/run_2d_projection_on_dataset.py -f RGB2Gatedv2 -t lidar_hdl64 -r data/dense/ -l all

echo "[bash] Part 1 completed..."

echo "[bash] Part 2 started..."

python SeeingThroughFog/tools/ProjectionTools/Gated2RGB/run_depth_warping.py -l all

echo "[bash] Part 2 completed..."

echo "[bash] Conversion completed..."

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