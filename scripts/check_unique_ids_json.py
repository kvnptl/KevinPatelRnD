import json

def verify_unique_ids(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract image and annotation IDs
    image_ids = {image['id'] for image in data['images']}
    annotation_ids = {annotation['id'] for annotation in data['annotations']}

    # find any duplicate in annotations
    # Find any duplicate annotation IDs
    duplicate_ids = set()
    seen_ids = set()

    for annotation in data['annotations']:
        if annotation['id'] in seen_ids:
            duplicate_ids.add(annotation['id'])
        else:
            seen_ids.add(annotation['id'])

    if duplicate_ids:
        print("Duplicate annotation IDs found:", duplicate_ids)
    else:
        print("No duplicate annotation IDs found.")

    # Check for duplicates
    if len(image_ids) != len(data['images']):
        print("Duplicate image IDs found.")
        return False
    if len(annotation_ids) != len(data['annotations']):
        print("Duplicate annotation IDs found.")
        return False

    print("All image and annotation IDs are unique.")
    return True

# Example usage
json_file = '/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/nuScenes/nuscenes_infos_val_mono3d_saf_fcos.coco.json'  # Replace with your file path
verify_unique_ids(json_file)
