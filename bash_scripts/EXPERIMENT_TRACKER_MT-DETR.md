# Method: MT-DETR

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

[Experiment Tracker sheet: https://docs.google.com/spreadsheets/d/1m2jxf0A0iqpwQYJDxDnoZ1-XZ8W_OqSWHnVe_a6aSKY/edit?pli=1#gid=11409550]

# Setup

Run commands:
```bash
pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.10.0/index.html
pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install tensorboard==2.14.0 setuptools==59.5.0
pip install numpy==1.20.0 cython==3.0.4 tqdm
conda install scikit-learn scipy
pip install -v -e .
```

NOTE: For A100 GPU, use `pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html` and `pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10.0/index.html`

### Step 2:

- Add MT_DETR as a submodule `git submodule add git@github.com:kvnptl/MT-DETR.git mt_detr_cuda11p1`
- Create symbolic links for dataset and checkpoints
- Create dataset for time modality `cd data` and `python create_time_data.py`

###############################################################################

### Current

- TIMESTAMP: 2-Nov-2023 5:24
    - Try train once on Work Lab PC
        - Testing on camera only works - DONE
        - Try training camera only model - DONE
        - Try Middle Fusion C+L+R model - [PENDING]


- TIMESTAMP: 1-Nov-2023 21:40
    - [Middle]
        - Train MT-DETR C+L+R model - single A100 gpu - batch=1 - [RUNNING]
        - Train MT-DETR C+R model - single A100 gpu - batch=1 - DONE
            - Need to update results in experiment tracker sheet - DONE
            - Running evaluation on TEST SET - [RUNNING]

    - [MT-DETR]
        - Train MT-DETR C+L+R model - single A100 gpu - batch=1 - [QUEUED]
        - Train MT-DETR C+L+R+T model - single A100 gpu - batch=1 - [QUEUED]
        - Train MT-DETR C+R model - single A100 gpu - batch=1 - [RUNNING]
            - [NOTE] this model is working on WORK LAB PC
            - check progress tmux `tmt-detr-2`
        - Train MT-DETR C+L model - single A100 gpu - batch=1 - [RUNNING]
            - [NOTE] this model is working on WORK LAB PC
            - check progress tmux `tmt-detr-1`

    - [Early]
        - Train Early Fusion C+R model - single gpu - batch=1 - DONE
        - Evaluation pending - [RUNNING]

##################################################################################

### Pending

- On early fusion C+R, try to reduce input image size and compare compute and memory usage
- How to generate KITTI style easy, moderate, and hard categories? (take reference from HRFuser)
- Read the MT-DETR paper again
- HOW TO GET groundtruth data?
- [Learn] from MMDetection on how to print all AP and AR metrics while training on validation set
- Divide images into Easy, moderate and Hard categories to match with HRFuser results
- Check experiment tracker sheet for more TODOs
- [Study] model summary all basic camera only, early fusion, middle fusion, C+L+R fusion

##################################################################################

### DONE


- TIMESTAMP: 2-Nov-2023 01:23
    - Test on provided weights - DONE
        - camera only with weather - DONE
            - Need to update results in experiment tracker sheet - DONE
        - camera + lidar + radar with weather - DONE
            - [ERROR] with config file, need to fix - DONE
        - camera + lidar + radar + time + weather - DONE
            - Need to update results in experiment tracker sheet - DONE


---------------------------------------------------------------------------------------

- TIMESTAMP: 31-Oct-2023 05:19
    - Get model summary with single modality
        - For only camera - DONE
        - For camera + lidar - DONE
        - For camera + radar - DONE
        - Check there are total 9 model summaries - DONE
    - Training Middle Fusion C+L+R model - single gpu - batch=1 - [Failed]
        - CUDA memory error on V100
    - Training Middle Fusion C+L+R model - multi gpu - batch=1 - [Failed]
        - CUDA memory error on V100
    - Training MT-DETR C+L+R model - multi gpu - batch=1 - [Failed]
    - Training MT-DETR C+L+R+T model - multi gpu - batch=1 - [Failed]


--------------------------------------------------------------------------------------------

- TIMESTAMP: 30-Oct-2023 22:23
    - Training MT-DETR Camera only model - single gpu - batch=1  - DONE
        - Need to update results in experiment tracker sheet - DONE
        - Running evaluation on TEST SET - DONE
            - Need to update results in experiment tracker sheet - DONE

    - Training Early Fusion C+L+R model - single gpu - batch=1 - DONE
        - Running evaluation on TEST SET - DONE
        - Need to update results in experiment tracker sheet - DONE

-----------------------------------------------------------------------------------------------------------------------

- TIMESTAMP: 29-Oct-2023 01:23
    - Train camera only model on multi gpu (default settings)
        - Either need to fix conda environment - DONE
            - Reinstall without apex installation - DONE


-----------------------------------------------------------------------------------------------------------------------

- TIMESTAMP: 28-Oct-2023 01:23
    - [IMPORTANT] FIRST CONVERT LIDAR AND RADAR pointcloud to RGB images - DONE
        - Missing to convert 54 radar files
        - So restarted conversion with `all.txt` instead of separate txt files and creating empty radar image when not found
    - Project Lidar and Radar image on RGB image for visualization - DONE
        - For DENSE
    - Understand Lidar and Radar Image generation - DONE

##################################################################################################

### Bug fixes in mmcv-full 1.3.17

- File: `/home/kpatel2s/anaconda3/envs/hrfuser-cuda102-torch110-mmcv-full-1317/lib/python3.8/site-packages/mmcv/utils/config.py`
    - Add `import yapf`
    - Add `from .version_utils import digit_version`
    - Repalce `text, _ = FormatCode(text, style_config=yapf_style, verify=True)` with 
        ```
        if digit_version(yapf.__version__) >= digit_version('0.40.2'):
            text, _ = FormatCode(text, style_config=yapf_style)
        else:
            text, _ = FormatCode(text, style_config=yapf_style, verify=True)
        ```