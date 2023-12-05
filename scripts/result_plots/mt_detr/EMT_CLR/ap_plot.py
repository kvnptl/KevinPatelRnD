import matplotlib.pyplot as plt
import numpy as np

# Path to the data file
root_path = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/scripts/result_plots/mt_detr/EMT_CLR/"
file_path = root_path + 'ap.txt'  # Update this with the actual path

# Function to read and parse data from the file
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract modalities
        modalities = [line.split('\t')[0] for line in lines[3:]]

        # Initialize dictionary to store AP values
        ap_values = {'Clear weather': [], 'Light fog': [], 'Dense fog': [], 'Snow/rain': []}
        weather_conditions = list(ap_values.keys())

        # Extract AP values for each modality
        for i, line in enumerate(lines[3:]):  # Data starts from the 4th line
            values = line.split('\t')
            for j, weather in enumerate(weather_conditions):
                day_value = float(values[j * 2 + 1])
                night_value = float(values[j * 2 + 2])
                ap_values[weather].append((day_value, night_value))

    return modalities, ap_values

# Read the data from the file
modalities, ap_values = read_data(file_path)

# Colors for each modality
colors = ['blue', 'red', 'orange']

# Define function to plot data with lines bolded between day and night
def plot_data_bolded(modality_index, modality_label, color):
    x_values = np.arange(len(ap_values) * 2)
    y_values = []

    # Extract y-values for the specific modality across all weather conditions
    for weather in ap_values.values():
        y_values.extend([weather[modality_index][0], weather[modality_index][1]])

    plt.plot(x_values, y_values, 'o-', label=modality_label, color=color, linewidth=1)
    for i in range(0, len(x_values), 2):
        plt.plot(x_values[i:i+2], y_values[i:i+2], color=color, linewidth=3)

    # Custom annotation placement and bold font for annotations
    for x, y in zip(x_values, y_values):
        if modality_label == 'Tightly-coupled':
            va = 'bottom'
            offset = 10
        else:
            va = 'top'
            offset = -10
        plt.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0, offset), 
                     ha='center', va=va, fontweight='bold')

# Create a new figure
plt.figure(figsize=(15, 7))

# Plotting the bolded lines for each modality
for i, (modality_label, color) in enumerate(zip(modalities, colors)):
    plot_data_bolded(i, modality_label, color)

# Setting up the X-axis with custom labels for 'Day' and 'Night'
weather_conditions = list(ap_values.keys())
day_night_labels = ['Day', 'Night'] * len(weather_conditions)
day_night_ticks = np.arange(len(day_night_labels))

# Setting the weather conditions centered between 'Day' and 'Night'
weather_ticks = np.arange(0, len(weather_conditions) * 2, 2) + 0.5
weather_labels = weather_conditions

# Applying the custom ticks and labels
plt.xticks(day_night_ticks, day_night_labels)  # Set day/night labels
plt.gca().set_xticks(weather_ticks, minor=True)  # Set weather condition labels as minor ticks
plt.gca().set_xticklabels(weather_labels, minor=True)
plt.tick_params(axis='x', which='minor', pad=15)

# Extracting 'C+L+R' y-values for trendline calculation
clr_y_values = [ap for weather in ap_values.values() for ap in weather[-1]]
x_values = np.arange(len(clr_y_values))

# Calculate the trendline
z = np.polyfit(x_values, clr_y_values, 1)
p = np.poly1d(z)

# Plot the trendline
plt.plot(x_values, p(x_values), "k--", linewidth=2, label="Trend (Tightly-coupled)")

# Adding the legend
plt.legend()

# Grid, title, and axis labels
plt.grid(True)
plt.title('MT-DETR C+L+R across fusion architectures: Average Precision (AP) by weather conditions')
plt.ylabel('Average Precision (AP)')
plt.xlabel('Weather Conditions', labelpad=10)

# Adjust layout to accommodate the second row of labels
plt.tight_layout(rect=[0, 0.03, 1, 1])

# Show the plot
file_path = "ap.png"
plt.savefig(f'{root_path}/{file_path}')

# Show the plot
file_path = "ap.svg"
plt.savefig(f'{root_path}/{file_path}')

# save pdf
# Save the plot as a PDF
file_path = "ap.pdf"
plt.savefig(f'{root_path}/{file_path}')