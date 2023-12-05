import matplotlib.pyplot as plt

# Given data
methods = ['HRFuser', 'SAF-FCOS']
AP = [64.00, 70.20]
AP_075 = [69.70, 77.60]
AP_05 = [81.40, 90.40]

# Assuming these are the number of parameters for each model (example values)
model_params = [48.8, 50.8]  # Number of parameters for HRFuser and SAF-FCOS

# Scale for marker size (you can adjust this based on your needs)
scale_factor = 1

# Set font to bold for everything
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting each method with varying marker size
for i, method in enumerate(methods):
    AP_scores = [AP_05[i], AP_075[i], AP[i]]  # Reversed order
    marker_sizes = [size * scale_factor for size in model_params]
    plt.plot(['AP (0.5)', 'AP (0.75)', 'AP'], AP_scores, '-o', label=method, markersize=marker_sizes[i])

# Annotating the data points
for i, txt in enumerate(AP_05):
    plt.annotate(f'{AP_05[i]}', (0, AP_05[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
for i, txt in enumerate(AP_075):
    plt.annotate(f'{AP_075[i]}', (1, AP_075[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
for i, txt in enumerate(AP):
    plt.annotate(f'{AP[i]}', (2, AP[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

# Set the ylim to create space above the highest data point
plt.ylim(50, 100)

# Set y-axis with interval of 5
plt.yticks(range(50, 105, 5))

# Adding labels and title
plt.xlabel('Metric')
plt.ylabel('Average Precision (AP)')
plt.title('HRFuser vs. SAF-FCOS')
plt.legend()
plt.grid(True)

# Save the plot as PDF
plt.savefig('ap_plot_with_model_params.pdf')
