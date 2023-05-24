import os

# путь к папке с файлами результатов детекции
results_folder = "C:/Users/Daria/OneDrive/Рабочий стол/Diplom/models/detect_new5/labels"
# путь к папке, куда будут сохранены новые файлы
output_folder = "C:/Users/Daria/OneDrive/Рабочий стол/Diplom/models/detect_new5/labels_new"
# класс, который нужно сохранить
target_class = "15"

# перебираем файлы с результатами детекции
for file_name in os.listdir(results_folder):
    if file_name.endswith(".txt"):
        with open(os.path.join(results_folder, file_name), "r") as f:
            lines = f.readlines()
        # перебираем строки в каждом файле
        for line in lines:
            parts = line.strip().split()
            class_id = parts[0]
            if class_id == target_class:
                # объект класса 15
                x_center = float(parts[1])
                y_center = float(parts[2])
                width = float(parts[3])
                height = float(parts[4])
                # проверяем пересечение с объектами других классов
                intersection = False
                for other_line in lines:
                    if line != other_line:
                        other_parts = other_line.strip().split()
                        other_class_id = other_parts[0]
                        if other_class_id != target_class:
                            other_x_center = float(other_parts[1])
                            other_y_center = float(other_parts[2])
                            other_width = float(other_parts[3])
                            other_height = float(other_parts[4])

                            # вычисляем координаты углов прямоугольников
                            x1 = (x_center - width / 2)
                            y1 = (y_center - height / 2)
                            x2 = (x_center + width / 2)
                            y2 = (y_center + height / 2)
                            other_x1 = (other_x_center - other_width / 2)
                            other_y1 = (other_y_center - other_height / 2)
                            other_x2 = (other_x_center + other_width / 2)
                            other_y2 = (other_y_center + other_height / 2)

                            # проверяем пересечение
                            if x1 < other_x2 and x2 > other_x1 and y1 < other_y2 and y2 > other_y1:
                                intersection = True
                                break

                if intersection:
                    # сохраняем строку с объектом класса 15 и объектами других классов
                    output_line = line
                    for other_line in lines:
                        other_parts = other_line.strip().split()
                        other_class_id = other_parts[0]
                        if other_class_id != target_class:
                            output_line += other_line
                    # записываем результат в новый файл
                    output_file_name = file_name.replace(".txt", ".txt")
                    with open(os.path.join(output_folder, output_file_name), "a") as f:
                        f.write(output_line)

