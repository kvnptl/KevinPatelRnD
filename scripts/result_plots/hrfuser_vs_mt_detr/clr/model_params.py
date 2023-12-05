import matplotlib.pyplot as plt
import numpy as np

root_path = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/hrfuser_vs_mt_detr/clr/"

# File path to the data file
data_file_path = root_path + 'model_complexity.txt'


# Function to read data from the file
def read_data_from_file_v4(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract categories (skipping the 'Modalities' column)
    categories = lines[0].strip().split('\t')[1:]
    data = {line.split('\t')[0]: [float(value.replace(',', '')) for value in line.strip().split('\t')[1:]] for line in lines[1:]}

    return categories, data



# Reading data from the file
categories, data = read_data_from_file_v4(data_file_path)

# Define the y position for each category
y_pos = np.arange(len(categories))

# Define new colors for each modality
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
colors = ['#2ca02c', '#ff7f0e']

# Start plotting with updated colors, grid and bold annotations
fig, ax = plt.subplots(figsize=(10, 6))

# Plot horizontal bars for each modality
bar_width = 0.15
for idx, (modality, values) in enumerate(data.items()):
    ax.barh(y_pos - bar_width/2 + idx*bar_width, values, bar_width, label=modality, color=colors[idx % len(colors)], log=True)

# Add annotations to the bars
for idx, (modality, values) in enumerate(data.items()):
    for i, value in enumerate(values):
        ax.text(value, y_pos[i] - bar_width/2 + idx*bar_width, f'{value:.1f}', ha='right', va='center', fontweight='bold')

# Set labels and title with updated colors
ax.set_xlabel('Values', color='black')
ax.set_title('MT-DETR vs. HRFuser: C+L+R with Tightly-Coupled Fusion: Complexity and Performance', color='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, color='black')
ax.legend()

# Set the scale of the x-axis to logarithmic
ax.set_xscale('log')

# Add grid to the plot
ax.grid(True)

# Adjust layout to make room for the annotations
plt.tight_layout()

# Save the plot to a file
output_path = root_path + 'model_complexity.png'
plt.savefig(output_path)

# save svg
# Save the plot as an SVG file
output_path = root_path + 'model_complexity.svg'
plt.savefig(output_path)

# save pdf
# Save the plot as a PDF
output_path = root_path + 'model_complexity.pdf'
plt.savefig(output_path)
