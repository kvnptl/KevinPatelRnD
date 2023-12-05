import json
from collections import defaultdict
import os
from tqdm import tqdm

"""
This module provides utilities for converting datasets between KITTI and COCO formats and for extracting unique classes from these datasets.

The module consists of three main functions:
1. `kitti_to_coco` - Converts a dataset from the KITTI format to the COCO format. It handles the conversion of images, lidar projections, radar projections, annotations, and categories. The function also supports using a sample COCO file as a reference for the conversion process.

2. `extract_unique_classes_kitti` - Extracts and lists unique object classes from a dataset in KITTI format. This function reads through the annotations in the KITTI dataset and gathers all unique class names, providing insights into the variety of objects annotated in the dataset.

3. `extract_unique_classes_coco` - Similar to `extract_unique_classes_kitti`, but for datasets in COCO format. It parses the categories section of a COCO dataset to list out all unique object classes present.

These utilities are particularly useful in computer vision and deep learning applications, where data often needs to be converted between different annotation formats for training object detection models.
"""

def kitti_to_coco(kitti_file, coco_file, sample_coco_file=None):
    """
    Converts KITTI format annotations to COCO format.

    This function transforms a dataset from the KITTI format to the COCO format.
    It handles images, lidar projections, radar projections, annotations, and
    categories. It also supports an optional sample COCO file for reference.

    Parameters:
    - kitti_file (str): Path to the KITTI format file.
    - coco_file (str): Path where the COCO format file will be saved.
    - sample_coco_file (str, optional): Path to a sample COCO format file used for reference.

    The function processes each image in the KITI dataset, converting and
    appending corresponding data to the COCO format. Annotations are grouped by
    image_id and sorted by category_id. Category IDs are mapped and annotations
    are re-assigned new IDs for consistency. The final COCO data is written to
    the specified output file.

    Example Usage:
    ```
    sample_coco_file = "/path/to/sample/coco_file.json"
    kitti_file = "/path/to/kitti_file.json"
    coco_file = "/path/to/output/coco_file.json"
    kitti_to_coco(kitti_file, coco_file, sample_coco_file)
    ```
    """

    # Just for ref
    if sample_coco_file is not None:
        with open(sample_coco_file, 'r') as f:
            sample_coco_data = json.load(f)

    with open(kitti_file, 'r') as f:
        kitti_data = json.load(f)

    coco_data = {
        "images": [],
        "lidar_projections": [],
        "radar_projections": [],
        "annotations": [],
        "categories": []
    }

    category_mapping = {}
    next_category_id = 0
    next_image_id = 0
    next_annotation_id = 0

    for image_info in kitti_data:
        try:
            # Process image information
            coco_image = {
                "id": next_image_id,
                "file_name": image_info['image']['image_path'],
                "height": image_info['image']['image_shape'][0],
                "width": image_info['image']['image_shape'][1],
            }
            coco_data["images"].append(coco_image)

            # Process lidar projections
            lidar_projection = {
                "id": next_image_id,
                "width": image_info['lidar_projections']['image_shape'][1],
                "height": image_info['lidar_projections']['image_shape'][0],
                "yzi": {
                    "file_name": image_info['lidar_projections']['yzi']['file_name'],
                    "pixel_scale_factor": image_info['lidar_projections']['yzi']['pixel_scale_factor'],
                    "shift": image_info['lidar_projections']['yzi']['shift'],
                    "empty_channels": image_info['lidar_projections']['yzi']['empty_channels']
                }
            }
            coco_data["lidar_projections"].append(lidar_projection)

            # Process radar projections
            radar_projection = {
                "id": next_image_id,
                "width": image_info['radar_projections']['image_shape'][1],
                "height": image_info['radar_projections']['image_shape'][0],
                "yzv": {
                    "file_name": image_info['radar_projections']['yzv']['file_name'],
                    "pixel_scale_factor": image_info['radar_projections']['yzv']['pixel_scale_factor'],
                    "shift": image_info['radar_projections']['yzv']['shift'],
                    "empty_channels": image_info['radar_projections']['yzv']['empty_channels']
                }
            }
            coco_data["radar_projections"].append(radar_projection)

            # Process annotations
            for i, name in enumerate(image_info['annos']['name']):
                # Create category if it doesn't exist
                if name == 'Car' or name == 'Van':
                    super_category = 'Car'
                    next_category_id = 2
                    name = 'Car'
                elif name == 'Pedestrian':
                    super_category = 'Pedestrian'
                    next_category_id = 0
                elif name == 'Cyclist':
                    super_category = 'Cyclist'
                    next_category_id = 1
                elif name == 'ignore':
                    continue
                elif name == 'DontCare':
                    continue
                else:
                    super_category = 'other'

                if name not in category_mapping:

                    category_mapping[name] = next_category_id
                    coco_data["categories"].append({
                        "supercategory": super_category,
                        "id": next_category_id,
                        "name": name
                    })
                    next_category_id += 1

                # Convert KITTI bbox to COCO bbox format
                kitti_bbox = image_info['annos']['bbox'][i]
                coco_bbox = [kitti_bbox[0], kitti_bbox[1], kitti_bbox[2] - kitti_bbox[0], kitti_bbox[3] - kitti_bbox[1]]

                area = coco_bbox[2] * coco_bbox[3]  # width * height
                coco_anno = {
                    "image_id": next_image_id,
                    "id": next_annotation_id,
                    "category_id": category_mapping[name],
                    "bbox": coco_bbox,
                    "area": area,
                    "iscrowd": 0
                }
                coco_data["annotations"].append(coco_anno)
                next_annotation_id += 1

            next_image_id += 1

        except KeyError as e:
            print(f"Missing key in data: {e}")

    # Group annotations by image_id
    grouped_annotations = defaultdict(list)
    for anno in coco_data["annotations"]:
        grouped_annotations[anno["image_id"]].append(anno)

    # Sort annotations within each group by category_id
    for image_id in grouped_annotations:
        grouped_annotations[image_id] = sorted(grouped_annotations[image_id], key=lambda x: x["category_id"])

    # Flatten the grouped annotations back into a list
    sorted_annotations = [anno for sublist in grouped_annotations.values() for anno in sublist]

    # Update coco_data with sorted annotations
    coco_data["annotations"] = sorted_annotations

    # Generate new id for annotations in ascending order
    for i, anno in enumerate(coco_data["annotations"]):
        coco_data["annotations"][i]["id"] = i

    # Sort categories by 'id' in ascending order
    coco_data["categories"] = sorted(coco_data["categories"], key=lambda x: x["id"])
    
    # Write COCO data to file
    with open(coco_file, 'w') as f:
        json.dump(coco_data, f, indent=4)


