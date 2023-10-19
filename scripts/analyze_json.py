import json

def count_keys_in_dict(d):
    count = 0
    for key, value in d.items():
        count += 1  # Counting the current key
        if isinstance(value, dict):
            count += count_keys_in_dict(value)  # Recursively count keys in sub-dictionary
            print(f"key: {key}")
    return count

def main():
    json_file_path = '/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/v1.0-trainval/gt_fcos_coco_val.json'  # Replace with your JSON file path
    
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    
    if not isinstance(json_data, dict):
        print("The JSON file does not contain a dictionary (JSON object) at the top level.")
        return

    total_keys = count_keys_in_dict(json_data)
    
    print(f"The total number of keys in the JSON file is {total_keys}.")

if __name__ == '__main__':
    main()
