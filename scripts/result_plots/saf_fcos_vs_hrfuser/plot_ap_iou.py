import matplotlib.pyplot as plt
import numpy as np

# Reading the AP values from the file
file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser/ap_iou.txt'
ap_values = np.loadtxt(file_path)

# The values are in the order AP, AP (0.5), AP (0.75), we need to reorder them.
# Assuming the first row corresponds to HRFuser and the second to SAF-FCOS
HRFuser_AP = [ap_values[0][1], ap_values[0][2], ap_values[0][0]]  # Reordered to AP (0.5), AP (0.75), AP
SAF_FCO_AP = [ap_values[1][1], ap_values[1][2], ap_values[1][0]]  # Reordered to AP (0.5), AP (0.75), AP

# Set font size
YOUR_FONT_SIZE = 16
plt.rcParams['font.size'] = YOUR_FONT_SIZE

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting each method with the correct order of AP values
plt.plot(['AP (0.5)', 'AP (0.75)', 'AP'], HRFuser_AP, '-o', label='HRFuser')
plt.plot(['AP (0.5)', 'AP (0.75)', 'AP'], SAF_FCO_AP, '-o', label='SAF-FCOS')

# Annotating the data points with adjusted positions
for i, (ap_h, ap_s) in enumerate(zip(HRFuser_AP, SAF_FCO_AP)):
    if ap_h > ap_s:
        plt.annotate(f'{ap_h}', (i, ap_h), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
        plt.annotate(f'{ap_s}', (i, ap_s), textcoords="offset points", xytext=(0,-20), ha='center', fontweight='bold')
    else:
        plt.annotate(f'{ap_s}', (i, ap_s), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
        plt.annotate(f'{ap_h}', (i, ap_h), textcoords="offset points", xytext=(0,-20), ha='center', fontweight='bold')

# Set the ylim to create space above the highest data point
plt.ylim(0, 100)

# Set y-axis with interval of 10
plt.yticks(range(0, 105, 10))

# Adding labels and title
plt.xlabel('AP @ IoU', labelpad=5)
plt.ylabel('Average Precision (AP)')
plt.title('HRFuser vs. SAF-FCOS AP IoU')
plt.legend()
plt.grid(True)

# Adjust x-axis tick labels position
ax = plt.gca()  # Get the current Axes instance
ax.tick_params(axis='x', which='major', pad=5)  # Increase pad to move the tick labels down

# Save the plot as PDF again
root_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser'
file_path = 'ap_iou_plot.pdf'
plt.savefig(f'{root_path}/{file_path}')
