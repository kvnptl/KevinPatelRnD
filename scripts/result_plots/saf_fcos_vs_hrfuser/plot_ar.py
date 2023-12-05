# Re-importing numpy and matplotlib as the execution state has been reset
import numpy as np
import matplotlib.pyplot as plt

# Load the AR values from the text file
ar_values = np.loadtxt('/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser/ar.txt')

# Set font size
YOUR_FONT_SIZE = 16
plt.rcParams['font.size'] = YOUR_FONT_SIZE

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting each method with the correct order of AR values
plt.plot(['AR (100)', 'AR (Small)', 'AR (Medium)', 'AR (Large)'], ar_values[0], '-o', label='HRFuser')
plt.plot(['AR (100)', 'AR (Small)', 'AR (Medium)', 'AR (Large)'], ar_values[1], '-o', label='SAF-FCOS')

# Annotating the data points with adjusted positions
for i, (ar_h, ar_s) in enumerate(zip(ar_values[0], ar_values[1])):
    if ar_h > ar_s:
        plt.annotate(f'{ar_h}', (i, ar_h), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
        plt.annotate(f'{ar_s}', (i, ar_s), textcoords="offset points", xytext=(0,-20), ha='center', fontweight='bold')
    else:
        plt.annotate(f'{ar_s}', (i, ar_s), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
        plt.annotate(f'{ar_h}', (i, ar_h), textcoords="offset points", xytext=(0,-20), ha='center', fontweight='bold')

# Set the ylim to create space above the highest data point
plt.ylim(0, 100)

# Set y-axis with interval of 10
plt.yticks(range(0, 105, 10))

# Adding labels and title
plt.xlabel('AR(100) and AR @ Object Size', labelpad=5)
plt.ylabel('Average Recall (AR)')
plt.title('HRFuser vs. SAF-FCOS AR(100) and AR s, m, l')
# plt.legend()
plt.legend(loc='upper center', bbox_to_anchor=(0.25, 1.))
plt.grid(True)

# Adjust x-axis tick labels position
ax = plt.gca()  # Get the current Axes instance
ax.tick_params(axis='x', which='major', pad=5)  # Increase pad to move the tick labels down

# Save the plot as a PDF
# Save the plot as PDF again
root_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser'
file_path = 'ar_plot.pdf'
plt.savefig(f'{root_path}/{file_path}')
file_path = 'ar_plot.svg'
plt.savefig(f'{root_path}/{file_path}')