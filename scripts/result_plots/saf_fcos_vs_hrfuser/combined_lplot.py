import matplotlib.pyplot as plt
import numpy as np

root_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser/'

# Reading the values from the file
ap_iou_path =  root_path + 'ap_iou.txt'
ap_sml_path = root_path + 'ap_sml.txt'
ar_path = root_path + 'ar.txt'

# Load the data from text files
ap_iou_values = np.loadtxt(ap_iou_path)
ap_sml_values = np.loadtxt(ap_sml_path)
ar_values = np.loadtxt(ar_path)

# Reorder AP values to AP (0.5), AP (0.75), AP
ap_iou_values = ap_iou_values[:, [1, 2, 0]]

# Create a combined plot with one common Y-axis but different X-axis values using subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Plot data on each subplot
titles = ['AP at Different IoU', 'AP for Object Sizes', 'AR for Object Sizes']
x_values = [
    ['AP (0.5)', 'AP (0.75)', 'AP'],
    ['Small', 'Medium', 'Large'],
    ['AR (100)', 'Small', 'Medium', 'Large']
]
datasets = [ap_iou_values, ap_sml_values, ar_values]
methods = ['HRFuser', 'SAF-FCOS']

for ax, title, x_vals, dataset in zip(axes, titles, x_values, datasets):
    x = np.arange(len(x_vals))
    for i, method in enumerate(methods):
        ax.plot(x, dataset[i], '-o', label=method)
        for j, val in enumerate(dataset[i]):
            ax.annotate(f'{val:.1f}', (x[j], val), textcoords="offset points", xytext=(0,10), ha='center')
    ax.set_xticks(x)
    ax.set_xticklabels(x_vals)
    ax.set_title(title)
    ax.grid(True)

# Common Y-axis label
fig.text(0.5, -0.02, 'Metric Value', ha='center', va='center')
fig.text(0.08, 0.5, 'Average Precision (AP) / Average Recall (AR)', ha='center', va='center', rotation='vertical')

# Adding a legend
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)

# Adjust the layout
plt.tight_layout()

# Adding a legend
# axes[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)

# Save the combined plot as a PDF
combined_plot_path = root_path + 'combined_plot.pdf'
fig.savefig(combined_plot_path)
