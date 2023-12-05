import matplotlib.pyplot as plt
import numpy as np

# Path to the data file
root_path = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/mt_detr/early/"

# Path to the data file for AR values
ar_file_path = root_path + 'ar.txt'  # Update this with the actual path

# Function to read and parse data from the file
def read_ar_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract modalities
        modalities = [line.split('\t')[0] for line in lines[3:]]

        # Initialize dictionary to store AR values
        ar_values = {'Clear weather': [], 'Light fog': [], 'Dense fog': [], 'Snow/rain': []}
        weather_conditions = list(ar_values.keys())

        # Extract AR values for each modality
        for i, line in enumerate(lines[3:]):  # Data starts from the 4th line
            values = line.split('\t')
            for j, weather in enumerate(weather_conditions):
                day_value = float(values[j * 2 + 1])
                night_value = float(values[j * 2 + 2])
                ar_values[weather].append((day_value, night_value))

    return modalities, ar_values

# Read the AR data from the file
modalities_ar, ar_values = read_ar_data(ar_file_path)

# Colors for each modality (you can update these if needed)
colors_ar = ['blue', 'red', 'orange']

# Define function to plot data with lines bolded between day and night
def plot_ar_data_bolded(modality_index, modality_label, color):
    x_values = np.arange(len(ar_values) * 2)
    y_values = [ar for weather in ar_values.values() for ar in weather[modality_index]]
    plt.plot(x_values, y_values, 'o-', label=modality_label, color=color, linewidth=1)
    for i in range(0, len(x_values), 2):
        plt.plot(x_values[i:i+2], y_values[i:i+2], color=color, linewidth=3)

    # Custom annotation placement and bold font for annotations
    for x, y in zip(x_values, y_values):
        if modality_label == 'C':
            va = 'bottom'
            offset = 10
        else:
            va = 'top'
            offset = -10
        plt.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0, offset), 
                     ha='center', va=va, fontweight='bold')

# Create a new figure for AR values
plt.figure(figsize=(15, 7))

# Plotting the bolded lines for each modality
for i, (modality_label, color) in enumerate(zip(modalities_ar, colors_ar)):
    plot_ar_data_bolded(i, modality_label, color)

# Setting up the X-axis with custom labels for 'Day' and 'Night'
weather_conditions_ar = list(ar_values.keys())
day_night_labels_ar = ['Day', 'Night'] * len(weather_conditions_ar)
day_night_ticks_ar = np.arange(len(day_night_labels_ar))

# Setting the weather conditions centered between 'Day' and 'Night'
weather_ticks_ar = np.arange(0, len(weather_conditions_ar) * 2, 2) + 0.5
weather_labels_ar = weather_conditions_ar

# Applying the custom ticks and labels for AR values
plt.xticks(day_night_ticks_ar, day_night_labels_ar)  # Set day/night labels
plt.gca().set_xticks(weather_ticks_ar, minor=True)  # Set weather condition labels as minor ticks
plt.gca().set_xticklabels(weather_labels_ar, minor=True)
plt.tick_params(axis='x', which='minor', pad=15)

# Extracting 'C+L+R' y-values for trendline calculation for AR values
clr_y_values_ar = [ar for weather in ar_values.values() for ar in weather[-1]]
x_values_ar = np.arange(len(clr_y_values_ar))

# Calculate the trendline for AR values
z_ar = np.polyfit(x_values_ar, clr_y_values_ar, 1)
p_ar = np.poly1d(z_ar)

# Plot the trendline for AR values
plt.plot(x_values_ar, p_ar(x_values_ar), "k--", linewidth=2, label="Trend (C+L+R)")

# Adding the legend for AR values
plt.legend()

# Grid, title, and axis labels for AR values
plt.grid(True)
plt.title('MT-DETR Early Fusion across modalities: Average Recall (AR) by weather conditions')
plt.ylabel('Average Recall (AR)')
plt.xlabel('Weather Conditions', labelpad=10)

# Adjust layout to accommodate the second row of labels for AR values
plt.tight_layout(rect=[0, 0.03, 1, 1])

# Show the plot
file_path = "ar.png"
plt.savefig(f'{root_path}/{file_path}')

# Show the plot
file_path = "ar.svg"
plt.savefig(f'{root_path}/{file_path}')

# save pdf
# Save the plot as a PDF
file_path = "ar.pdf"
plt.savefig(f'{root_path}/{file_path}')