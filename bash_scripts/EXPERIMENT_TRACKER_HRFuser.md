# Method: HRFuser

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

[Experiment Tracker sheet: https://docs.google.com/spreadsheets/d/1m2jxf0A0iqpwQYJDxDnoZ1-XZ8W_OqSWHnVe_a6aSKY/edit?pli=1#gid=11409550]

Run commands:
- pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.10.0/index.html
- pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

NOTE: below torch and mmcv versions are for CUDA 11.1 version

Create conda env using `conda create -n hrfuser python=3.8`

```bash
pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10.0/index.html
pip install tensorboard==2.14.0 setuptools==59.5.0
pip install numpy==1.20.0 cython==3.0.4 tqdm numba==0.48.0 nuscenes-devkit==1.1.9
conda install scikit-learn scipy
pip install -v -e .
```
###############################################################################

### Current

- START WRITING REPORT NOW

- [nuscenes] 
    - Train HRFuser with only 7 classes to match with SAF-FCOS - [RUNNING]
        - bicycle, car, motorcycle, bus, train(trailer + construction vehicle), truck
        - If possible train only C+R
- [DENSE]
    - Train with only Camera + Radar - [RUNNING]


##################################################################################

### Pending

- Read the HRFuser paper again
- [Study] model summary


- Plot confusion matrix
- Replace all results with CAR ONLY RESULTS (only required for SAF-FCOS)
- Get model summary with single modality
    - For only camera
    - For camera + lidar (understand how to do this?)
    - For camera + radar

- Check experiment tracker sheet for more TODOs


##################################################################################

### DONE

- TIMESTAMP: 16-Nov-2023 7:55
    - [DENSE]
        - Evaluate on all weather with Day and Night split
            - Evaluate with CLR modalities (8 batch model) - DONE
            - Evaluate with Camera only - DONE
            - Evaluate with CLR modalities (12 batch model) - DONE

- Check Camera only result on HRFuser using config file - DONE
- Understand Lidar and Radar Image generation - DONE
    - Check GitHub issue
- How to get ground truth data? - DONE
- Project Lidar and Radar image on RGB image for visualization - Done
    - For DENSE and nuScenes

- Check how to store best epoch model based on val loss in MMDetection - Not required
- How to generate KITTI style easy, moderate, and hard categories? (debug trough test.py and find out) - Not planned

------------------------------------------------------------------------------------
- TIMESTAMP: 14-Nov-2023 23:55
    - Convert KITTI JSON TO COCO JSON Format - DONE
        - include lidar and radar image in the JSON - DONE
        - Convert all .pkl files to JSON files - DONE
        - Convert all .json files to COCO JSON files - DONE
    - Evaluate HRFuser on full test set in COCO format - DONE
    - [DENSE] Check evaluation on C+L+R modalities - DONE

- TIMESTAMP: 9-Nov-2023 23:55 (started on)
    - Convert final results into COCO style format - DONE
    - Command for running test on modified dataset config for DENSE dataset:
        - `py tools/test.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_settings3.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF_weights/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_latest.pth --eval bbox`

    - To see the result
        - `py tools/test.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_settings3.py /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF_weights/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_latest.pth --eval bbox --work-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/testing_result_metric --show-dir /home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/dense/inference/testing_result_metric`

----------------------------------------------------------------------------
- TIMESTAMP: 14-Nov-2023 15:00
    - Generate groundtruth for HRFuser dataset - DONE
        - Check on work lab pc
    - Convert DENSE KITTI JSON files to COCO JSON files - DONE

---------------------------------------------------------------------------------
- Timestamp: 13-Nov-2023 15:55
    - Generating ground truths for DENSE dataset - DONE
        - Run after MT-DETR is done

-------------------------------------------------------------------------------------
- Timestamp: 12-Nov-2023 15:55
    - [DENSE] Train camera only on TWO CLASSES - On RTX 3090 GPU - DONE
        - With adjusted learning rate
    - [DENSE] Generate ground truth images for DENSE dataset - DONE
        - [Problem] with dataset annotation, some cars are not annotated in 2D ground truth images

--------------------------------------------------------------------------------------
- TIMESTAMP: 11-Nov-2023 5:00
    - [DENSE]
        - Train Tiny HRFuser model on DENSE - orig setting - batch=12 - multi A100 gpu - DONE
            - With orig settings
            - Remeber to copy only car category
            - FAILED DUE TO CUDA VERSION ERROR
            - [NEED TO INSTALL CUDA 11.1] - DONE
            - Training started on A100 GPU - DONE
            - Testing on A100 GPU - DONE
        - Train camera only - DONE
        - [DENSE] Train camera only on TWO CLASSES - On RTX 3090 GPU - DONE
            - With adjusted learning rate
-------------------------------------------------------------------------------------

- TIMESTAMP: 4-Nov-2023 23:12
    - [nuScenes] Train Tiny HRFuser model on nuScenes - batch=12 - gpu=4 - DONE
        - !!! SOMETHING WRONG WITH THE CONFIG FILE !!!!!! [Re-train]
        - It uses 16 batch size and LR rate of batch size 4 !!!!!!!
        - Need to update results in experiment tracker sheet - NOT UPDATING THIS ONE
        - STARTED RE-TRAINING - DONE
            - Evaluation on TEST SET - DONE

--------------------------------------------------------------------------------------

- TIMESTAMP: 2-Nov-2023 5:45
    - [DENSE] Train Tiny HRFuser model on DENSE - batch=2 - gpu=1 - DONE
        - With adjusted learning rate
        - Running test set evaluation - DONE
        - Need to update results in experiment tracker sheet - DONE

---------------------------------------------------------------------------------------

- TIMESTAMP: 31-Oct-2023 05:02
    - [nuScenes] Train Tiny HRFuser model on nuScenes - batch=4 - gpu=1 - STOPPED
        - Couldn't finish in 3 days

--------------------------------------------------------------------------------------

- TIMESTAMP: 29-Oct-2023 17:13
    - [nuScenes] Train Tiny HRFuser model on nuScenes - batch=12 - Slurm Multi Node - gpus=4 - FAILED
        - Failed dur to CUDA memory error
        - Need to reduce batch size
    - [nuScenes] Train Tiny HRFuser model on nuScenes - batch=12 - cores=64 - Slurm Multi Node - gpus=4 - [IN-PROGRESS]
        - Failed dur to CUDA memory error
        - Giving up on this approach now.
    - [nuScenes] Test Tiny HRFuser model on nuScenes with prov**ided weights - samples=64 - DONE
        - Need to udpate results in experiment tracker sheet - DONE
        - NOT achieving same results as mentioned in the paper


--------------------------------------------------------------------------------

- TIMESTAMP: 28-Oct-2023 23:42
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    - [MOST-IMPORTANT] FOUND PROBLEM IN NUSCENES DATASET
        - LIDAR and RADAR samples are only 404
        - Even total samples are only 1692 !!?? [impossible]
        - Only CAM_FRONT images are 40154, then how come lidar and radar samples are low??
        - NEED TO FIX THIS ASAP!!!!
        - [BUG] silly mistake, I didn't convert nuScenes full dataset. I was using mini dataset.
    - nuScenes data conversion started - DONE
        - TOOK HH:MM = 22:19 !! 

- TIMESTAMP: 28-Oct-2023 14:00
    - Train on DENSE with adjusted learning rate - DONE
        - LR change according to Linear Scaling Rule
        - New config stf_4mod_epo_60_batch_8_gpu_4_worker_8_lr_0p0006667
        - Test evaluation - DONE
        - Need to udpate results in experiment tracker sheet - DONE


--------------------------------------------------------------------------------

- TIMESTAMP: 26-Oct-2023 03:16 (it took me straight 8 hours to complete!!!!!!)
    - Understand the model architectue from the code - DONE
        - Total trainable params?
        - Model summary, save it
        - [NOTE] have to use (debug mode) breakpoint in torchinfo code and then make img_metas to 0.0
    - [nuScenes] Training HRFuser [Base] model on nuScenes - epoch 60 - with batch size = 1 - Single GPUs - DONE
        - saving checkpoints after every 5 epochs
        - Need to udpate results in experiment tracker sheet - DONE
        - Run Test set evaluation - DONE

- TIMESTAMP: 26-Oct-2023 19:19
    - Understand the model architectue of BASE model - DONE
    - Understand the model architectue of DENSE TINY model - DONE
        - Total trainable params?
        - Model summary, save it
        - [NOTE] have to use (debug mode) breakpoint in torchinfo.py code (line 227) and then make `img_metas` to 0.0
            - Change `"justMyCode": false` in launch.json file VSCode
            - FILE: `/home/kpatel2s/anaconda3/envs/hrfuser-cuda102-torch110-mmcv-full-1317/lib/python3.8/site-packages/torchinfo/torchinfo.py`

- TIMESTAMP: 26-Oct-2023 22:39
    - [DENSE] Training HRFuser tiny model on DENSE dataset - Try 1 - epoch=60 - batch size = 2 - single GPU - [IN-PROGRESS]
        - After 4 epochs, model AP is 0.0 (WHY????!!)
        - Restarted this script - DONE
        - Running inference - DONE

---------------------------------------------------------------------------

- TIMESTAMP: 25-Oct-2023 18:10:00
    - Train HRFuser model on STF dataset
    - [DENSE] Training HRFuser [tiny] model on DENSE dataset - Try 1 - epoch=60 - batch size = 8 - 4 GPUs - DONE
        - Not achieving same results as mentioned in the paper
        - Need to udpate results in experiment tracker sheet - DONE
        - Run Test set evaluation - DONE
    - [nuScenes] Training HRFuser [Base] model on nuScenes - epoch 60 - with batch size = 4 - 4 GPUs - DONE
        - saving checkpoints after every 5 epochs
        - Need to udpate results in experiment tracker sheet - DONE
        - Run Test set evaluation - DONE

    ####################################################################
        - Raise an issue on GitHub with result details - DONE
            - LINK: https://github.com/timbroed/HRFuser/issues/3
    #####################################################################


------------------------------------------------------------------------------

- TIMESTAMP: 24-Oct-2023 12:33:00

    - [DENSE] Running inference with author's given [TINY] model on DENSE - DONE
        - Log data into experiment tracker sheet - DONE
    - Change checkpoint saving to after every 5 epochs instead of 1 - `/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/configs/_base_/default_runtime.py` - DONE
    - Plot results, loss, acc, etc for nuScenes HRFuser - DONE
        - Write down a code to extract data from JSON or log file to plot curves
        - Can track result in tensorboard


-------------------------------------------------------------------------------

- TIMESTAMP: 23-Oct-2023 20:00:00
    - DENSE dataset conversion script - DONE
    - Inference on HRFuser STF - DONE


-------------------------------------------------------------------------------

- TIMESTAMP: 22-Oct-2023 23:30:00
    - Training HRFuser Tiny model on nuScenes - part 1 - epoch=12 - DONE
        - Logs and results are available at `/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/hrfuser_weights/nuscenes/work_dirs`
    - Training HRFuser [Tiny] model on nuScenes - part 2 - epoch=60 - batch size = 4 - DONE
        - Change `step` according to 60 epochs - DONE
            ```bash
            lr_config = dict(
                            policy='step',
                            warmup='linear',
                            warmup_iters=500,
                            warmup_ratio=0.001,
                            step=[8, 11])
            ```
        - Not getting good results (not even close to what is mentioned in the paper)
    - Training HRFuser [Base] model on nuScenes - Try 1 - epoch 60 - with batch size = 1 - STOPPED
        - Model AP not improving

- TIMESTAMP: 22-Oct-2023 11:30:00
    - Training HRFuser Tiny model on nuScenes - part 2 - epoch=60 - In Progress
        - Change `step` according to 60 epochs - DONE
            ```bash
            lr_config = dict(
                            policy='step',
                            warmup='linear',
                            warmup_iters=500,
                            warmup_ratio=0.001,
                            step=[8, 11])
            ```

- TIMESTAMP: 22-Oct-2023 18:30:00
    - Prepare STF dataset for HRFuser
        - Making a copy of STF dataset - DONE
        - Extract the zip files - Pending
            - All zip files are located at [/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/SeeingThroughFogCompressed]
            - But zip command won't work for files like .z01, .z02, etc.
            - We need `7z x` command
                - Install `7z` locally - Done
            - Extraction running - DONE


-----------------------------------------------------------------------------------------------

- TIMESTAMP: 20-Oct-2023 00:00:00
    - Nuscenes data convertsion - DONE
    - Setup HRFuser environment on cluster - DONE
        - Env setup is kind of done, need to check with training - DONE
        - Tested with NuScenes training (multi-gpu) - DONE

-----------------------------------------------------------------------------------------------

- TIMESTAMP: 21-Oct-2023 22:30:00
    - Check INFERENCE on nuScenes - DONE
        - results are stored in demo folder
    - Evaluation on nuScenes - DONE
        - results are udpated in experiment tracker sheet

-----------------------------------------------------------------------------------------------

- TIMESTAMP: 19-Oct-2023 00:08:00
    - Running checksum on STF dataset - DONE

##################################################################################################

### Bug fixes in mmcv-full 1.3.17

- File: /home/kpatel2s/anaconda3/envs/hrfuser-cuda102-torch110-mmcv-full-1317/lib/python3.8/site-packages/mmcv/utils/config.py
    - Error:
    ```bash
        FormatCode() got an unexpected keyword argument 'verify'
    TypeError: FormatCode() got an unexpected keyword argument 'verify'
        text, _ = FormatCode(text, style_config=yapf_style, verify=True)
    TypeError: FormatCode() got an unexpected keyword argument 'verify'
    ```
    - Add below lines in the file
    ```python
    import yapf
    from .version_utils import digit_version
    ```
    - Repalce `text, _ = FormatCode(text, style_config=yapf_style, verify=True)` with 
        ```python
        if digit_version(yapf.__version__) >= digit_version('0.40.2'):
            text, _ = FormatCode(text, style_config=yapf_style)
        else:
            text, _ = FormatCode(text, style_config=yapf_style, verify=True)
        ```

### How to get model summary

    - Change to `model_summary` branch
    - Run `py tools/train.py configs/hrfuser/cascade_rcnn_hrfuser_t_1x_stf_r1248_4mod_bn.py`
        - [NOTE]
            - Need to change `batch_size` to 1 in config file
            - Run only 1 GPU based config file (with batch normalization one)
