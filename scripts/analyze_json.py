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


def main():
    json_file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/mt_detr/data/coco_annotation/dense_fog_night_modified.json'  # Replace with your JSON file path
    
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    
    if not isinstance(json_data, dict):
        print("The JSON file does not contain a dictionary (JSON object) at the top level.")
        return

    total_keys = count_keys_in_dict(json_data)
    
    print(f"The total number of keys in the JSON file is {total_keys}.")

    modify_json_file(json_data)

if __name__ == '__main__':
    main()
