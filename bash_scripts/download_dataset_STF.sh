#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=8    # cores
#SBATCH --mem 8GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 2-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output download_dataset_STF_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error download_dataset_STF_output.%j.err  # filename for STDERR

echo "Downloading SeeingThroughFog dataset..."

cd /scratch/kpatel2s/datasets/STF/downloading
echo "Directory changed to /scratch/kpatel2s/datasets/STF/downloading"

# curl -u dense:B7r1-2AKz-MhXX-sknY --output STF_DELETE.zip https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.zip

echo "Downloading z01 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z01 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z01
echo "Downloading z01 file completed..."

echo "Downloading z02 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z02 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z02
echo "Downloading z02 file completed..."

echo "Downloading z03 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z03 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z03
echo "Downloading z03 file completed..."

echo "Downloading z04 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z04 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z04
echo "Downloading z04 file completed..."

echo "Downloading z05 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z05 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z05
echo "Downloading z05 file completed..."

echo "Downloading z06 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z06 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z06
echo "Downloading z06 file completed..."

echo "Downloading z07 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z07 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z07
echo "Downloading z07 file completed..."

echo "Downloading z08 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z08 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z08
echo "Downloading z08 file completed..."

echo "Downloading z09 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z09 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z09
echo "Downloading z09 file completed..."

echo "Downloading z10 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z10 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z10
echo "Downloading z10 file completed..."

echo "Downloading z11 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z11 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z11
echo "Downloading z11 file completed..."

echo "Downloading z12 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z12 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z12
echo "Downloading z12 file completed..."

echo "Downloading z13 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z13 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z13
echo "Downloading z13 file completed..."

echo "Downloading z14 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z14 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z14
echo "Downloading z14 file completed..."

echo "Downloading z15 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z15 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z15
echo "Downloading z15 file completed..."

echo "Downloading z16 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z16 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z16
echo "Downloading z16 file completed..."

echo "Downloading z17 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z17 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z17
echo "Downloading z17 file completed..."

echo "Downloading z18 file started..."
curl -u dense:B7r1-2AKz-MhXX-sknY --output SeeingThroughFogCompressed.z18 https://cloudstore.uni-ulm.de/training/DENSE/SeeingThroughFogCompressed.z18
echo "Downloading z18 file completed..."