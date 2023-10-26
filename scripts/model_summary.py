import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
import torchvision

def main():
    # visualize the network
    # from torchview import draw_graph # To visualize the network graph
    from torchinfo import summary

    IMAGE_SIZE = (224, 224)

    # Create the network
    # Resnet18
    model = torchvision.models.resnet18()

    x = torch.randn((1, 3, IMAGE_SIZE[0], IMAGE_SIZE[1]))

    summary(model=model, 
            input_size=x.shape,
            col_names=["input_size", "output_size", "num_params", "trainable"],
            col_width=20,
            row_settings=["var_names"])

    # # Visualize the network graph
    # model_graph = draw_graph(model, x, 
    #                          expand_nested=True,
    #                          hide_module_functions=False,
    #                          graph_name='fcos_graph_torchview')
    # model_graph.resize_graph(scale=1.0)
    # model_graph.visual_graph.render(format='png')

# def simple_net_viz():
#     import torchlens
#     from torchview import draw_graph

#     class SimpleFeedForward(nn.Module):
#         def __init__(self):
#             super().__init__()
#             self.conv = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, padding=1)
#             self.fc = nn.Linear(in_features=6*16*16, out_features=10)

#         def forward(self, x):
#             x = self.conv(x)
#             x = nn.functional.relu(x)
#             x = nn.functional.max_pool2d(x, 2)
#             x = x.flatten()
#             x = self.fc(x)
#             return x


#     x = torch.rand(1, 3, 32, 32)
#     ff_model = SimpleFeedForward()
    
    # torchlens.log_forward_pass(model=ff_model,
    #                            input_args=x,
    #                            vis_opt='unrolled',
    #                            vis_save_only=True,
    #                            vis_outpath='ff_model',
    #                            vis_fileformat='png',
    #                            vis_direction='topdown')
    # torchlens.log_forward_pass(ff_model, x, vis_opt='rolled')

    # # Visualize the network
    # model_graph = draw_graph(ff_model, x, 
    #                          expand_nested=True,
    #                          hide_module_functions=False,
    #                         #  hide_inner_tensors=False,
    #                          graph_name='ffmodel_graph')
    # model_graph.resize_graph(scale=1.0)
    # model_graph.visual_graph.render(format='png')

if __name__ == "__main__":
    main()
    # simple_net_viz()