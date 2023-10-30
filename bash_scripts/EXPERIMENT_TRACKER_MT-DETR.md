# Method: MT-DETR

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

[Experiment Tracker sheet: https://docs.google.com/spreadsheets/d/1m2jxf0A0iqpwQYJDxDnoZ1-XZ8W_OqSWHnVe_a6aSKY/edit?pli=1#gid=11409550]

Run commands:
- pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.10.0/index.html
- pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

###############################################################################

### Current


- TIMESTAMP: 30-Oct-2023 02:54
    - Training MT-DETR Camera only model - single gpu - batch=1  - [IN-PROGRESS]
    - Training MT-DETR C+L+R model - multi gpu - batch=1 - [IN-PROGRESS]
    - Training MT-DETR C+L+R+T model - multi gpu - batch=1 - [IN-PROGRESS]
    - Training Middle Fusion C+L+R model - multi gpu - batch=1 - [IN-PROGRESS]
    - Training Early Fusion C+L+R model - multi gpu - batch=1 - [IN-PROGRESS]

- TIMESTAMP: 28-Oct-2023 01:23
    - Test on provided weights - [PENDING]
        - camera only with weather - DONE
            - Need to update results in experiment tracker sheet - DONE
        - camera + lidar + radar with weather - [PENDING]
        - camera + lidar + radar + time + weather - [PENDING]
    
    - Train camera only model on multi gpu (default settings) - [PENDING]
        - Either need to fix conda environment
        - Need to fix other bugs


##################################################################################

### Pending

- Divide images into Easy, moderate and Hard categories to match with HRFuser results
- Project Lidar and Radar image on RGB image for visualization
    - For DENSE and nuScenes
- Understand Lidar and Radar Image generation - PENDING
    - Check GitHub issue
- Get model summary with single modality
    - For only camera
    - For camera + lidar (understand how to do this?)
    - For camera + radar

##################################################################################

### DONE

- TIMESTAMP: 28-Oct-2023 01:23
    - [IMPORTANT] FIRST CONVERT LIDAR AND RADAR pointcloud to RGB images - DONE
        - Missing to convert 54 radar files
        - So restarted conversion with `all.txt` instead of separate txt files and creating empty radar image when not found

##################################################################################################

### Bug fixes in mmcv-full 1.3.17

- File: /home/kpatel2s/anaconda3/envs/hrfuser-cuda102-torch110-mmcv-full-1317/lib/python3.8/site-packages/mmcv/utils/config.py
    - Add `import yapf`
    - Add `from .version_utils import digit_version`
    - Repalce `text, _ = FormatCode(text, style_config=yapf_style, verify=True)` with 
        ```
        if digit_version(yapf.__version__) >= digit_version('0.40.2'):
            text, _ = FormatCode(text, style_config=yapf_style)
        else:
            text, _ = FormatCode(text, style_config=yapf_style, verify=True)
        ```