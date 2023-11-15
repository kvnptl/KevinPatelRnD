#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=32    # cores
#SBATCH --mem 50GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 1-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output dense_full_dataset_ground_truth_generation_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error dense_full_dataset_ground_truth_generation_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/11.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate hrfuser-cuda11p1

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1

export PYTHONPATH=$PYTHONPATH:`pwd`

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Generating ground truth for DENSE dataset started..."

echo -e "[bash] --------------------------------------------\n"

# Define the list of JSON files
# annotation_files_list=("dense_infos_dense_fog.pkl", "dense_infos_light_fog.pkl", "dense_infos_snow.pkl", "dense_infos_test_clear.pkl", "dense_infos_train_clear.pkl", "dense_infos_val_clear.pkl")
# annotation_files_list=("dense_infos_dense_fog.pkl")
annotation_files_list=("dense_infos_val_clear.pkl")
# annotation_files_list=("dense_infos_all.pkl")

# Loop through each file in the list
for annotation_file in "${annotation_files_list[@]}"
do
    # Remove the file extension from the JSON filename
    annotation_file_without_ext="${annotation_file%.*}"

    # Print the current file being processed
    echo "[bash] Processing ${annotation_file}..."

    # Execute the Python command with the modified output directory
    python tools/misc/browse_dataset.py /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1/configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_orig.py \
        --output-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/dense_hrfuser_GT/${annotation_file_without_ext} \
        --annotation /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1/data/dense/${annotation_file}
done

echo "[bash] Generating ground truth completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

HOURS=$(printf "%02d" $((TOTAL_TIME / 3600)))
MINUTES=$(printf "%02d" $(((TOTAL_TIME % 3600) / 60)))

echo "[bash] Total time taken (HH:MM): ${HOURS}:${MINUTES}"