# Usage example

sample_coco_file = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/dense_fog_night_modified.json"

json_files_dir = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_json_files"
dest_dir = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/coco_annotations"

for json_file in tqdm(os.listdir(json_files_dir)):
    if json_file.endswith(".json"):
        json_file_path = os.path.join(json_files_dir, json_file)
        coco_file_path = os.path.join(dest_dir, json_file.replace(".json", "_coco.json"))
        kitti_to_coco(json_file_path, coco_file_path)

# kitti_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_json_files/dense_infos_all_modified.json'
# coco_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_json_files/dense_infos_all_modified_coco_2.json'
# kitti_to_coco(kitti_file, coco_file)



def extract_unique_classes_kitti(kitti_file):
    """
    Extracts and prints unique classes from a KITTI format file.

    This function reads a KITTI format file, extracts unique object classes
    present in the annotations, and prints them in a sorted list. It also
    calculates the total number of images in the dataset.

    Parameters:
    - kitti_file (str): Path to the KITTI format file.

    Returns:
    - set: A set of unique class names found in the file.

    The function processes the KITTI file, gathers unique names from the
    annotations, and returns them as a sorted set. It also prints the total
    number of images in the dataset.

    Example Usage:
    ```
    kitti_file = "/path/to/kitti_file.json"
    unique_classes = extract_unique_classes_kitti(kitti_file)
    ```
    """
    with open(kitti_file, 'r') as file:
        data = json.load(file)

    unique_classes = set()
    for item in data:
        if 'annos' in item and 'name' in item['annos']:
            for name in item['annos']['name']:
                unique_classes.add(name)

    # Sort the unique classes
    unique_classes = sorted(unique_classes)
    print(f'Sorted unique classes: {unique_classes}')

    # Calculate total images
    total_images = len(data)
    print(f'Total images: {total_images}')

    return unique_classes

import json

def extract_unique_classes_coco(coco_file):
    """
    Extracts and prints unique classes from a COCO format file.

    This function reads a COCO format file, extracts unique object classes
    present in the category section, and prints them. It also calculates and
    prints the total number of images in the dataset.

    Parameters:
    - coco_file (str): Path to the COCO format file.

    Returns:
    - tuple: A set of unique class names and the total number of images.

    The function processes the COCO file, gathers unique category names, and
    returns them as a set. It also calculates and prints the total number of
    images in the dataset.

    Example Usage:
    ```
    coco_file = "/path/to/coco_file.json"
    unique_classes, total_images = extract_unique_classes_coco(coco_file)
    ```
    """
    with open(coco_file, 'r') as file:
        data = json.load(file)

    unique_classes = set()
    if 'categories' in data:
        for category in data['categories']:
            class_name = category.get('name')
            if class_name:
                unique_classes.add(class_name)

    total_images = len(data['images']) if 'images' in data else 0

    print(f"Unique Classes: {unique_classes}")
    print(f"Total Number of Images: {total_images}")

    return unique_classes, total_images

# Usage example
# coco_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/train_clear_simple.json'
# unique_classes, total_images = extract_unique_classes_coco(coco_file)


# Usage example
# kitti_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_json_files/dense_infos_all.json'
# unique_classes = extract_unique_classes_kitti(kitti_file)
