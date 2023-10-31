======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─MT_DETR_two (backbone)                                               [1, 6, 825, 608]     [1, 256, 103, 76]    4,208,896            True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 103, 76]    [1, 256, 103, 76]    512                  True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 103, 76]    [1, 256, 103, 76]    512                  True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 51, 38]     [1, 512, 51, 38]     1,024                True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 51, 38]     [1, 512, 51, 38]     1,024                True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 25, 19]    [1, 1024, 25, 19]    2,048                True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 25, 19]    [1, 1024, 25, 19]    2,048                True
├─CBChannelMapper (neck)                                               [1, 256, 103, 76]    [1, 256, 103, 76]    --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 256, 103, 76]    [1, 256, 103, 76]    66,048               True
│    │    └─ConvModule (1)                                             [1, 512, 51, 38]     [1, 256, 51, 38]     131,584              True
│    │    └─ConvModule (2)                                             [1, 1024, 25, 19]    [1, 256, 25, 19]     262,656              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 1024, 25, 19]    [1, 256, 13, 10]     2,359,808            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 103, 76]    [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 103, 76]         [1, 256, 103, 76]    --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 51, 38]          [1, 256, 51, 38]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 25, 19]          [1, 256, 25, 19]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 13, 10]          [1, 256, 13, 10]     --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 103, 76]    [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [10371, 1, 256]      4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 10371, 256]      [1, 10371, 256]      65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 10371, 256]      [1, 10371, 256]      512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 10371, 256]      [1, 10371, 2]        514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 10371, 256]      [1, 10371, 4]        132,612              True
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
│    └─FocalLoss (loss_cls)                                            [10371, 2]           [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [10371, 4]           --                   --                   --
│    └─L1Loss (loss_bbox)                                              [10371, 4]           --                   --                   --
======================================================================================================================================================
Total params: 209,762,090
Trainable params: 209,762,090
Non-trainable params: 0
Total mult-adds (G): 56.41
======================================================================================================================================================
Input size (MB): 12.04
Forward/backward pass size (MB): 7701.29
Params size (MB): 769.79
Estimated Total Size (MB): 8483.12
======================================================================================================================================================
