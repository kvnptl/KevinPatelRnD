import cv2
import glob
import re
import os
from tqdm import tqdm

def create_video_from_images(img_path, video_path, fps=24):

  if not os.path.exists(os.path.dirname(video_path)):
    os.makedirs(os.path.dirname(video_path))

  img_array = []
  numbers = re.compile(r'(\d+)')

  def atoi(text):
    return int(text) if text.isdigit() else text

  def natural_keys(text):
    return [atoi(c) for c in re.split(numbers, text)]

  print("Step 1/3: Extracting images from folder")
  for filename in tqdm(glob.glob(img_path)):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append((img, filename))

  img_array.sort(key=lambda img: natural_keys(img[1]))

  out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
  print(f"\nStep 2/3: Video creation started. Saving to {video_path}")

  for img, filename in tqdm(img_array):
    out.write(img)
  out.release()

  print(f"\nStep 3/3: DONE! Video saved to {video_path}")

def main():

  # Create video from images
  img_path = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07_LR_0p001_Prediction/*.png"
  video_path = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/fcos_imprv_R_101_FPN_1x_ATTMIX_135_Circle_07_LR_0p001_Prediction/1_video_6fps.mp4"
  create_video_from_images(img_path, video_path, fps=6)

if __name__ == "__main__":
  main()