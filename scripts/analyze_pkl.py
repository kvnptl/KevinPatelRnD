import pickle

# Replace 'your_file.pkl' with the path to your .pkl file
with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense/dense_infos_all.pkl', 'rb') as file:
    data = pickle.load(file)

# # remove some dict
# modified_data = data[:5]

# # Write the modified data back to the file
# with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense/dense_infos_dense_fog_modified.pkl', 'wb') as file:
#     pickle.dump(modified_data, file)

pass

# Pick the same ids as MT-DETR

data_modified = []
# extract same image is in pkl file as mt-detr
for d in data:
    if d['image']['image_idx'] == '2018-02-07_18-39-52_00300' or d['image']['image_idx'] == '2018-12-12_15-21-22_00300' or d['image']['image_idx'] == '2018-12-12_15-21-22_02700' or d['image']['image_idx'] == '2018-12-12_15-18-40_00400' or d['image']['image_idx'] == '2018-12-14_15-27-11_04300':
        # save the d and store to create a new pkl
        data_modified.append(d)
        print(f"found {d['image']['image_idx']}")

# Write the modified data back to the file
with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense/dense_infos_modified.pkl', 'wb') as file:
    pickle.dump(data_modified, file)

# MT-DETR image ids
# [{"id": 0, "file_name": "2018-02-07_18-39-52_00300.png", "height": 1024, "width": 1920}, {"id": 1, "file_name": "2018-12-12_15-21-22_00300.png", "height": 1024, "width": 1920}, {"id": 2, "file_name": "2018-12-12_15-21-22_02700.png", "height": 1024, "width": 1920}, {"id": 3, "file_name": "2018-12-12_15-18-40_00400.png", "height": 1024, "width": 1920}, {"id": 4, "file_name": "2018-12-14_15-27-11_04300.png", "height": 1024, "width": 1920}]