#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=8    # cores
#SBATCH --mem 16GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-23:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output checksum_STF_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error checksum_STF_output.%j.err  # filename for STDERR

echo "Running unzip for SeeingThroughFog dataset..."

cd /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/downloading

echo "Directory changed to /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/downloading"

echo "Running unzip..."

zip -s- SeeingThroughFogCompressed.zip -O zip_file_full.zip

unzip zip_file_full.zip