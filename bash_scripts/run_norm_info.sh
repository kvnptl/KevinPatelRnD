#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 32GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-20:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error output.%j.err  # filename for STDERR

module load gcc/10.1.0 cuda/11.6

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate saf_fcos_cuda11p6

cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/SAF-FCOS

# python tools/nuscenes/convert_radar_point.py --dataroot /scratch/kpatel2s/datasets/nuScenes
python tools/nuscenes/extract_pc_image_norm_info_from_image.py --datadir /scratch/kpatel2s/datasets/nuScenes --outdir /scratch/kpatel2s/datasets/nuScenes/v1.0-trainval
