import os
import yaml

# set up paths
cwd = os.getcwd()
data_path = os.path.join(cwd, 'data')
config_path = os.path.join(cwd, 'config', 'custom_coco.yaml')

# load configuration file
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# run training script
cmd = f'python yolov5/detect.py --img 896 --weights ' \
      f'yolov5/runs/train/exp/weights/best.pt --name result_detect ' \
      f'--save-txt --conf-thres 0.15 --source newProject/validation'
os.system(cmd)