import matplotlib.pyplot as plt
import numpy as np


'''
TXT data

Method	Trinable Params (M)	GFLOPs	FPS
HRFuser	48.8	58.7	1.9
SAF-FCOS	50.8	2,200.0	11
'''

root_path = '/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/saf_fcos_vs_hrfuser/'

# Reading the AP values from the file
file_path = root_path + 'model_complexity.txt'


# File path to the data file
data_file_path = root_path + 'model_complexity.txt'


def read_data_from_file_v3(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract categories (skipping the 'Method' column)
    categories = lines[0].strip().split('\t')[1:]
    hrfuser_values = []
    saf_fcos_values = []

    # Assuming the second line is HRFuser and the third line is SAF-FCOS
    hrfuser_data = lines[1].strip().split('\t')[1:]
    saf_fcos_data = lines[2].strip().split('\t')[1:]

    # Convert string values to float, handling commas in numbers
    hrfuser_values = [float(value.replace(',', '')) for value in hrfuser_data]
    saf_fcos_values = [float(value.replace(',', '')) for value in saf_fcos_data]

    return categories, hrfuser_values, saf_fcos_values

# Reading data from the file
categories, hrfuser_values, saf_fcos_values = read_data_from_file_v3(data_file_path)

# Define the y position for each category
y_pos = np.arange(len(categories))

# Define new colors from the image provided
hrfuser_color = '#1f77b4'  # blue color
saf_fcos_color = '#ff7f0e'  # orange color

# Start plotting with updated colors, grid and bold annotations
fig, ax = plt.subplots()

# Plot horizontal bars with new colors
bar_width = 0.4
rects1 = ax.barh(y_pos - bar_width/2, hrfuser_values, bar_width, label='HRFuser', color=hrfuser_color, log=True)
rects2 = ax.barh(y_pos + bar_width/2, saf_fcos_values, bar_width, label='SAF-FCOS', color=saf_fcos_color, log=True)

# Add the annotations to the bars with bold font
# Adjusting only the largest value's annotation to be inside the bar
for rect in rects1 + rects2:
    width = rect.get_width()
    # Check if this is the largest value
    if width == max(saf_fcos_values):
        # Place the annotation inside the bar
        ax.text(width * 0.95, rect.get_y() + rect.get_height() / 2, f'{width}', ha='right', va='center', fontweight='bold')
    else:
        # Place the annotation outside the bar
        ax.text(width, rect.get_y() + rect.get_height() / 2, f'{width}', ha='left', va='center', fontweight='bold')

# Set labels and title with updated colors
ax.set_xlabel('Values', color='black')
# ax.set_ylabel('Parameters', color='black')
ax.set_title('HRFuser vs. SAF-FCOS: Complexity and Performance', color='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, color='black')
ax.legend()

# Set the scale of the x-axis to logarithmic
ax.set_xscale('log')

# Add grid to the plot
ax.grid(True)

# Adjust layout to make room for the annotations
plt.tight_layout()



# Show the plot
plt.savefig( root_path + 'model_complexity.pdf')
