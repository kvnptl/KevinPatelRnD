import json

def count_keys_in_dict(d):
    count = 0
    for key, value in d.items():
        count += 1  # Counting the current key
        if isinstance(value, dict):
            count += count_keys_in_dict(value)  # Recursively count keys in sub-dictionary
            print(f"key: {key}")
    return count

def modify_json_file(json_data):
    json_data['images'] = json_data['images'][:2]
    json_data['annotations'] = json_data['annotations'][:19]

    # save the modified data back to a new JSON file
    with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_val_modified_2.json', 'w') as f:
        json.dump(json_data, f)

def modify_json_file_hrfuser_nuscenes(json_data):
    json_data['images'] = json_data['images'][:2]
    json_data['annotations'] = json_data['annotations'][:4]
    json_data['lidar_projections'] = json_data['lidar_projections'][:2]
    json_data['radar_projections'] = json_data['radar_projections'][:2]

    # save the modified data back to a new JSON file
    with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d_denug_2.coco.json', 'w') as f:
        json.dump(json_data, f)

# By value
def modify_json_file_hrfuser_nuscenes_2(json_data):
    value = "n008-2018-08-01-15-34-25-0400__CAM_FRONT__1533152351862404"
    at_idx = []
    for image in json_data['images']:
        if value in image['file_name']:
            at_idx.append(json_data['images'].index(image))

    img_data = [json_data['images'][idx] for idx in at_idx]
    json_data['images'] = img_data
    
    # List all annotations belogs to the value image
    at_idx_ann = []
    for annotation in json_data['annotations']:
        if value in annotation['file_name']:
            at_idx_ann.append(json_data['annotations'].index(annotation))
            

    # get all annotations at list of at_idx_ann
    annotations = [json_data['annotations'][idx] for idx in at_idx_ann]
    json_data['annotations'] = annotations

    lidar_data = [json_data['lidar_projections'][idx] for idx in at_idx]
    json_data['lidar_projections'] = lidar_data

    radar_data = [json_data['radar_projections'][idx] for idx in at_idx]
    json_data['radar_projections'] = radar_data

    # save the modified data back to a new JSON file
    with open('/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d_denug_1.coco.json', 'w') as f:
        json.dump(json_data, f)

def modify_json_based_on_id(json_data, id=0):
    """
    Only keep dict whose id is 4
    """
    modified_data = {
        'images': [],
        'lidar_projections': [],
        'radar_projections': [],
        'annotations': [],
        'categories': json_data['categories']
    }
    query = None
    for data in json_data:
        if data == 'annotations':
            query = 'image_id'
        elif data == 'categories':
            continue
        else:
            query = 'id'
        for d in json_data[data]:
            if d[query] == id:
                modified_data[data].append(d)

    # Write the modified data back to the file
    with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1/data/dense/dense_infos_all_modified_coco_2_only_4.json', 'w') as f:
        json.dump(modified_data, f)

def modify_json_based_on_id_mt_detr(json_data, id=0):
    """
    Only keep dict whose id is 4
    """
    modified_data = {
        'images': [],
        'annotations': [],
        'categories': json_data['categories']
    }
    query = None
    for data in json_data:
        if data == 'annotations':
            query = 'image_id'
        elif data == 'categories':
            continue
        else:
            query = 'id'
        for d in json_data[data]:
            if d[query] == id:
                modified_data[data].append(d)

    # Write the modified data back to the file
    with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/dense_fog_night_modified_only_3.json', 'w') as f:
        json.dump(modified_data, f)


def main():
    # json_file_path = '/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_test.json'  # Replace with your JSON file path
    json_file_path = '/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_test_mono3d_saf_fcos.coco.json'
    
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    
    if not isinstance(json_data, dict):
        print("The JSON file does not contain a dictionary (JSON object) at the top level.")
        return

    # Print total number of images
    if 'images' in json_data:
        total_images = len(json_data['images'])
        print(f"The total number of images in the JSON file is {total_images}.")

        # For SAF-FCOS to HRFuser comparison

        # From HRfuset to SAF fcos
        # img_name = 'n015-2018-08-02-17-16-37+0800__CAM_FRONT__1533201470412460.jpg'
        # for image in json_data['images']:
        #     if img_name in image['file_name']:
        #         print(image['file_name'])
        #         breakpoint()

        # From SAF fcos to hrfuser comparison
        # img_name = 'n008-2018-08-01-16-03-27-0400__CAM_FRONT__1533153857912404'
        # for image in json_data['images']:
        #     if 'n008-2018-08-01-16-03-27-0400__CAM_FRONT__1533153857912404' in image['file_name']:
        #         print(f'Found image: {image["file_name"]}')

    total_keys = count_keys_in_dict(json_data)
    
    print(f"The total number of keys in the JSON file is {total_keys}.")

    # modify_json_file(json_data)
    # modify_json_file_hrfuser_nuscenes(json_data)
    modify_json_file_hrfuser_nuscenes_2(json_data)

    # modify_json_based_on_id(json_data, id=4)
    # modify_json_based_on_id_mt_detr(json_data, id=3)

if __name__ == '__main__':
    main()
