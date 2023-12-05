import matplotlib.pyplot as plt

# Given data
methods = ['HRFuser', 'SAF-FCOS']
AP = [64.00, 70.20]
AP_075 = [69.70, 77.60]
AP_05 = [81.40, 90.40]

# Set font to bold for everything
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

# Plotting the data
plt.figure(figsize=(10, 6))

# Plotting each method and annotating
for i, method in enumerate(methods):
    AP_scores = [AP_05[i], AP_075[i], AP[i]]
    plt.plot(['AP (0.5)', 'AP (0.75)', 'AP'], AP_scores, '-o', label=method)
    for j, ap_score in enumerate(AP_scores):
        plt.annotate(f'{ap_score}', (j, ap_score), textcoords="offset points", 
                     xytext=(0,10), ha='center', fontweight='bold')

# Set the y-axis limits and ticks
plt.ylim(50, 100)
plt.yticks(range(50, 105, 5))

# Adding labels and title
plt.xlabel('Metric')
plt.ylabel('Average Precision (AP)')
plt.title('HRFuser vs. SAF-FCOS')

# Calculate deltas
delta_AP_05 = AP_05[1] - AP_05[0]
delta_AP_075 = AP_075[1] - AP_075[0]
delta_AP = AP[1] - AP[0]

# Annotate the deltas
plt.annotate(f'Δ {delta_AP_05:.1f}', xy=(0, (AP_05[0] + AP_05[1]) / 2), xytext=(0, 25),
             textcoords="offset points", ha='center', fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='<->', lw=1.5))
plt.annotate(f'Δ {delta_AP_075:.1f}', xy=(1, (AP_075[0] + AP_075[1]) / 2), xytext=(0, 25),
             textcoords="offset points", ha='center', fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='<->', lw=1.5))
plt.annotate(f'Δ {delta_AP:.1f}', xy=(2, (AP[0] + AP[1]) / 2), xytext=(0, 25),
             textcoords="offset points", ha='center', fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='<->', lw=1.5))

# Adding grid and legend
plt.grid(True)
plt.legend()

# Save the plot as a PDF
plt.savefig('ap_plot_with_deltas.pdf')
