======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─EarlyFusion (backbone)                                               [1, 6, 768, 778]     [1, 256, 96, 97]     256                  True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   3,840                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   2,762,624            True
│    │    └─ModuleList (stages)                                        --                   --                   84,801,792           True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 96, 97]     [1, 256, 96, 97]     512                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 48, 48]     [1, 512, 48, 48]     1,024                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 24, 24]    [1, 1024, 24, 24]    2,048                True
├─ChannelMapper (neck)                                                 [1, 256, 96, 97]     [1, 256, 96, 97]     --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 256, 96, 97]     [1, 256, 96, 97]     66,048               True
│    │    └─ConvModule (1)                                             [1, 512, 48, 48]     [1, 256, 48, 48]     131,584              True
│    │    └─ConvModule (2)                                             [1, 1024, 24, 24]    [1, 256, 24, 24]     262,656              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 1024, 24, 24]    [1, 256, 12, 12]     2,359,808            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 96, 97]     [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 96, 97]          [1, 256, 96, 97]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 48, 48]          [1, 256, 48, 48]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 24, 24]          [1, 256, 24, 24]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 12, 12]          [1, 256, 12, 12]     --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 96, 97]     [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [12336, 1, 256]      4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 12336, 256]      [1, 12336, 256]      65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 12336, 256]      [1, 12336, 256]      512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 12336, 256]      [1, 12336, 2]        514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 12336, 256]      [1, 12336, 4]        132,612              True
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
│    └─FocalLoss (loss_cls)                                            [12336, 2]           [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [12336, 4]           --                   --                   --
│    └─L1Loss (loss_bbox)                                              [12336, 4]           --                   --                   --
======================================================================================================================================================
Total params: 201,373,610
Trainable params: 201,373,610
Non-trainable params: 0
Total mult-adds (G): 48.99
======================================================================================================================================================
Input size (MB): 14.34
Forward/backward pass size (MB): 6122.30
Params size (MB): 404.56
Estimated Total Size (MB): 6541.19
======================================================================================================================================================