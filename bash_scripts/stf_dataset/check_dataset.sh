#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=8    # cores
#SBATCH --mem 8GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-20:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output checksum_STF_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error checksum_STF_output.%j.err  # filename for STDERR

echo "Running checksum for SeeingThroughFog dataset..."

cd /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/downloading

echo "Directory changed to /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/downloading"

echo "Running checksum..."

sha256sum -c SeeingThroughFog_sha256sum.txt