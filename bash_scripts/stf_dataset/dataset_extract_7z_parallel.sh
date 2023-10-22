#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=24    # cores
#SBATCH --mem 100GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-23:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output dataset_extract_7z_parallel_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error dataset_extract_7z_parallel_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "Extract SeeingThroughFog dataset..."

echo "Extraction started..."

python /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/dataset_extraction_7z.py

echo "Extract completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

HOURS=$(printf "%02d" $((TOTAL_TIME / 3600)))
MINUTES=$(printf "%02d" $(((TOTAL_TIME % 3600) / 60)))

echo "[bash] Total time taken: ${HOURS}:${MINUTES}"