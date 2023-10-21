# Method: HRFuser

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

Run commands:
- pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.10.0/index.html
- pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html


### Current

- TIMESTAMP: 21-Oct-2023 23:00:00
    - Training HRFuser Tiny model on nuScenes - part 1 - epoch=12 - DONE
        - Logs and results are available at `/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/work_dirs`
    - Training HRFuser Tiny model on nuScenes - part 2 - epoch=60 - In Progress


### Pending


- TIMESTAMP: 21-Oct-2023 01:37:00
    - Prepare STF dataset for HRFuser
        - Making a copy of STF dataset - DONE
        - Extract the zip files - Pending
            - All zip files are located at [/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/datasets/STF/SeeingThroughFogCompressed]
            - But zip command won't work for files like .z01, .z02, etc.
            - We need `7z x` command
                - Install `7z` locally - Pending
    - Setup HRFuser environment on cluster
        - Env setup is kind of done, need to check with training - Work in progress





- Understand Lidar and Radar Image generation - PENDING
    - Check GitHub issue
- Inference on HRFuser
- Train HRFuser model on STF dataset




### DONE

- TIMESTAMP: 19-Oct-2023 00:08:00
    - Running checksum on STF dataset - DONE

- TIMESTAMP: 20-Oct-2023 00:00:00
    - Nuscenes data convertsion - DONE

- TIMESTAMP: 21-Oct-2023 22:30:00
    - Check INFERENCE on nuScenes - DONE
        - results are stored in demo folder
    - Evaluation on nuScenes - DONE
        - results are udpated in experiment tracker sheet


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