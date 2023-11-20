import json
import os
from tqdm import tqdm

saf_fcos_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_train.json"

hrfuser_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_train_mono3d.coco.json"
hrfuser_json_val = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_val_mono3d.coco.json"

hrfuser_json_test = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d.coco.json"
run_testset = False

new_hrfuser_json = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d_saf_fcos.coco.json"

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        return False
    return True

# Function to load JSON data
def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# Load data from JSON files
saf_fcos_data = load_json(saf_fcos_json)
hrfuser_data = load_json(hrfuser_json)
hrfuser_data_val = load_json(hrfuser_json_val)
hrfuser_data_test = load_json(hrfuser_json_test)

saf_fcos_bboxes = []
saf_fcos_areas = []
saf_fcos_iscrowds = []
saf_fcos_image_ids = []

# Function to extract base file names
def extract_base_file_names(json_data):
    # return {name.split('__')[0] for name in (img["file_name"] for img in json_data["images"])}
    base_names = set()

    for img in json_data["images"]:
        file_name = img["file_name"]
        # base_name = file_name.split('/')[-1].split('__')[0]
        base_name = file_name.split('/')[-1].split('.')[0]
        base_names.add(base_name)

        # Get bboxes, area, iscrowd
        image_id = img["id"]
        for ann in json_data["annotations"]:
            if ann["image_id"] == image_id:
                saf_fcos_bboxes.append(ann["bbox"])
                saf_fcos_areas.append(ann["area"])
                saf_fcos_iscrowds.append(ann["iscrowd"])
                saf_fcos_image_ids.append(image_id)
    
    print(f"Number of base names: {len(base_names)}")
    return base_names

# Extract base file names from Method 2
base_names_saf_fcos = extract_base_file_names(saf_fcos_data)

def filter_data(data, base_names):
    return [item for item in data if item["file_name"].split('/')[-1].split('.')[0] in base_names]

filtered_images = filter_data(hrfuser_data["images"], base_names_saf_fcos)
filtered_images += filter_data(hrfuser_data_val["images"], base_names_saf_fcos)

if run_testset:
    filtered_images += filter_data(hrfuser_data_test["images"], base_names_saf_fcos)

print(f"Number of filtered images: {len(filtered_images)}")

filtered_lidar_projections = []
for lidar in hrfuser_data["lidar_projections"]:
    if lidar['rih']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_lidar_projections.append(lidar)

for lidar in hrfuser_data_val["lidar_projections"]:
    if lidar['rih']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
        filtered_lidar_projections.append(lidar)

if run_testset:
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

if run_testset:
    for radar in hrfuser_data_test["radar_projections"]:
        if radar['riv']["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
            filtered_radar_projections.append(radar)

ann_id_cnt = 0
# Filter annotations based on filtered images
filtered_annotations = []
if not run_testset:
    for ann in hrfuser_data["annotations"]:
        if ann["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
            ann["id"] = ann_id_cnt
            filtered_annotations.append(ann)
            ann_id_cnt += 1

    for ann in hrfuser_data_val["annotations"]:
        if ann["file_name"].split('/')[-1].split('.')[0] in base_names_saf_fcos:
            ann["id"] = ann_id_cnt
            filtered_annotations.append(ann)
            ann_id_cnt += 1

    categories = hrfuser_data["categories"]

else:

    for i, img in enumerate(filtered_images):
        
        img_name = img["file_name"].split('/')[-1].split('.')[0]
        
        for saf_fcos_img in saf_fcos_data["images"]:
            if saf_fcos_img["file_name"].split('/')[-1].split('.')[0] == img_name:
                for ann_saf_fcos in saf_fcos_data["annotations"]:
                    if ann_saf_fcos["image_id"] == saf_fcos_img["id"]:
                        
                        # Create a new annotation dictionary with 
                        new_ann = {
                            "file_name": img['file_name'],
                            "image_id": img['id'],
                            "area": ann_saf_fcos["area"],
                            "category_name": "vehicle", # fixed as only one class
                            "category_id": 0, # fixed as only one class
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



# Copy only "bbox" key annotations from saf_fcos data


# Create new JSON with filtered data
new_hrfuser_data = {
    "annotations": filtered_annotations,
    "images": filtered_images,
    "lidar_projections": filtered_lidar_projections,
    "radar_projections": filtered_radar_projections,
    "categories": categories
}

# Write to a new JSON file
with open(new_hrfuser_json, 'w') as f:
    json.dump(new_hrfuser_data, f)

print("Done")