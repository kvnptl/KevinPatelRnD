"""
Analyze only MT_DETR Training JSON file
"""


import json
import os
from collections import defaultdict

JSON_LOG_PATH = '/home/kpatel2s/kpatel2s/a_data_storage_link/kpatel2s_datasets/mt_detr/work_dirs/mt_detr_c+l_single_gpu_2023-11-02_23-48-06/20231102_234811.log.json'

def extract_from_config(config_str):
    import re

    # Find samples_per_gpu
    match = re.search(r'samples_per_gpu\s*=\s*(\d+)', config_str)
    samples_per_gpu = int(match.group(1)) if match else None

    # Find workers_per_gpu
    match = re.search(r'workers_per_gpu\s*=\s*(\d+)', config_str)
    workers_per_gpu = int(match.group(1)) if match else None

    # Extract the value of "lr"
    lr_match = re.search(r'lr\s*=\s*([\d.]+)', config_str)
    if lr_match:
        lr_value = float(lr_match.group(1))
        print(f"lr: {lr_value}")

    # Extract the value of "max_epochs"
    max_epochs_match = re.search(r'max_epochs\s*=\s*(\d+)', config_str)
    if max_epochs_match:
        max_epochs_value = int(max_epochs_match.group(1))
        print(f"max_epochs: {max_epochs_value}")

    # put these values in a dictionary
    config = {
        'lr': lr_value,
        'samples_per_gpu': samples_per_gpu,
        'max_epochs': max_epochs_value,
        'workers_per_gpu': workers_per_gpu
    }

    return config

def load_json_logs(json_logs):
    log_dicts = [dict() for _ in json_logs]
    config = None
    for json_log, log_dict in zip(json_logs, log_dicts):
        with open(json_log, 'r') as log_file:
            for line in log_file:
                log = json.loads(line.strip())
                # Extract `config`
                if config is None:
                    config = log['config']
                # skip lines without `epoch` field
                if 'epoch' not in log:
                    continue
                epoch = log.pop('epoch')
                if epoch not in log_dict:
                    log_dict[epoch] = defaultdict(list)
                for k, v in log.items():
                    log_dict[epoch][k].append(v)
    
    extracted_config = extract_from_config(config)

    # Initialize variables for tasks
    best_bbox_mAP = -1
    best_epoch = -1
    last_train_iter_loss_details = None
    bbox_mAP_copypaste = None

    # Loop through all epochs
    for epoch, metrics in log_dict.items():
        # Check for validation mode and bbox_mAP
        if 'mode' in metrics and 'val' in metrics['mode']:
            val_bbox_mAP = metrics.get('bbox_mAP', [None])[-1]
            if val_bbox_mAP is not None and val_bbox_mAP >= best_bbox_mAP:
                best_bbox_mAP = val_bbox_mAP
                best_epoch = epoch
                bbox_mAP_copypaste = metrics.get('bbox_mAP_copypaste', [None])
        
        # Check for training mode in the same best_epoch
        if 'mode' in metrics and 'train' in metrics['mode'] and epoch == best_epoch:
            if metrics.get('loss_cls', [None])[-1]:
                last_train_iter_loss_details = {
                    'loss_cls': metrics.get('loss_cls', [None])[-1],
                    'loss_bbox': metrics.get('loss_bbox', [None])[-1],
                    'loss_iou': metrics.get('loss_iou', [None])[-1],
                    'loss': metrics.get('loss', [None])[-1]
                }
                mt_detr_fusion_flag = False
            elif metrics.get('loss_cls1', [None])[-1]:
                last_train_iter_loss_details = {
                    'loss_cls1': metrics.get('loss_cls1', [None])[-1],
                    'loss_bbox1': metrics.get('loss_bbox1', [None])[-1],
                    'loss_iou1': metrics.get('loss_iou1', [None])[-1],
                    'loss': metrics.get('loss', [None])[-1]
                }
                mt_detr_fusion_flag = True
            else:
                exit("[ERROR] !!!No loss_cls or loss_cls1 found in metrics")

    # Output the results
    # if extracted_config:
    #     print(f"Extracted config: {extracted_config}")
    # print(f"Best bbox_mAP: {best_bbox_mAP} at epoch: {best_epoch}")
    # if bbox_mAP_copypaste:
    #     print(f"bbox_mAP_copypaste: {bbox_mAP_copypaste}")
    # if last_train_iter_loss_details:
    #     keys_order = ['loss', 'loss_cls', 'loss_bbox', 'loss_iou']
    #     keys = ', '.join([f"'{k}'" for k in keys_order])
    #     values = ', '.join([f"{last_train_iter_loss_details[k]}" for k in keys_order])
        # print(f"Last training iteration losses in the same epoch: {{{keys}: {values}}}")

    # Output the results and prepare the dictionary to append
    append_dict = {}
    if extracted_config:
        # print(f"Extracted config: {extracted_config}")
        append_dict["Extracted_config"] = extracted_config

    # print(f"Best bbox_mAP: {best_bbox_mAP} at epoch: {best_epoch}")
    append_dict["Best_bbox_mAP"] = best_bbox_mAP
    append_dict["Best_epoch"] = best_epoch

    if bbox_mAP_copypaste:
        bbox_mAP_copypaste = ' '.join(bbox_mAP_copypaste)
        bbox_mAP_copypaste = [round(float(i)*100, 2) for i in bbox_mAP_copypaste.split(" ")]
        print(f"bbox_mAP_copypaste: {bbox_mAP_copypaste}")
        append_dict["bbox_mAP_copypaste"] = bbox_mAP_copypaste

    if last_train_iter_loss_details:
        if mt_detr_fusion_flag:
            keys_order = ['loss', 'loss_cls1', 'loss_bbox1', 'loss_iou1']
        else:
            keys_order = ['loss', 'loss_cls', 'loss_bbox', 'loss_iou']
        keys = ', '.join([f"'{k}'" for k in keys_order])
        values = ', '.join([f"{last_train_iter_loss_details[k]}" for k in keys_order])
        last_train_iter_loss_details_str = f"{{{keys}: {values}}}"
        print(f"Last training iteration losses in the same epoch: {last_train_iter_loss_details_str}")
        append_dict["Last_train_iter_loss_details"] = last_train_iter_loss_details_str

    # Append the results to the JSON file
    with open(JSON_LOG_PATH, 'a') as f:
        f.write("\n")
        json.dump(append_dict, f)


# check if JSON_LOG_PATH exists and it's json
if not os.path.exists(JSON_LOG_PATH) or not JSON_LOG_PATH.endswith('.json'):
    raise ValueError(f'{JSON_LOG_PATH} does not exist or is not a json file')

# Provide your json_logs as a list
json_logs = [JSON_LOG_PATH]
load_json_logs(json_logs)
