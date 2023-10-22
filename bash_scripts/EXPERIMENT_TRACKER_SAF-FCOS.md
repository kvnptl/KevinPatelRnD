Method: SAF_FCOS

Note:
    - write down last activity on this window
    - put timestamp (date, time in 24h format)

### Current


### Pending

- Add LIDAR image to the Dataloader and check performance
- Check performance with all 10 nuScenes classes

### DONE

- TIMESTAMP: 15-Oct-2023 02:30:00
    1. LR 0.01 Workers 8 - DONE
    2. LR 0.001 Workers 8 - DONE
    3. LR 0.01 Workers 16 - DONE

- TIMESTAMP: 19-Oct-2023 15:00:00
    - Put all 3 models for evaluation jobs | TIMESTAMP: 18-Oct-2023 00:50:00
        - waiting for my turn on cluster, right now in pending state - DONE
    - Fill out experiment tracker sheet for last 3 model runs - DONE
    - Evaluation on TEST SET - DONE
    - Run training on GPU4 with multi-gpu (low priority) - DONE (failed)
        - Failed due to some parallelism issues
    - Run inference on latest model and save video- DONE
    - Generate ground truth images for comparisons - DONE
        - Create video of ground truth images with annotations
