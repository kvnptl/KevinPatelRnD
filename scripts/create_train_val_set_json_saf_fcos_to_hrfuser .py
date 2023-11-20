import json
import os
from tqdm import tqdm

# Define file paths
saf_fcos_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_val.json"

hrfuser_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_train_mono3d.coco.json"
hrfuser_json_val = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_val_mono3d.coco.json"

hrfuser_json_test = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d.coco.json"
run_testset = False

new_hrfuser_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_val_mono3d_saf_fcos.coco.json"

# Function to load JSON data
def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

print("Loading data...")
# Load data from JSON files
saf_fcos_data = load_json(saf_fcos_json)
hrfuser_data = load_json(hrfuser_json)
hrfuser_data_val = load_json(hrfuser_json_val)
hrfuser_data_test = load_json(hrfuser_json_test)

# Function to extract base file names and preprocess data
def preprocess_data(json_data):
    base_names = set()
    image_id_to_data = {}

    for img in json_data["images"]:
        file_base = img["file_name"].split('/')[-1].split('.')[0]
        base_names.add(file_base)
        image_id_to_data[img["id"]] = img

    annotations = {ann["image_id"]: ann for ann in json_data["annotations"]}
    return base_names, image_id_to_data, annotations

print("Preprocessing data...")
base_names_saf_fcos, saf_fcos_images, saf_fcos_annotations = preprocess_data(saf_fcos_data)

# Function to filter data based on base names
def filter_data(data, base_names):
    return [item for item in data if item["file_name"].split('/')[-1].split('.')[0] in base_names]

print("Filtering data...")
filtered_images = filter_data(hrfuser_data["images"], base_names_saf_fcos)
filtered_images += filter_data(hrfuser_data_val["images"], base_names_saf_fcos)
filtered_images += filter_data(hrfuser_data_test["images"], base_names_saf_fcos)

print(f"Number of filtered images: {len(filtered_images)}")

# filtered_lidar_projections = filter_data(hrfuser_data["lidar_projections"], base_names_saf_fcos)
# filtered_lidar_projections += filter_data(hrfuser_data_val["lidar_projections"], base_names_saf_fcos)
# filtered_lidar_projections += filter_data(hrfuser_data_test["lidar_projections"], base_names_saf_fcos)

# filtered_radar_projections = filter_data(hrfuser_data["radar_projections"], base_names_saf_fcos)
# filtered_radar_projections += filter_data(hrfuser_data_val["radar_projections"], base_names_saf_fcos)
# filtered_radar_projections += filter_data(hrfuser_data_test["radar_projections"], base_names_saf_fcos)


filtered_lidar_projections = []
for lidar in hrfuser_data["lidar_projections"]:
    if lidar['rih']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_lidar_projections.append(lidar)

for lidar in hrfuser_data_val["lidar_projections"]:
    if lidar['rih']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_lidar_projections.append(lidar)

for lidar in hrfuser_data_test["lidar_projections"]:
    if lidar['rih']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_lidar_projections.append(lidar)
# =======================================================================================
filtered_radar_projections = []
for radar in hrfuser_data["radar_projections"]:
    if radar['riv']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_radar_projections.append(radar)

for radar in hrfuser_data_val["radar_projections"]:
    if radar['riv']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_radar_projections.append(radar)

for radar in hrfuser_data_test["radar_projections"]:
    if radar['riv']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_radar_projections.append(radar)


# Filter and create annotations
# Create a dictionary for quick lookup of saf_fcos image IDs by base file name
saf_fcos_image_id_lookup = {img["file_name"].split('/')[-1].split('.')[0]: img["id"] 
                            for img in saf_fcos_data["images"]}

# Create a dictionary for quick lookup of saf_fcos annotations by image ID, allowing multiple annotations per image
saf_fcos_annotation_lookup = {}
for ann in saf_fcos_data["annotations"]:
    if ann["image_id"] in saf_fcos_annotation_lookup:
        saf_fcos_annotation_lookup[ann["image_id"]].append(ann)
    else:
        saf_fcos_annotation_lookup[ann["image_id"]] = [ann]

ann_id_cnt = 0
filtered_annotations = []

print("Filtering annotations...")
if not run_testset:
    for ann in hrfuser_data["annotations"]:
        if ann["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
            ann["id"] = ann_id_cnt
            ann["category_name"] = "vehicle" # Fixed class to match with SAF FCOS
            ann["category_id"] = 0 # Fixed class to match with SAF FCOS
            filtered_annotations.append(ann)
            ann_id_cnt += 1

    for ann in hrfuser_data_val["annotations"]:
        if ann["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
            ann["id"] = ann_id_cnt
            ann["category_name"] = "vehicle" # Fixed class to match with SAF FCOS
            ann["category_id"] = 0 # Fixed class to match with SAF FCOS
            filtered_annotations.append(ann)
            ann_id_cnt += 1

    categories = saf_fcos_data["categories"]
    categories[0]["id"] = 0
    
else:
    for img in filtered_images:
        img_base_name = img["file_name"].split('/')[-1].split('.')[0]
        
        if img_base_name in saf_fcos_image_id_lookup:
            saf_fcos_image_id = saf_fcos_image_id_lookup[img_base_name]

            # Iterate over all annotations for the specific image
            if saf_fcos_image_id in saf_fcos_annotation_lookup:
                for ann_saf_fcos in saf_fcos_annotation_lookup[saf_fcos_image_id]:
                    new_ann = {
                        "file_name": img['file_name'],
                        "image_id": img['id'],
                        "area": ann_saf_fcos["area"],
                        "category_name": "vehicle",
                        "category_id": 0,
                        "bbox": ann_saf_fcos["bbox"],
                        "iscrowd": ann_saf_fcos["iscrowd"],
                        "visibility_token": '2',
                        "bbox_cam3d": '',
                        "velo_cam3d": '',
                        "center2d": '',
                        "attribute_name": '',
                        "attribute_id": '',
                        "segmentation": '',
                        "id": ann_id_cnt
                    }
                    filtered_annotations.append(new_ann)
                    ann_id_cnt += 1

    categories = saf_fcos_data["categories"]
    categories[0]["id"] = 0

# Create new JSON with filtered data
new_hrfuser_data = {
    "annotations": filtered_annotations,
    "images": filtered_images,
    "lidar_projections": filtered_lidar_projections,
    "radar_projections": filtered_radar_projections,
    "categories": categories
}

print("Writing to {}...".format(new_hrfuser_json))
# Write to a new JSON file
with open(new_hrfuser_json, 'w') as f:
    json.dump(new_hrfuser_data, f)

print("Done")