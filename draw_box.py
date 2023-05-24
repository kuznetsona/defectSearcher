from PIL import Image, ImageDraw, ImageFont
import os


# написать флаг вывода бокса 7 и 5

# Путь к папке с изображениями и аннотациями
image_folder = "Diplom/validation"
annotation_folder = "exp10/labels/postProcessingLabels"

folder_postProcessing = "exp10/labels/postProcessingImages"
if not os.path.exists(folder_postProcessing):
    os.makedirs(folder_postProcessing)

class_names = ['exposure', 'force Crack', 'cracking', 'biodestruction', 'repair',
               'not_detect', 'Destruction', 'facade']


class_colors = {
    0: (255, 57, 56),  # exposure
    1: (255, 158, 151),  # Force crack
    2: (253, 114, 29),  # cracking
    3: (253, 179, 31),  # biodestruction
    4: (208, 209, 50),  # repair
    5: (112, 237, 66),  # not_detect
    6: (147, 204, 24),  # Destruction
    7: (61, 219, 134),  # facade
}

# Проходим по всем файлам с изображениями и аннотациями
for filename in os.listdir(image_folder):
    if filename.endswith('.JPG') or filename.endswith('.jpg'):

        image_path = os.path.join(image_folder, filename).replace('\\', '/')
        with Image.open(image_path) as img:
            # Отключаем поворот изображения
            img = img.copy()
            img_exif = img.getexif()
            if img_exif:
                orientation = img_exif.get(274)
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
            image = img.convert('RGB')


        if filename.endswith('.JPG'):
            annotation_path = os.path.join(annotation_folder, filename.replace('.JPG', '.txt')).replace('\\', '/')
        else:
            annotation_path = os.path.join(annotation_folder, filename.replace('.jpg', '.txt')).replace('\\', '/')

        try:
            with open(annotation_path, 'r') as f:
                annotations = f.readlines()
            # Рисуем боксы
            for annotation in annotations:
                if annotation.split(' ')[0] == '5' or annotation.split(' ')[0] == '7' or annotation.split(' ')[0] == '6':
                    continue
                class_id, x_center, y_center, width, height, confidence = annotation.split()
                class_id = int(class_id)
                x_center, y_center, width, height, confidence = map(float, [x_center, y_center, width, height, confidence])
                # Вычисляем координаты
                x1 = int((x_center - width / 2) * image.size[0])
                y1 = int((y_center - height / 2) * image.size[1])
                x2 = int((x_center + width / 2) * image.size[0])
                y2 = int((y_center + height / 2) * image.size[1])

                draw = ImageDraw.Draw(image)

                color = class_colors.get(class_id)

                draw.rectangle((x1, y1, x2, y2), outline=color, width=5)

                # Подписываем бокс
                label = f'{class_names[class_id]} {confidence:.2f}'
                text_bbox = draw.textbbox((x1, y1 - 5), label, font=ImageFont.truetype('arial.ttf', 23))
                text_size = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])

                draw.rectangle((x1, y1 - 5, x1 + text_size[0], y1 + text_size[1] - 5), fill=color)
                draw.text((x1, y1 - 5), label, fill=(255, 255, 255), font=ImageFont.truetype('arial.ttf', 23))

            result_path = os.path.join(folder_postProcessing, filename)
            image.save(result_path)
        except FileNotFoundError:
            print(f"File '{annotation_path}' does not exist")