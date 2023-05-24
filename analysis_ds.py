import os

#по классам из classes.txt выводит количество каждого класса в папке
def count_classes(folder):
    classes_file_path = os.path.join(folder, 'classes.txt')

    class_counts = {}

    with open(classes_file_path, 'r') as classes_file:
        lines = classes_file.readlines()

        for i, line in enumerate(lines):
            class_name = line.strip()
            class_counts[i] = {'class_name': class_name, 'count': 0}

    for file_name in os.listdir(folder):
        if file_name.endswith('.txt') and file_name != 'classes.txt':
            annotation_file_path = os.path.join(folder, file_name)

            with open(annotation_file_path, 'r') as annotation_file:
                annotation_lines = annotation_file.readlines()

                for annotation_line in annotation_lines:
                    class_number = int(annotation_line.split()[0])

                    if class_number in class_counts:
                        class_counts[class_number]['count'] += 1

    class_name_width = max(len(data['class_name']) for data in class_counts.values()) + 2
    count_width = len(str(max(data['count'] for data in class_counts.values()))) + 2

    print(f"{'Class':<{class_name_width}}{'Count':<{count_width}}")
    print('-' * (class_name_width + count_width))

    for class_number, data in class_counts.items():
        class_name = data['class_name']
        count = data['count']
        print(f"{class_name:<{class_name_width}}{count:<{count_width}}")


folder_path = 'trainBuild_8cl_dishonest_p2/labels/val'
count_classes(folder_path)
