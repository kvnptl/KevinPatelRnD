======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─MiddleFusion_three (backbone)                                        [1, 9, 768, 1032]    [1, 768, 96, 129]    --                   True
│    └─ConvNeXt (model1)                                               [1, 3, 768, 1032]    [1, 256, 96, 129]    256                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 96, 129]    [1, 256, 96, 129]    512                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 48, 64]     [1, 512, 48, 64]     1,024                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 24, 32]    [1, 1024, 24, 32]    2,048                True
│    └─ConvNeXt (model2)                                               [1, 3, 768, 1032]    [1, 256, 96, 129]    256                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 96, 129]    [1, 256, 96, 129]    512                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 48, 64]     [1, 512, 48, 64]     1,024                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 24, 32]    [1, 1024, 24, 32]    2,048                True
│    └─ConvNeXt (model3)                                               [1, 3, 768, 1032]    [1, 256, 96, 129]    256                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 96, 129]    [1, 256, 96, 129]    512                  True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 48, 64]     [1, 512, 48, 64]     1,024                True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 24, 32]    [1, 1024, 24, 32]    2,048                True
├─ChannelMapper (neck)                                                 [1, 768, 96, 129]    [1, 256, 96, 129]    --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 768, 96, 129]    [1, 256, 96, 129]    197,120              True
│    │    └─ConvModule (1)                                             [1, 1536, 48, 64]    [1, 256, 48, 64]     393,728              True
│    │    └─ConvModule (2)                                             [1, 3072, 24, 32]    [1, 256, 24, 32]     786,944              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 3072, 24, 32]    [1, 256, 12, 16]     7,078,400            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 96, 129]    [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 96, 129]         [1, 256, 96, 129]    --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 48, 64]          [1, 256, 48, 64]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 24, 32]          [1, 256, 24, 32]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 12, 16]          [1, 256, 12, 16]     --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 96, 129]    [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [16416, 1, 256]      4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 16416, 256]      [1, 16416, 256]      65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 16416, 256]      [1, 16416, 256]      512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 16416, 256]      [1, 16416, 2]        514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 16416, 256]      [1, 16416, 4]        132,612              True
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
│    └─FocalLoss (loss_cls)                                            [16416, 2]           [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [16416, 4]           --                   --                   --
│    └─L1Loss (loss_bbox)                                              [16416, 4]           --                   --                   --
======================================================================================================================================================
Total params: 294,577,962
Trainable params: 294,577,962
Non-trainable params: 0
Total mult-adds (G): 85.16
======================================================================================================================================================
Input size (MB): 28.53
Forward/backward pass size (MB): 15738.49
Params size (MB): 1125.81
Estimated Total Size (MB): 16892.84
======================================================================================================================================================
