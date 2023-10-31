import re

test_log_file = "/home/kpatel2s/kpatel2s/sensor_fusion_rnd/KevinPatelRnD/bash_scripts/mt_detr/test/early_fusion/test_early_c+l+r_output.214294.out"

# Read the text file
with open(test_log_file, "r") as f:
    text = f.read()

# split the text into lines based on the newline character
lines = text.split("\n")

# in all lines find "bbox_mAP_copypaste" and tell me the count
count = sum(1 for line in lines if re.search(r"bbox_mAP_copypaste", line))

result = dict()
big_test_result_string = "TEST STRING: "

for line in lines:
    if re.search(r"data/coco_annotation", line):
        file_name = line.split("/")[-1].split(".")[0]
    if re.search(r"Average Recall\s+\(AR\)\s+@\[\s+IoU=0\.50:0\.95\s+\|\s+area=\s+all\s+\|\s+maxDets=1000\s+\]", line):
        ar_all = float(line.split(" ")[-1])
    if re.search(r"Average Recall\s+\(AR\)\s+@\[\s+IoU=0\.50:0\.95\s+\|\s+area=\s+small\s+\|\s+maxDets=1000\s+\]", line):
        ar_small = float(line.split(" ")[-1])
    if re.search(r"Average Recall\s+\(AR\)\s+@\[\s+IoU=0\.50:0\.95\s+\|\s+area=medium\s+\|\s+maxDets=1000\s+\]", line):
        ar_medium = float(line.split(" ")[-1])
    if re.search(r"Average Recall\s+\(AR\)\s+@\[\s+IoU=0\.50:0\.95\s+\|\s+area=\s+large\s+\|\s+maxDets=1000\s+\]", line):
        ar_large = float(line.split(" ")[-1])
    if re.search(r"bbox_mAP_copypaste", line):
        pattern = r"'bbox_mAP_copypaste',\s*'([^']+)'\)"
        match = re.search(pattern, line)
        if match:
            bbox_mAP_copypaste = match.group(1)
            bbox_mAP_copypaste = bbox_mAP_copypaste.split(" ")
            bbox_mAP_copypaste = [float(i) for i in bbox_mAP_copypaste]

        result[file_name] = {
            "ap, ap_50, ap_75, ap_s, ap_m, ap_l, ar_1000, ar_s, ar_m, ar_l": [*bbox_mAP_copypaste, ar_all, ar_small, ar_medium, ar_large]
        }

        big_test_result_string += ' '.join(map(str, bbox_mAP_copypaste)) + " " + str(ar_all) + " " + str(ar_small) + " " + str(ar_medium) + " " + str(ar_large) + " "

# print(result)
print(big_test_result_string)

# Append the big string to the test_log_file 
with open(test_log_file, "a") as f:
    f.write("\n")
    f.write("\n")
    f.write(big_test_result_string)
    