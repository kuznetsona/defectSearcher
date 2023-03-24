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

cmd = f'python yolov5/train.py --img 416 --batch 16 --epochs 50 --data ' \
      f'PycharmProjects/newProject/custom_coco.yaml --weights ' \
      f'yolov5s.pt'
os.system(cmd)