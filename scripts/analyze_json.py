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
    json_data['images'] = json_data['images'][:5]
    json_data['annotations'] = json_data['annotations'][:23]

    # save the modified data back to a new JSON file
    with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/dense_fog_night_modified_2.json', 'w') as f:
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
    json_file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser_cuda11p1/data/dense/dense_infos_all_modified_coco_2.json'  # Replace with your JSON file path
    
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    
    if not isinstance(json_data, dict):
        print("The JSON file does not contain a dictionary (JSON object) at the top level.")
        return

    total_keys = count_keys_in_dict(json_data)
    
    print(f"The total number of keys in the JSON file is {total_keys}.")

    # modify_json_file(json_data)

    modify_json_based_on_id(json_data, id=4)
    # modify_json_based_on_id_mt_detr(json_data, id=3)

if __name__ == '__main__':
    main()
