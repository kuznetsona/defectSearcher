import os

directory = 'newProject/trainingBuilding_data/labels/val/M-T'

for filename in os.listdir(directory):
    if filename.endswith('.JPG'):
        os.remove(os.path.join(directory, filename))