#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=32    # cores
#SBATCH --mem 100GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 1-00:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output dense_full_dataset_conversion_output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error dense_full_dataset_conversion_output.%j.err  # filename for STDERR

# Capture start time
START_TIME=$(date +%s)

echo "[bash] Loading GCC and CUDA modules..."

module load gcc/10.1.0 cuda/10.2

. "/home/kpatel2s/anaconda3/etc/profile.d/conda.sh"
conda activate mt_detr

cd /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr

export PYTHONPATH=$PYTHONPATH:`pwd`

echo "[bash] Directory changed to $(pwd)"

echo "[bash] Generating ground truth for DENSE dataset started..."

echo -e "[bash] --------------------------------------------\n"

# Define the list of JSON files
json_file_list=("dense_fog_simple.json" "light_fog_simple.json" "snow_simple.json" "test_clear_simple.json" "train_clear_simple.json" "val_clear_simple.json")

# Loop through each file in the list
for json_file in "${json_file_list[@]}"
do
    # Remove the file extension from the JSON filename
    json_file_without_ext="${json_file%.*}"

    # Execute the Python command with the modified output directory
    python tools/misc/browse_dataset.py /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/configs/mt_detr/mt_detr_c+l+r.py \
        --output-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/ground_truths/${json_file_without_ext} \
        --annotation /home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/${json_file}
done

echo "[bash] Generating ground truth completed..."

# Capture end time
END_TIME=$(date +%s)

# Calculate the total time taken
TOTAL_TIME=$((END_TIME - START_TIME))

HOURS=$(printf "%02d" $((TOTAL_TIME / 3600)))
MINUTES=$(printf "%02d" $(((TOTAL_TIME % 3600) / 60)))

echo "[bash] Total time taken (HH:MM): ${HOURS}:${MINUTES}"