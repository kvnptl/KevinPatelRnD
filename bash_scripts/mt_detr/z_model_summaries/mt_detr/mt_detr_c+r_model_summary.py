======================================================================================================================================================
Layer (type (var_name))                                                Input Shape          Output Shape         Param #              Trainable
======================================================================================================================================================
DeformableDETR (DeformableDETR)                                        --                   --                   --                   True
├─MT_DETR_two (backbone)                                               [1, 6, 608, 731]     [1, 256, 76, 91]     4,205,312            True
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
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 76, 91]     [1, 256, 76, 91]     512                  True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 76, 91]     [1, 256, 76, 91]     512                  True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm1)                                          [1, 256, 76, 91]     [1, 256, 76, 91]     512                  True
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
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 38, 45]     [1, 512, 38, 45]     1,024                True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 38, 45]     [1, 512, 38, 45]     1,024                True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm2)                                          [1, 512, 38, 45]     [1, 512, 38, 45]     1,024                True
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
│    └─ConvNeXt (model2)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 19, 22]    [1, 1024, 19, 22]    2,048                True
│    └─ConvNeXt (model1)                                               --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 19, 22]    [1, 1024, 19, 22]    2,048                True
│    └─ConfidenceFusionModule (fusion)                                 --                   --                   (recursive)          True
│    │    └─LayerNorm (norm3)                                          [1, 1024, 19, 22]    [1, 1024, 19, 22]    2,048                True
├─CBChannelMapper (neck)                                               [1, 256, 76, 91]     [1, 256, 76, 91]     --                   True
│    └─ModuleList (convs)                                              --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 256, 76, 91]     [1, 256, 76, 91]     66,048               True
│    │    └─ConvModule (1)                                             [1, 512, 38, 45]     [1, 256, 38, 45]     131,584              True
│    │    └─ConvModule (2)                                             [1, 1024, 19, 22]    [1, 256, 19, 22]     262,656              True
│    └─ModuleList (extra_convs)                                        --                   --                   --                   True
│    │    └─ConvModule (0)                                             [1, 1024, 19, 22]    [1, 256, 10, 11]     2,359,808            True
├─DeformableDETRHead (bbox_head)                                       [1, 256, 76, 91]     [6, 1, 300, 2]       --                   True
│    └─SinePositionalEncoding (positional_encoding)                    [1, 76, 91]          [1, 256, 76, 91]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 38, 45]          [1, 256, 38, 45]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 19, 22]          [1, 256, 19, 22]     --                   --
│    └─SinePositionalEncoding (positional_encoding)                    [1, 10, 11]          [1, 256, 10, 11]     --                   --
│    └─DeformableDetrTransformer (transformer)                         [1, 256, 76, 91]     [6, 300, 1, 256]     6,387,968            True
│    │    └─DetrTransformerEncoder (encoder)                           --                   [9154, 1, 256]       4,541,184            True
│    │    └─Linear (enc_output)                                        [1, 9154, 256]       [1, 9154, 256]       65,792               True
│    │    └─LayerNorm (enc_output_norm)                                [1, 9154, 256]       [1, 9154, 256]       512                  True
│    └─ModuleList (cls_branches)                                       --                   --                   (recursive)          True
│    │    └─Linear (6)                                                 [1, 9154, 256]       [1, 9154, 2]         514                  True
│    └─ModuleList (reg_branches)                                       --                   --                   (recursive)          True
│    │    └─Sequential (6)                                             [1, 9154, 256]       [1, 9154, 4]         132,612              True
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
│    └─FocalLoss (loss_cls)                                            [9154, 2]            [1]                  --                   --
│    └─GIoULoss (loss_iou)                                             [9154, 4]            --                   --                   --
│    └─L1Loss (loss_bbox)                                              [9154, 4]            --                   --                   --
======================================================================================================================================================
Total params: 209,762,090
Trainable params: 209,762,090
Non-trainable params: 0
Total mult-adds (G): 49.91
======================================================================================================================================================
Input size (MB): 10.67
Forward/backward pass size (MB): 6829.60
Params size (MB): 769.80
Estimated Total Size (MB): 7610.07
======================================================================================================================================================