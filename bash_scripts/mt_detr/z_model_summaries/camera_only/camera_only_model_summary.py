======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─CameraOnly (backbone)                                                [1, 3, 480, 652]     [1, 256, 60, 81]     --                   True
│    └─ConvNeXt (model1)                                               [1, 3, 480, 652]     [1, 256, 60, 81]     256                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 60, 81]     [1, 256, 60, 81]     512                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 30, 40]     [1, 512, 30, 40]     1,024                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 15, 20]    [1, 1024, 15, 20]    2,048                True
├─ChannelMapper (neck)                                                 [1, 256, 60, 81]     [1, 256, 60, 81]     --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 256, 60, 81]     [1, 256, 60, 81]     66,048               True
│    │    └─ConvModule (1)                                             [1, 512, 30, 40]     [1, 256, 30, 40]     131,584              True
│    │    └─ConvModule (2)                                             [1, 1024, 15, 20]    [1, 256, 15, 20]     262,656              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 1024, 15, 20]    [1, 256, 8, 10]      2,359,808            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 60, 81]     [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 60, 81]          [1, 256, 60, 81]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 30, 40]          [1, 256, 30, 40]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 15, 20]          [1, 256, 15, 20]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 8, 10]           [1, 256, 8, 10]      --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 60, 81]     [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [6440, 1, 256]       4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 6440, 256]       [1, 6440, 256]       65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 6440, 256]       [1, 6440, 256]       512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 6440, 256]       [1, 6440, 2]         514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 6440, 256]       [1, 6440, 4]         132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─Linear (pos_trans)                                         [1, 300, 512]        [1, 300, 512]        262,656              True
│    │    └─LayerNorm (pos_trans_norm)                                 [1, 300, 512]        [1, 300, 512]        1,024                True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   [6, 300, 1, 256]     6,123,264            True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (0)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   --                   (recursive)          True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (1)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   --                   (recursive)          True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (2)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   --                   (recursive)          True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (3)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   --                   (recursive)          True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (4)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─DeformableDetrTransformer (transformer)                         --                   --                   (recursive)          True
│    │    └─DeformableDetrTransformerDecoder (decoder)                 --                   --                   (recursive)          True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (5)                                             [1, 300, 256]        [1, 300, 4]          132,612              True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (0)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (0)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (1)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (1)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (2)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (2)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (3)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (3)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (4)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (4)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (5)                                                 [1, 300, 256]        [1, 300, 2]          514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (5)                                             [1, 300, 256]        [1, 300, 4]          (recursive)          True
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [300, 2]             [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [300, 4]             --                   --                   --
│    └─L1Loss (loss_bbox)                                              [300, 4]             --                   --                   --
│    └─FocalLoss (loss_cls)                                            [6440, 2]            [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [6440, 4]            --                   --                   --
│    └─L1Loss (loss_bbox)                                              [6440, 4]            --                   --                   --
======================================================================================================================================================
Total params: 113,805,354
Trainable params: 113,805,354
Non-trainable params: 0
Total mult-adds (G): 25.59
======================================================================================================================================================
Input size (MB): 3.76
Forward/backward pass size (MB): 2765.38
Params size (MB): 402.87
Estimated Total Size (MB): 3172.00
======================================================================================================================================================