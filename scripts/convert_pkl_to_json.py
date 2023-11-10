import json
import pickle
import numpy as np

def default_converter(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    elif isinstance(o, np.integer):
        return int(o)
    elif isinstance(o, np.floating):
        return float(o)
    elif isinstance(o, np.bool_):
        return bool(o)
    # Add more conversions here if there are other specific numpy types
    else:
        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')


with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_pkl_files/dense_infos_all.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)

# Convert the data to JSON and write it to a file
with open('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_pkl_files/dense_infos_all.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, default=default_converter)
