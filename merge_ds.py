import os
import re

# Папки 1 и 2
folder1 = "C:/Users/Daria/OneDrive/Рабочий стол/Diplom/trainingBuilding_6labels/labels/val"
folder2 = "C:/Users/Daria/OneDrive/Рабочий стол/Diplom/trainingBuilding_11labels/labels/val"

# Регулярное выражение для поиска строки, начинающейся с числа 14
regex = r'^15.*'

# Проходим по всем файлам в папке 1
for filename in os.listdir(folder1):
    if filename.endswith('.txt'):
        file1_path = os.path.join(folder1, filename)
        file2_path = os.path.join(folder2, filename)

        # Открываем файл 1 и ищем строку, начинающуюся с числа 14
        with open(file1_path, 'r') as file1:
            for line in file1:
                if re.match(regex, line):
                    # Ищем файл 2 с таким же именем
                    for root, dirs, files in os.walk(folder2):
                        for file in files:
                            if file == filename:
                                file2_path = os.path.join(root, file)
                                break
                    # Добавляем строку в файл 2
                    with open(file2_path, 'a') as file2:
                        file2.write(line)
                        break