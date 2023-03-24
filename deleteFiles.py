import os

directory = 'newProject/trainingBuilding_data/labels/val/M-T' # specify directory path

for filename in os.listdir(directory): # iterate through all files in the directory
    if filename.endswith('.JPG'): # check if file ends with .txt
        os.remove(os.path.join(directory, filename)) # delete the file