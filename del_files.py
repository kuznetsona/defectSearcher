import os

def delete_files(img_dir, txt_dir ):
    img_files = os.listdir(img_dir)
    txt_files = os.listdir(txt_dir)

    # Определяем различия между двумя наборами файлов
    diff_files_txt = [f for f in txt_files if os.path.splitext(f)[0] not in [os.path.splitext(t)[0] for t in img_files]]

    # Выводим список разметки, которые есть в директории, но которых нет в директории с изображениями
    print(diff_files_txt)
    print(len(diff_files_txt))
    for f in diff_files_txt:
        os.remove(os.path.join(txt_dir, f))



# Директория с изображениями
img_dir = 'trainBuild_8cl_dishonest_p1_2/images/val'
# Директория с текстовыми файлами
txt_dir = 'trainBuild_8cl_dishonest_p1_2/labels/val'

delete_files(img_dir, txt_dir)
