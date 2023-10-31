======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─MT_DETR_four (backbone)                                              [1, 12, 512, 612]    [1, 256, 64, 76]     8,421,376            True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model3)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model4)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter3)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter4)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model3)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model4)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 64, 76]     [1, 256, 64, 76]     512                  True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 64, 76]     [1, 256, 64, 76]     512                  True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 64, 76]     [1, 256, 64, 76]     512                  True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter3)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter4)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model3)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model4)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 32, 38]     [1, 512, 32, 38]     1,024                True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 32, 38]     [1, 512, 32, 38]     1,024                True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 32, 38]     [1, 512, 32, 38]     1,024                True
│    └─EnhancementModule (scatter1)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter2)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter3)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─EnhancementModule (scatter4)                                    --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model3)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ConvNeXt (model4)                                               --                   --                   (recursive)          True
│    │    └─ModuleList (downsample_layers)                             --                   --                   (recursive)          True
│    │    └─ModuleList (stages)                                        --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─ModuleList (fusion_layers)                                 --                   --                   (recursive)          True
│    └─ResidualFusionModule (fusion1)                                  --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 16, 19]    [1, 1024, 16, 19]    2,048                True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 16, 19]    [1, 1024, 16, 19]    2,048                True
│    └─ConfidenceFusionModule (fusion2)                                --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 16, 19]    [1, 1024, 16, 19]    2,048                True
├─CBChannelMapper (neck)                                               [1, 256, 64, 76]     [1, 256, 64, 76]     --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 256, 64, 76]     [1, 256, 64, 76]     66,048               True
│    │    └─ConvModule (1)                                             [1, 512, 32, 38]     [1, 256, 32, 38]     131,584              True
│    │    └─ConvModule (2)                                             [1, 1024, 16, 19]    [1, 256, 16, 19]     262,656              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 1024, 16, 19]    [1, 256, 8, 10]      2,359,808            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 64, 76]     [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 64, 76]          [1, 256, 64, 76]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 32, 38]          [1, 256, 32, 38]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 16, 19]          [1, 256, 16, 19]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 8, 10]           [1, 256, 8, 10]      --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 64, 76]     [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [6464, 1, 256]       4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 6464, 256]       [1, 6464, 256]       65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 6464, 256]       [1, 6464, 256]       512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 6464, 256]       [1, 6464, 2]         514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 6464, 256]       [1, 6464, 4]         132,612              True
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
│    └─FocalLoss (loss_cls)                                            [6464, 2]            [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [6464, 4]            --                   --                   --
│    └─L1Loss (loss_bbox)                                              [6464, 4]            --                   --                   --
======================================================================================================================================================
Total params: 394,683,562
Trainable params: 394,683,562
Non-trainable params: 0
Total mult-adds (G): 50.49
======================================================================================================================================================
Input size (MB): 15.04
Forward/backward pass size (MB): 8649.97
Params size (MB): 1492.48
Estimated Total Size (MB): 10157.49
======================================================================================================================================================