import json
import pickle
import numpy as np
import os
import concurrent.futures
from tqdm import tqdm

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

def convert_pkl_to_json(pkl_file, json_file):
    with open(pkl_file, 'rb') as pkl_file:
        data = pickle.load(pkl_file)

    # Convert the data to JSON and write it to a file
    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4, default=default_converter)

def main():
    
    single_file = False
    
    if single_file:
        pkl_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense/dense_infos_dense_fog_modified.pkl'
        json_file = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense/dense_infos_dense_fog_modified.json'
        
        convert_pkl_to_json(pkl_file, json_file)
    
    else:
        pkl_file_dir = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_pkl_files'
        json_file_dir = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/dense_pkl_files/converted_stf_json_files'

        # Get a list of .pkl files in the directory
        pkl_files = [f for f in os.listdir(pkl_file_dir) if f.endswith('.pkl')]

        # Create a thread pool
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks to the executor
            futures = [executor.submit(convert_pkl_to_json, 
                                       os.path.join(pkl_file_dir, file), 
                                       os.path.join(json_file_dir, file.replace('.pkl', '.json')))
                       for file in pkl_files]

            # Process futures with tqdm for progress tracking
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
                try:
                    future.result()
                except Exception as exc:
                    print(f'File conversion generated an exception: {exc}')

    

if __name__ == '__main__':
    main()