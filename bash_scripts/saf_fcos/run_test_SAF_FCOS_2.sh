#!/bin/sh
#SBATCH --partition gpu4       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=1    # cores
#SBATCH --mem 50GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-01:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output evaluation_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error evaluation_output.%j.err  # filename for STDERR

module load gcc/10.1.0 cuda/11.6

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate saf_fcos_cuda11p6

cd /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/SAF-FCOS

python tools/test_net.py \
    --config-file /home/kpatel2s/kpatel2s/test_zone/saf_fcos_method/SAF-FCOS/configs/fcos_nuscenes/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07.yaml \
    --checkpoint-file /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07_LR_0p001/model_0040000.pth \
    OUTPUT_DIR /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07_LR_0p001