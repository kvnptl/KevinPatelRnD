# import re
# import matplotlib.pyplot as plt

# def parse_log_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     iter_values = []
#     loss_values = []

#     for line in lines:
#         # Find 'iter' and 'loss' using regular expressions
#         iter_match = re.search(r'iter: (\d+)', line)
#         loss_match = re.search(r'loss: (\d+\.\d+)', line)

#         if iter_match and loss_match:
#             iter_value = int(iter_match.group(1))
#             loss_value = float(loss_match.group(1))

#             iter_values.append(iter_value)
#             loss_values.append(loss_value)

#     return iter_values, loss_values

# def plot_loss_vs_iter(iter_values, loss_values):
#     plt.plot(iter_values, loss_values)
#     plt.xlabel('Iteration')
#     plt.ylabel('Loss')
#     plt.grid(True)
#     plt.title('Loss vs Iteration')
#     plt.savefig('saf_fcos_loss_curve.png')

# # Example usage
# file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/bash_scripts/saf_fcos/model_outputs_logs/ver2/LR_0p001/train/loss_logs.txt'  # Replace with your actual file path
# iter_values, loss_values = parse_log_file(file_path)
# plot_loss_vs_iter(iter_values, loss_values)



import re
import matplotlib.pyplot as plt

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    iter_values = []
    loss_values = []

    for line in lines:
        # Find 'iter' and 'loss' using regular expressions
        iter_match = re.search(r'iter: (\d+)', line)
        loss_match = re.search(r'loss: (\d+\.\d+)', line)

        if iter_match and loss_match:
            iter_value = int(iter_match.group(1))
            loss_value = float(loss_match.group(1))

            iter_values.append(iter_value)
            loss_values.append(loss_value)

    return iter_values, loss_values

def convert_iters_to_epochs(iter_values, iterations_per_epoch):
    return [iter_value / iterations_per_epoch for iter_value in iter_values]

def plot_loss_vs_epoch(epoch_values, loss_values):
    plt.plot(epoch_values, loss_values)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.title('Loss vs Epoch')
    plt.savefig('saf_fcos_loss_vs_epoch_curve.png')

# Calculate iterations per epoch (using previously calculated value)
iterations_per_epoch = 4218.125

# Example usage
file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/bash_scripts/saf_fcos/model_outputs_logs/ver2/LR_0p001/train/loss_logs.txt'  # Replace with your actual file path
iter_values, loss_values = parse_log_file(file_path)
epoch_values = convert_iters_to_epochs(iter_values, iterations_per_epoch)
plot_loss_vs_epoch(epoch_values, loss_values)
