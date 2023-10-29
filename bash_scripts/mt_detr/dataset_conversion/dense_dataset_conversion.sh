#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=32    # cores
#SBATCH --mem 10GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 1-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output dense_full_dataset_conversion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error dense_full_dataset_conversion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate LabelTool

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/SeeingThroughFog

export PYTHONPATH=$PYTHONPATH:`pwd`

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Conversion of DENSE dataset started..."

echo -e "[bash] --------------------------------------------\n"

python /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/SeeingThroughFog/tools/ProjectionTools/Lidar2RGB/run_2d_projection.py -r /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/SeeingThroughFogCompressed_extracted

echo "[bash] Conversion completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

HOURS=$(printf "%02d" $((TOTAL_TIME / 3600)))
MINUTES=$(printf "%02d" $(((TOTAL_TIME % 3600) / 60)))

echo "[bash] Total time taken (HH:MM): ${HOURS}:${MINUTES}"