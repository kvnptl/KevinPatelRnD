import json

# Load your Method 2 annotations
with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_test.json') as file:
    data = json.load(file)

# Destination json file 
with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d.coco.json', 'w') as file:
    target_data = json.load(file)

# Original and target image dimensions
original_width, original_height = data['images'][0]['width'], data['images'][0]['height']
target_width, target_height = target_data['images'][0]['width'], target_data['images'][0]['height']

# Calculate scaling factors
scale_x = target_width / original_width
scale_y = target_height / original_height

# Function to scale a single bounding box
def scale_bbox(bbox):
    x, y, width, height = bbox
    scaled_x = x * scale_x
    scaled_y = y * scale_y
    scaled_width = width * scale_x
    scaled_height = height * scale_y
    scaled_area = scaled_width * scaled_height
    return [scaled_x, scaled_y, scaled_width, scaled_height, scaled_area]

# Scale all bounding boxes
for annotation in data['annotations']:
    bbox = annotation['bbox']
    scaled_bbox = scale_bbox(bbox)
    annotation['bbox'] = scaled_bbox[:4]
    annotation['area'] = scaled_bbox[4]

# Save the transformed annotations
with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_val_modified_2_640_360.json', 'w') as file:
    json.dump(data, file)

print("Conversion complete. The annotations are saved in 'method1_converted_annotations.json'")
