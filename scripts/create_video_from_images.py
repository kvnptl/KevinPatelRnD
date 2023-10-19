import cv2
import glob
import re
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def read_image(filename):
    img = cv2.imread(filename)
    return img, filename

def create_video_from_images(img_path, video_path, fps=24):
    os.makedirs(os.path.dirname(video_path), exist_ok=True)

    numbers = re.compile(r'(\d+)')

    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        return [atoi(c) for c in re.split(numbers, text)]

    filenames = glob.glob(img_path)
    filenames.sort(key=natural_keys)

    first_image = cv2.imread(filenames[0])
    height, width, layers = first_image.shape
    size = (width, height)

    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    with ThreadPoolExecutor() as executor:
        img_array = list(tqdm(executor.map(read_image, filenames), total=len(filenames)))

    img_array.sort(key=lambda img: natural_keys(img[1]))

    for img, filename in tqdm(img_array, desc="Writing to video"):
        out.write(img)
    
    out.release()

def main():
    img_path = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/nuscenes_ground_truths/*.png"
    video_path = "/home/kpatel2s/kpatel2s/link_scratch_dir/kpatel2s/model_weights/saf_fcos_weights/tmp_ver2/nuscenes_ground_truths/1_video_6fps.mp4"
    create_video_from_images(img_path, video_path, fps=6)

if __name__ == "__main__":
    main()
