from typing import List
import os

def process_objects(input_file: str, class_num) -> List[str]:
    queue = []
    with open(input_file, 'r') as f:
        for line in f:
            obj_class, x_center, y_center, width, height, confidence = map(float, line.split())
            if class_num == 7 and obj_class == 7 and confidence >= 0.3:
                queue.append(line)
            elif class_num == 5 and obj_class == 5 and confidence >= 0.4:
                queue.append(line)
    return queue


def is_inside(obj2, obj1):
    # проверяем объект obj2 полностью внутри объекта obj1
    x1, y1, w1, h1 = obj1[1:-1]
    x2, y2, w2, h2 = obj2[1:-1]
    x1_min, y1_min, x1_max, y1_max = x1 - w1 / 2, y1 - h1 / 2, x1 + w1 / 2, y1 + h1 / 2
    x2_min, y2_min, x2_max, y2_max = x2 - w2 / 2, y2 - h2 / 2, x2 + w2 / 2, y2 + h2 / 2

    if x1_min > x2_min and y1_min > y2_min and x1_max < x2_max and y1_max < y2_max:
        return True
    else:
        return False


def intersection_over_union(boxA, boxB):
    #вычисляем iou

    WIDTH = 1000
    HEIGHT = 1000

    x1A, y1A, wA, hA = boxA[1:-1]
    x1A = int(x1A * WIDTH - (wA * WIDTH / 2))
    y1A = int(y1A * HEIGHT - (hA * HEIGHT / 2))
    x2A = int(x1A + (wA * WIDTH))
    y2A = int(y1A + (hA * HEIGHT))

    x1B, y1B, wB, hB = boxB[1:-1]
    x1B = int(x1B * WIDTH - (wB * WIDTH / 2))
    y1B = int(y1B * HEIGHT - (hB * HEIGHT / 2))
    x2B = int(x1B + (wB * WIDTH))
    y2B = int(y1B + (hB * HEIGHT))

    xA = max(x1A, x1B)
    yA = max(y1A, y1B)
    xB = min(x2A, x2B)
    yB = min(y2A, y2B)

    intersection_area = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    boxA_area = (wA * WIDTH) * (hA * HEIGHT)
    boxB_area = (wB * WIDTH) * (hB * HEIGHT)
    union_area = float(boxA_area + boxB_area - intersection_area)

    iou = intersection_area / union_area

    return iou


def post_processing(input_file, output_file):
    queue7 = process_objects(input_file, 7)
    first_list = []
    if len(queue7) == 0:
        with open(input_file, "r") as file:
            for line in file:
                first_list.append(line)
    else:
        for item in queue7:
            if not item.endswith("\n"):
                first_list.append(item + '\n')
            else:
                first_list.append(item)
            with open(input_file, "r") as file:
                for line in file:
                    if line[0] != "7" and line[0] != "5":
                        boxA = list(map(float, item.split(' ')))
                        boxB = list(map(float, line.split(' ')))
                        iou = intersection_over_union(boxA, boxB)
                        if (iou != 0.0):
                            first_list.append(line)
    queue5 = process_objects(input_file, 5)
    for item in queue5:
        boxA = list(map(float, item.split(' ')))
        is_inside_5 = False
        for el in first_list:
            if el[0] == "7":
                continue
            elif el[0] == "5":
                boxB = list(map(float, el.split(' ')))
                if is_inside(boxA, boxB):
                    is_inside_5 = True
            else:
                boxB = list(map(float, el.split(' ')))
                if is_inside(boxA, boxB):
                    if el in first_list:
                        first_list.remove(el)
        if not is_inside_5:
            first_list.append(item)
    with open(output_file, 'w') as f:
        f.writelines(first_list)




input_file = '/20220415_114140.txt'
output_file = '/20220415_114140 — копия.txt'

post_processing(input_file, output_file)


#folder_path = "exp10/labels"
#folder_postProcessing = "exp10/labels/postProcessingLabels"
#if not os.path.exists(folder_postProcessing):
#    os.makedirs(folder_postProcessing)

#for filename in os.listdir(folder_path):
#    if filename.endswith(".txt"):
#        input_file = os.path.join(folder_path, filename)
#        output_file = os.path.join(folder_postProcessing, filename)
 #       post_processing(input_file, output_file)