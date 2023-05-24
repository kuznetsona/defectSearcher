import os
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

def load_data(det_folder, gt_file):
    # загрузка данных
    det_files = os.listdir(det_folder)
    det_files.sort()

    det_list = []
    for file in det_files:
        det_path = os.path.join(det_folder, file)
        #det_df = pd.read_csv(det_path, header=None, names=["class", "x_center", "y_center", "width", "height", "confidence"])
        det_df = pd.read_csv(det_path, header=None,
                             names=["class", "x_center", "y_center", "width", "height", "confidence"], sep=" ")

        det_list.append(det_df)
    det_data = pd.concat(det_list)

    gt_data = pd.read_csv(gt_file, header=None, names=["class", "x_center", "y_center", "width", "height"])

    return det_data, gt_data

def build_feature_space(det_data, gt_data):
    # создание матрицы признаков
    features = []
    for index, det in det_data.iterrows():
        center_x = det["x_center"] + det["width"] / 2
        center_y = det["y_center"] + det["height"] / 2
        for index, gt in gt_data.iterrows():
            gt_center_x = gt["x_center"] + gt["width"] / 2
            gt_center_y = gt["y_center"] + gt["height"] / 2
            dist = np.sqrt((center_x - gt_center_x)**2 + (center_y - gt_center_y)**2)
            features.append([dist, det["confidence"]])

        # наложение разных классов
        for index, gt in gt_data.iterrows():
            if det["class"] == gt["class"]:
                features[index+len(gt_data)*index].append(1)
            else:
                features[index+len(gt_data)*index].append(0)

    return pd.DataFrame(features)

def train_and_validate_model(X_train, y_train, X_val, y_val):
    # обучение SVM
    clf = svm.SVC(kernel='linear', C=1, probability=True)
    clf.fit(X_train, y_train)

    # оценка модели
    train_acc = clf.score(X_train, y_train)
    val_acc = clf.score(X_val, y_val)

    return clf, train_acc, val_acc

# пример использования функций
det_folder = "exp6/labels"

gt_file = "val"

# загрузка данных
det_data, gt_data = load_data(det_folder, gt_file)

# создание матрицы признаков
features = build_feature_space(det_data, gt_data)

# разделение на train и validation
X_train, X_val, y_train, y_val = train_test_split(features.iloc[:, :-2], features.iloc[:, -1], test_size=0.2)

# обучение и валидация модели
model, train_acc, val_acc = train_and_validate_model(X_train, y_train, X_val, y_val)
print(f"Train accuracy: {train_acc}")
print(f"Validation accuracy: {val_acc}")

