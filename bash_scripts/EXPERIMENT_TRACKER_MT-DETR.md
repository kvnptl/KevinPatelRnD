# Method: MT-DETR

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

[Experiment Tracker sheet: https://docs.google.com/spreadsheets/d/1m2jxf0A0iqpwQYJDxDnoZ1-XZ8W_OqSWHnVe_a6aSKY/edit?pli=1#gid=11409550]

# Setup

Run commands:

Create conda env using `conda create -n mt_detr python=3.8`

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

- START WRITING REPORT NOW

- Training with 10 percentage of adverse weather(light fog, dense fog, snow) data - DONE
    - Dataset split
        - 10 perc training, 5 perc for validation
        - Taking 10 perc from all 3 seasons with day and night separately
    - Early C+L+R - DONE
        - SOMETHING WRONG, got AP 0.0
            - Maybe because of increased batch size 8 and LR 0.0004
            - Retrain with original setting 0 - DONE
    - Middle C+L+R - DONE
    - Tightly-coupled C+L+R - DONE

- Training with 50 percentage of adverse weather(light fog, dense fog, snow) data - DONE
    - Dataset split
        - 50 perc training, 5 perc for validation
        - Taking 50 perc from all 3 seasons with day and night separately
    - Early C+L+R - DONE
    - Middle C+L+R - DONE
    - Tightly-coupled C+L+R - DONE
        - Evaluation - [IN-PROGRESS]
    - [NOTE] SOMETHING IS WRONG WITH THIS, 
        - NEED TO DEBUG THIS
        - MORE DATA SHOULD GIVE -> GOOD RESULT BUT NOT THIS BAD

##################################################################################

### Pending

- On early fusion C+R, try to reduce input image size and compare compute and memory usage
- Read the MT-DETR paper again
- [Study] model summary all basic camera only, early fusion, middle fusion, C+L+R fusion

- Check experiment tracker sheet for more TODOs


##################################################################################

### DONE

- TIMESTAMP: 16-Nov-2023 7:12


- Recalculate all model summaries with a large depth value - DONE
    - As depth value matters for total multi-adds calculations
    - Once done add a column in exp-tracker for total multi-adds
- HOW TO GET groundtruth data? - DONE

- Divide images into Easy, moderate and Hard categories to match with HRFuser results - Not required
- Evaluate only on Car class - Not required
- How to generate KITTI style easy, moderate, and hard categories? (take reference from HRFuser) - Not planned
- [Learn] from MMDetection on how to print all AP and AR metrics while training on validation set - Not required

------------------------------------------------------------------------------------

    - Generating ground truth for MT-DETR - DONE

- Debugging COCO style annotations
    - `python tools/test.py configs/mt_detr/mt_detr_c+l+r.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/provided/mt_detr_c+l+r.pth --eval bbox --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/testing_result_metric --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/testing_result_metric`

------------------------------------------------------------------------------------
- TIMESTAMP: 7-Nov-2023 23:12
    - [MT-DETR]
        - Train MT-DETR C+R model - single A100 gpu - batch=1 - DONE
            - [NOTE] this model is working on WORK LAB PC
            - check progress tmux `tmt-detr-2`
            - CUDA Error on 3090 GPU
            - Need to train on A100 only - DONE
                - Running evaluation on TEST SET - DONE

-------------------------------------------------------------------------------------
- TIMESTAMP: 4-Nov-2023 23:12
    - [MT-DETR]
        - Train MT-DETR C+L+R model - single A100 gpu - batch=1 - DONE
        - Train MT-DETR C+L model - single A100 gpu - batch=1 - DONE
            - [NOTE] this model is working on WORK LAB PC
            - check progress tmux `tmt-detr-1`
            - Running evaluation on TEST SET - DONE
        - Train MT-DETR C+L+R+T model - single A100 gpu - batch=1 - DONE
            - Running evaluation on TEST SET - DONE
    - [Middle]
        - Train MT-DETR C+L+R model - single A100 gpu - batch=1 - DONE
            - Running evaluation on TEST SET - DONE

----------------------------------------------------------------------------
- TIMESTAMP: 3-Nov-2023 20:23
    - [Early]
        - Train Early Fusion C+R model - single gpu - batch=1 - DONE
        - Evaluation pending - DONE
    - [Middle]
        - Train MT-DETR C+R model - single A100 gpu - batch=1 - DONE
            - Need to update results in experiment tracker sheet - DONE
            - Running evaluation on TEST SET - DONE

---------------------------------------------------------------------------------------
- TIMESTAMP: 2-Nov-2023 01:23
    - Test on provided weights - DONE
        - camera only with weather - DONE
            - Need to update results in experiment tracker sheet - DONE
        - camera + lidar + radar with weather - DONE
            - [ERROR] with config file, need to fix - DONE
        - camera + lidar + radar + time + weather - DONE
            - Need to update results in experiment tracker sheet - DONE

    - Try train once on Work Lab PC
        - Testing on camera only works - DONE
        - Try training camera only model - DONE
        - Try Middle Fusion C+L+R model - DONE

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