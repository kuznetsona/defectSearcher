import os

folder_path = "dishonest_p1/dishonest_p1"

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            lines = file.readlines()
        with open(os.path.join(folder_path, filename), 'w') as file:
            for line in lines:
                # Если строка начинается с числа 4, 5, 6, 7, 8 или 9, то пропускаем ее
                #if line[0] in '57':
                #    print(filename)
                #    continue
                if line[0] == '5':
                    line = '6' + line[1:]
                    print(line)
                # Иначе записываем строку в файл
                file.write(line)