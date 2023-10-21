#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=8    # cores
#SBATCH --mem 8GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-23:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output copy_STF_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error copy_STF_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "Copy SeeingThroughFog dataset..."

cd /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF

echo "Directory changed to /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF"

echo "Running rsync to copy..."

rsync -avh --progress downloading/SeeingThroughFogCompressed .

echo "Copying completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

echo "Total time taken: $TOTAL_TIME seconds"