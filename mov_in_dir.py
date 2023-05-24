import os
import shutil
# директория с изображениями, которые нужно найти. Сюда будут перемещаться найденные текстовые файлы
jpg_path = "images/val/Nepamyatnik"
# директория с текстовыми файлами где ищет по названию изоюражений в jpg_path. Отсюда перемещаются файлы
txt_path = "labels/train/Moyka120"

jpeg_files = [f for f in os.listdir(jpg_path) if f.endswith('.jpg')]

for jpeg_file in jpeg_files:
    txt_file = os.path.splitext(jpeg_file)[0] + ".txt"
    txt_file_path = os.path.join(txt_path, txt_file)
    if os.path.exists(txt_file_path):
        shutil.move(txt_file_path, jpg_path)