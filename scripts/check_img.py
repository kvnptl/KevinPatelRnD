# import cv2

# # read image

# img = cv2.imread("/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/nuscenes/lidar_samples/rih/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151604012404.png")

# print(img.shape)
# pass

'''

Plot the histograms for R, G, and B

'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread("/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/hrfuser/data/nuscenes/lidar_samples/rih/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151604012404.png")


# Convert from BGR to RGB (OpenCV loads images in BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imwrite("orig_image.png", image)

# Prepare the figure
plt.figure(figsize=(16, 5))

colors = ('r', 'g', 'b')

# Plot the histograms for R, G, and B
for i, color in enumerate(colors):
    # Calculate the histogram
    histogram, bin_edges = np.histogram(
        image[:, :, i], bins=256, range=(0, 255)
    )
    
    # Normalize the histogram
    histogram = histogram / histogram.sum()

    # Plot the histogram
    plt.subplot(1, 3, i + 1)
    plt.title(f'Histogram for color {color.upper()}')
    plt.xlabel('Pixel value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    plt.plot(bin_edges[0:-1], histogram, color=color)

# plt.show()
plt.savefig("histogram.png")