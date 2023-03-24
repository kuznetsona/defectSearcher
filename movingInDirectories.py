import os
import shutil

jpg_path = "Diplom/trainingBuilding/Ю-Л"
txt_path = "Diplom/trainingBuilding"

jpeg_files = [f for f in os.listdir(jpg_path) if f.endswith('.JPG')]

for jpeg_file in jpeg_files:
    txt_file = os.path.splitext(jpeg_file)[0] + ".txt"
    txt_file_path = os.path.join(txt_path, txt_file)
    if os.path.exists(txt_file_path):
        shutil.move(txt_file_path, jpg_path)