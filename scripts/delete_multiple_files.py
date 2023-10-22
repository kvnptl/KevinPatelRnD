from concurrent.futures import ThreadPoolExecutor
import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Failed to delete {file_path}: {e}")

file_paths = [
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_1.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_2.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_3.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_4.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_5.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_6.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_7.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_8.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_9.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_10.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_11.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_12.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_13.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_14.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_15.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_16.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_17.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_18.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_19.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_20.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_21.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_22.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_23.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_24.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_25.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_26.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_27.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_28.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_29.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_30.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_31.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_32.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_33.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_34.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_35.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_36.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_37.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_38.pth",
"/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs/cascade_rcnn_hrfuser_t_1x_nus_r640_l_r_fusion_epoch_60/epoch_39.pth",
]

print(f"Total files to be deleted: {len(file_paths)}")

# Use a ThreadPool to delete files in parallel
with ThreadPoolExecutor() as executor:
    executor.map(delete_file, file_paths)
