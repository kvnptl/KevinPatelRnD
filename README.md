# Object Detection in Adverse Weather Conditions using Tightly-coupled Data-driven Multi-modal Sensor Fusion

- Supervisors:
    - Prof. Dr. Ing- Sebastian Houben
    - M.Sc. Santosh Thoduka

## Motivation
- Why multi-modal sensor fusion?

| ![Figure 1: Sensors modality characteristics](https://github.com/kvnptl/KevinPatelRnD/assets/47410011/9e9bdabb-eeb3-4147-b51b-0daf8fe3a92b) | ![Figure 2: Sensors modality characteristics](https://github.com/kvnptl/KevinPatelRnD/assets/47410011/69e7ef29-7288-4132-a007-294ee27e9367) |
|:--:|:--:|
| *Figure 1: Sensors modality characteristics* | *Figure 2: Sensors modality characteristics* |


## Datasets

**Table 3.1: Multimodal adverse weather conditions datasets. Sensors†: C-R-L-N-F denotes Camera, Radar, LiDAR, Near-infrared, and Far-infrared sensors, respectively. Weather conditions‡: F-SN-R-O-SL-N denotes Fog, Snow, Rain, Overcast, Sleet, and Night conditions, respectively. Note that DENSE and nuScenes datasets are used for the project.**
- Sorted in ascending order w.r.t year column
  
| **Name**             | **Sensors†** | **Weather Cond.‡**           | **Size (GB)** | **Year** | **Citation Cnt.** | **Link** | **Publisher**                                         | **Pros**                                          | **Cons**                                              |
|----------------------|-------------|-----------------------------|---------------|----------|-------------------|----------|-------------------------------------------------------|---------------------------------------------------|------------------------------------------------------|
| **DENSE**            | CRLNF       | F, SN, R, N                 | 582           | 2020     | 269               | [Link](https://www.cs.princeton.edu/~fheide/AdverseWeatherFusion/) | Mercedes, Ulm, Princeton                              | - More adverse weather data<br>- Higher resolution data than nuScenes | - Less label frames<br>- Sparse Radar data        |
| **nuScenes**         | CRL         | R, N                        | 400           | 2020     | 3459              | [Link](https://openaccess.thecvf.com/content_CVPR_2020/html/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.html) | Motional                                              | - Well documented<br>- Heavily used              | - Not good for adverse weather conditions<br>- Sparse Radar data |
| **The Oxford RobotCar** | CRL      | R, SN, F                    | 4700          | 2020     | 317               | [Link](https://ieeexplore.ieee.org/abstract/document/9196884?casa_token=2BTLePzGRJUAAAAA:-8e1s7lpxTQvbOC02GFlYATkuaRuuV4c_6f9lLSVov180BuKv_sHcU5rhZ5qXwLt6-GoZwC-0uQ) | Oxford Robotics Institute                             |                                                   |                                                     |
| **EU Long-term**     | CRL         | SN, R, O, N                 |               | 2020     | 72                | [Link](https://arxiv.org/abs/1909.03330) | University of Technology of Belfort-Montbéliard (UTBM) |                                                   |                                                     |
| **RADIATE**          | CRL         | F, SN, R, O, SL, N          |               | 2021     | 132               | [Link](http://pro.hw.ac.uk/radiate/doc/dataset/#sensors) | Heriot-Watt University                                |                                                   |                                                     |
| **K-Radar**          | CRL         | F, R, SN                    | 13000         | 2022     | 15                | [Link](https://proceedings.neurips.cc/paper_files/paper/2022/hash/185fdf627eaae2abab36205dcd19b817-Abstract-Datasets_and_Benchmarks.html) | KAIST University                                      | - Includes 4D radar                                | - Heavy dataset, order via physical drive           |
| **Boreas**           | CRL         | SN, R, O, N                 | 4400          | 2022     | 38                | [Link](https://www.boreas.utias.utoronto.ca/#/) | University of Toronto                                 | - High resolution radar                            |                                                     |
| **aiMotive**         | CRL         | R, O, N                     | 85            | 2023     | 3                 | [Link](https://github.com/aimotive/aimotive_dataset) | aiMotive company                                      | - Fog and Snow not included (future work)<br>- Relatively small dataset |                                                     |

## Methods

**Table 3.4: Multi-modal sensor fusion methods. Sensors†: C-R-L denote Camera, Radar, and LiDAR sensors, respectively**
- SAF-FCOS, HRFuser, and MT-DETR methods are thoroughly analyzed in the report

| Name              | Sensors† | Dataset Used        | Fusion method | 2D/3D | Code Link | Year | Published at | Cited By | Comment 1                                     | Comment 2                                    | Framework  |
|-------------------|---------|---------------------|---------------|-------|-----------|------|--------------|----------|-----------------------------------------------|----------------------------------------------|------------|
| CRF Net           | CR      | nuScenes            | Data-level    | 2D    | [Link](https://github.com/TUMFTM/CameraRadarFusionNet)  | 2019 | SDF          | 208      | Uses BlackIn method for training              | didn't mention NDS                           | Tensorflow |
| SAF-FCOS          | CR      | nuScenes            | Feature-level | 2D    | [Link](https://github.com/Singingkettle/SAF-FCOS)  | 2020 | Sensors      | 105      | New spatial fusion strategy                   | AP = 72.4, didn't mention NDS                | PyTorch    |
| BIRANet           | CR      | nuScenes            | Feature-level | 2D    | [Link](https://github.com/RituYadav92/Radar-RGB-Attentive-Multimodal-Object-Detection)  | 2020 | ICIP         | 36       |                                               |                                               | PyTorch    |
| GRIF Net          | CR      | nuScenes            |               | NA    | NA  | 2020 |              |          |                                               |                                               | NA         |
| SeeingThroughFog  | CRLNF   | DENSE               | Feature-level | 2D    | NA        | 2020 | CVPR         | 236      | Novel entropy based net                       | normal to adverse weather transfer           | NA         |
| YOdar             | CR      | nuScenes            |               | 2D    | NA        | 2020 | ICAART       | 23       |                                               |                                               | NA         |
| CenterFusion      | CR      | nuScenes            | Feature-level | 3D    | [Link](https://github.com/mrnabati/CenterFusion)  | 2021 | WACV         | 170      | data augmentation applied                     | NDS = 44.0                                   | PyTorch    |
| RODNet            | CR      | CRUW                | Feature-level | 2D    | [Link](https://github.com/yizhou-wang/RODNet)  | 2021 | WACV         | 58       | Uses unique Radar data processing             |                 | PyTorch |
| CRAMNet            | CR     | RADIATE             |               | NA    |           | 2022 |              |          |                                               |                                               | NA         |
| Attention Powered- #1 | CR  | nuScenes            |               | NA    | NA  | 2022 |              |          |                                               |                                               | NA         |
| Attention Powered- #2 | CR  | RADIATE             |               | 2D    | NA        | 2022 | CISDS        | 0        | Outperform SAF-FCOS, CenterFusion             |                                               | NA         |
| MT-DETR            | CRL    | DENSE               | Mixed-level   | 2D    | [Link](https://github.com/Chushihyun/MT-DETR)  | 2023 | WACV         | 2        | Attention based method                        |                                               | PyTorch    |
| RTNH               | R      | K-Radar             |               | 3D    | [Link](https://github.com/kaist-avelab/k-radar)  | 2023 | NeurIPS      | 9        | Baseline method uses only radar               | 4D radar dataset with AW                      | PyTorch    |
| HVDetFusion        | CR     | nuScenes            |               | 3D    | [Link](https://github.com/HVXLab/HVDetFusion)  | 2023 |              | 2        | NDS = 67.4, built on top of CenterFusion      |                                               | PyTorch    |
| REDFormer          | CR     | nuScenes            |               | 3D    | [Link](https://github.com/PurdueDigitalTwin/REDFormer)  | 2023 | ITSC         | 0        | NDS = 48.6, multi camera input, BEV based     | how did they define SOTA in low visibility subset? | PyTorch |
| RADIANT            | CR     | nuScenes            | Feature-level | 3D    | [Link](https://github.com/longyunf/radiant)  | 2023 | AAAI         | 2        | didn't mention NDS                            | How come this is SOTA?                        | PyTorch    |
| HRFuser            | CRL    | nuScenes, DENSE     | Mixed-level   | 2D    | [Link](https://github.com/timbroed/HRFuser)  | 2023 | ITSC         | 8        | Mixed Fusion, Transformer based               | didn't mention NDS                            | PyTorch    |
| CamRaDepth         | CR     | nuScenes            |               |       | [Link](https://github.com/TUMFTM/CamRaDepth/tree/main)  | 2023 |              | Not yet published |                                              |                                               | PyTorch    |
| AutoFed            | CRL    | The Oxford RobotCar |               | NA    |           | 2023 |              |          |                                               |                                               | NA         |
| aiMotive           | LR     | aiMotive            |               | 3D    | [Link](https://github.com/aimotive/mm_training)  | 2023 | ICLR         | 2        | Yet to explore for Camera+Radar fusion        |                                               | PyTorch    |


## Figures from the report:

- A few sample figures highlighting the importance of multi-modal sensor fusion

| <img src="https://github.com/kvnptl/KevinPatelRnD/assets/47410011/3af9ac5c-02cc-4fab-b32d-716e98bae338" alt="drawing" width="500"/>|
|:--:| 
| *Figure 3: Van occluded by a water droplet on the lens* |

| <img src="https://github.com/kvnptl/KevinPatelRnD/assets/47410011/e7b8f078-b6ab-4b5d-a499-d26358401c84" alt="drawing" width="600"/>|
|:--:| 
| *Figure 4: LiDAR performance test* |

| <img src="https://github.com/kvnptl/KevinPatelRnD/assets/47410011/e7cd3537-a236-4b1c-baea-47099f0464f3" alt="drawing" width="600"/>|
|:--:| 
| *Figure 5: 1st row: clear weather condition, 2nd row: with fog. Shows that lidar affects by the fog but radar intensity remains the same* |

| <img src="https://github.com/kvnptl/KevinPatelRnD/assets/47410011/c7ada244-cf38-4702-930b-0c4b35dc70be" alt="drawing" width="400"/>|
|:--:| 
| *Figure 6: Highlighting the significance of fusing multimodal sensor data* |

| <img src="https://github.com/kvnptl/KevinPatelRnD/assets/47410011/3429689c-26bd-4a2e-a484-8b4a3e0ed3db" alt="drawing" width="500"/>|
|:--:| 
| *Figure 7: Samples of K-Radar datasets for various weather conditions* |

### Report:

R&D detailed report link (required access): [Link](https://drive.google.com/file/d/1Kw0dCeUCSVvS41pdW04DT21GatEBN1Mc/view?usp=sharing)

### TODOs:
- [ ] Quantitative results
- [ ] Qualitative results
- [x] Methods table
- [x] Dataset used table
- [x] Link to final report

### Contact:
Email 📧: kevinpatel4400@gmail.com

### Citation:
```
@unpublished{RnDPatel,
    abstract = {In the ﬁeld of autonomous vehicles, object detection is a critical component, especially in perceiving the environment under adverse weather conditions. Traditional methods, primar- ily focused on camera data, face signiﬁcant limitations in such scenarios. This research aims to address these challenges through the exploration of multimodal sensor fusion, incor- porating Cameras, LiDAR, and Radar, to improve detection accuracy in inclement weather. The study primarily focuses on a tightly-coupled fusion approach, contrasted against the existing middle fusion strategy, with experiments conducted using the nuScenes and DENSE datasets, the latter featuring extreme weather conditions. The ﬁndings indicate that the integration of complementary sensors substantially enhances detection accuracy across various weather conditions and that the tightly-coupled fusion approach outperforms the middle fusion method. Both qualitative and quantitative analyses support these conclusions, highlighting the eﬀectiveness of this approach in the advancement of object detection technologies in autonomous vehicles. This research provides signiﬁcant insights into the robustness of sensor fusion techniques, oﬀering substantial contributions to the ﬁelds of computer vision and autonomous vehicle technology.},
    title = {Object detection in adverse weather conditions using tightly-coupled data-driven multi-modal sensor fusion},
    author = {Patel, Kevin},
    year = {2023},
    month = {December},
}
```
