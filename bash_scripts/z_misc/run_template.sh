#!/bin/sh
#SBATCH --partition any       # partition (queue)
#SBATCH --nodes 1                # number of nodes
#SBATCH --ntasks-per-node=64    # cores
#SBATCH --mem 180GB               # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time 0-10:00              # total runtime of job allocation (format D-HH:MM)
#SBATCH --output output.%j.out # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error output.%j.err  # filename for STDERR

module load cuda

cd /home/<username/path/to/code
python main.py \
  --data_root=/scratch/sthodu2m/armbench \
  --training_trials=train.csv \
  --test_trials=test.csv \
  --batch_size=128 \
  --resize_size=224 \
  --crop_size=224 \
  --log_every_n_steps=1 \
  --default_root_dir=<path to save> \
  --learning_rate=0.0001 \
  --max_epochs=200 \
  --n_threads=32 \
  --gpus=1 \
  --accelerator=gpu \
  --progress_bar_refresh_rate=0 \
