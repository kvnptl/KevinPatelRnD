#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=8    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-20:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output nuscenes_dataset_conversion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error nuscenes_dataset_conversion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda102-torch110-mmcv-full-1317

echo "Converting Nuscenes dataset..."

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser

echo "Directory changed to $(pwd)"

echo "Conversion started..."

python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes --version v1.0-mini

echo "Conversion completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

echo "Total time taken: $TOTAL_TIME seconds"

echo "Total time taken: $((TOTAL_TIME / 60)) minutes"

echo "Total time taken: $((TOTAL_TIME / 3600)) hours"