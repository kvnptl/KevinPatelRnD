import json
import matplotlib.pyplot as plt

log_file = '/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/log.txt'

# Initialize empty dictionaries to hold the extracted values
loss = {}
loss_rpn_cls = {}
loss_rpn_bbox = {}

# Validation loss
map = {}
map_50 = {}
map_75 = {}
map_s = {}
map_m = {}
map_l = {}

# Read the log data from a file and parse each line
with open(log_file, 'r') as f:
    for line in f:
        parsed = json.loads(line.strip())
        
        # Check if the mode is "train" before extracting values
        if parsed['mode'] == 'train':
            epoch = parsed['epoch']
            loss[epoch] = parsed['loss']
            loss_rpn_cls[epoch] = parsed['loss_rpn_cls']
            loss_rpn_bbox[epoch] = parsed['loss_rpn_bbox']

        # Check if the mode is "val" before extracting values
        if parsed['mode'] == 'val':
            map[epoch] = parsed['bbox_mAP']
            map_50[epoch] = parsed['bbox_mAP_50']
            map_75[epoch] = parsed['bbox_mAP_75']
            map_s[epoch] = parsed['bbox_mAP_s']
            map_m[epoch] = parsed['bbox_mAP_m']
            map_l[epoch] = parsed['bbox_mAP_l']

# Convert the dictionaries to lists, preserving the order
loss = [v for k, v in sorted(loss.items())]
loss_rpn_cls = [v for k, v in sorted(loss_rpn_cls.items())]
loss_rpn_bbox = [v for k, v in sorted(loss_rpn_bbox.items())]

map = [v for k, v in sorted(map.items())]
map_50 = [v for k, v in sorted(map_50.items())]
map_75 = [v for k, v in sorted(map_75.items())]
map_s = [v for k, v in sorted(map_s.items())]
map_m = [v for k, v in sorted(map_m.items())]
map_l = [v for k, v in sorted(map_l.items())]

# Plot the extracted values
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(loss)
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(loss_rpn_cls)
plt.title('Loss RPN Class')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(loss_rpn_bbox)
plt.title('Loss RPN BBox')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)

plt.savefig('loss_plots.png')
plt.close()

# Plot for map
# Plot the extracted values
plt.figure(figsize=(20, 10))

plt.subplot(2, 3, 1)
plt.plot(map)
plt.title('map')
plt.xlabel('Epochs')
plt.ylabel('map')
plt.grid(True)

plt.subplot(2, 3, 2)
plt.plot(map_50)
plt.title('map_50')
plt.xlabel('Epochs')
plt.ylabel('map_50')
plt.grid(True)

plt.subplot(2, 3, 3)
plt.plot(map_75)
plt.title('map_75')
plt.xlabel('Epochs')
plt.ylabel('map_75')
plt.grid(True)

plt.subplot(2, 3, 4)
plt.plot(map_s)
plt.title('map_s')
plt.xlabel('Epochs')
plt.ylabel('map_s')
plt.grid(True)

plt.subplot(2, 3, 5)
plt.plot(map_m)
plt.title('map_m')
plt.xlabel('Epochs')
plt.ylabel('map_m')
plt.grid(True)

plt.subplot(2, 3, 6)
plt.plot(map_l)
plt.title('map_l')
plt.xlabel('Epochs')
plt.ylabel('map_l')
plt.grid(True)

plt.savefig('map_plots.png')
plt.tight_layout()