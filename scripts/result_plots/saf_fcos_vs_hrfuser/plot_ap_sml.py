import matplotlib.pyplot as plt
import numpy as np

# Reading the AP values from the file
file_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser/ap_sml.txt'
ap_values = np.loadtxt(file_path)

# Extracting AP values for each method
HRFuser_AR = ap_values[0]
SAF_FCO_AR = ap_values[1]

# Set font size
YOUR_FONT_SIZE = 16
plt.rcParams['font.size'] = YOUR_FONT_SIZE

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting each method
plt.plot(['AP (Small)', 'AP (Medium)', 'AP (Large)'], HRFuser_AR, '-o', label='HRFuser')
plt.plot(['AP (Small)', 'AP (Medium)', 'AP (Large)'], SAF_FCO_AR, '-o', label='SAF-FCOS')

# Annotating the data points with adjusted positions
for i, (ap_h, ap_s) in enumerate(zip(HRFuser_AR, SAF_FCO_AR)):
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
# plt.xlabel('Object Size')
plt.xlabel('AP @ Object Size', labelpad=5)
plt.ylabel('Average Precision (AP)')
plt.title('HRFuser vs. SAF-FCOS AP s, m, l')
plt.legend()
plt.grid(True)

# Adjust x-axis tick labels position
ax = plt.gca()  # Get the current Axes instance
ax.tick_params(axis='x', which='major', pad=5)  # Increase pad to move the tick labels down

# Save the plot as PDF again
root_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser'
file_path = 'ap_sml_plot.pdf'
plt.savefig(f'{root_path}/{file_path}')
file_path = 'ap_sml_plot.svg'
plt.savefig(f'{root_path}/{file_path}')
