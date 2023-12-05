'''
This script is designed to crop an image to match the dimensions used by the HRFuser in the MT-DETR framework. This script automates the cropping process to ensure consistency in image dimensions between HRFuser and MT-DETR. It centers the cropping area on the second image and adjusts the dimensions to match the first image's size, used by HRFuser.

Inputs:
    img_path_2: Path to the image that needs to be cropped.
    center_x, center_y: Center coordinates for cropping on the second image.
    target_width, target_height: The width and height of the target cropped image, which should match the HRFuser's image size.

Output:
    cropped_image.png: The cropped image saved at the specified location.

Assumptions:
    The script assumes that the center of the image is offset by (-30, +80) pixels from the actual center.
'''

from PIL import Image

# Load the second image
img_path_2 = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/mt_detr_weights/inference/early_fusion/early_camera_lidar_radar_single_gpu_2023-10-30_03-28-55_214253_2023-10-31_01-15-04_214294/2018-02-04_00-00-32_00000.png"
img2 = Image.open(img_path_2)

# Center coordinates of the second image
center_x, center_y = (img2.size[0] // 2) - 30, (img2.size[1] // 2) + 80

# Dimensions of the first image (to match)
target_width, target_height = 1248, 384

# Calculate the cropping box
left = center_x - target_width // 2
top = center_y - target_height // 2
right = center_x + target_width // 2
bottom = center_y + target_height // 2

# Crop the image
cropped_img = img2.crop((left, top, right, bottom))

# Save the cropped image
cropped_img_path = "cropped_image.png"
cropped_img.save(cropped_img_path)