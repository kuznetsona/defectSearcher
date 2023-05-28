import os

def process_files(first_folder, second_folder):
    # Получаем список файлов из папки first
    first_files = os.listdir(first_folder)

    for file_name in first_files:
        # Формируем полные пути к файлам в папках first и second
        first_file_path = os.path.join(first_folder, file_name)
        second_file_path = os.path.join(second_folder, file_name)

        # Проверяем, существует ли файл в папке second
        if os.path.isfile(second_file_path):
            # Открываем файл из папки first для чтения
            with open(first_file_path, 'r') as first_file:
                # Читаем строки из файла в папке first
                lines = first_file.readlines()

            # Открываем файл из папки second для дописывания
            with open(second_file_path, 'a') as second_file:
                # Записываем строки, начинающиеся с 5 или 7, в файл в папке second
                for line in lines:
                    if line.startswith('5') or line.startswith('7'):
                        second_file.write(line)


first_folder = 'trainBuild_8cl_dishonest_p1/labels/val'
second_folder = 'dishonest_p1/dishonest_p1'

process_files(first_folder, second_folder)
