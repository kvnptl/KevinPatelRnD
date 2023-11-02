# Method: HRFuser

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

[Experiment Tracker sheet: https://docs.google.com/spreadsheets/d/1m2jxf0A0iqpwQYJDxDnoZ1-XZ8W_OqSWHnVe_a6aSKY/edit?pli=1#gid=11409550]

Run commands:
- pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.10.0/index.html
- pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

###############################################################################

### Current

- TIMESTAMP: 1-Nov-2023 21:45
    - [DENSE]
        - Train Tiny HRFuser model on DENSE - orig setting - batch=12 - multi A100 gpu - [IN-PROGRESS]
            - With orig settings
            - Remeber to copy only car category

    - [nuScenes] Train Tiny HRFuser model on nuScenes - batch=12 - gpu=4 - [IN-PROGRESS]
        - !!! SOMETHING WRONG WITH THE CONFIG FILE !!!!!! [Re-train]
        - It uses 16 batch size and LR rate of batch size 4 !!!!!!!
        - Need to update results in experiment tracker sheet - NOT UPDATING THIS ONE
        - STARTED RE-TRAINING [IN-PROGRESS]


##################################################################################

### Pending

- Replace all results with CAR ONLY RESULTS
- How to generate KITTI style easy, moderate, and hard categories? (debug trough test.py and find out)
- Read the HRFuser paper again
- How to get ground truth data?
- Check how to store best epoch model based on val loss in MMDetection
- Project Lidar and Radar image on RGB image for visualization
    - For DENSE and nuScenes
- Understand Lidar and Radar Image generation - PENDING
    - Check GitHub issue
- [Study] model summary
- Get model summary with single modality
    - For only camera
    - For camera + lidar (understand how to do this?)
    - For camera + radar
- Check experiment tracker sheet for more TODOs
##################################################################################

### DONE

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
    - Add `import yapf`
    - Add `from .version_utils import digit_version`
    - Repalce `text, _ = FormatCode(text, style_config=yapf_style, verify=True)` with 
        ```
        if digit_version(yapf.__version__) >= digit_version('0.40.2'):
            text, _ = FormatCode(text, style_config=yapf_style)
        else:
            text, _ = FormatCode(text, style_config=yapf_style, verify=True)
        ```