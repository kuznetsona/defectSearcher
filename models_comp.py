import pandas as pd
import matplotlib.pyplot as plt


def build_graphs(metric):
    path = "C:/Users/Daria/OneDrive/Рабочий стол/Diplom/models/"

    yolov5n = pd.read_csv(path + "exp_n_200_hyp/results.csv")
    yolov5s = pd.read_csv(path + "exp_s_200_hyp/results.csv")
    yolov5m = pd.read_csv(path + "exp_m_200_hyp/results.csv")
    yolov5l = pd.read_csv(path + "exp_l_200_hyp/results.csv")
    yolov5x = pd.read_csv(path + "exp4_x_200_hyp/results.csv")

    print(yolov5s.columns)

    n_model = yolov5n[metric][:156]
    s_model = yolov5s[metric][:156]
    m_model = yolov5m[metric][:156]
    l_model = yolov5l[metric][:156]
    x_model = yolov5x[metric][:156]

    x_data = yolov5l['               epoch'][:156]
    fig, ax = plt.subplots()
    #ax.plot(x_data, n_model, label='yolov5n')
    ax.plot(x_data, s_model, label='yolov5s')
    #ax.plot(x_data, m_model, label='yolov5m')
    #ax.plot(x_data, l_model, label='yolov5l')
    #ax.plot(x_data, x_model, label='yolov5x')

    ax.legend()
    plt.title(metric)
    plt.show()


metrics = ['     metrics/mAP_0.5',
           'metrics/mAP_0.5:0.95',
           '      train/box_loss',
           '      train/obj_loss',
           '      train/cls_loss',
           '   metrics/precision',
           '      metrics/recall',
           '        val/box_loss',
           '        val/obj_loss',
           '        val/cls_loss',
           '               x/lr0',
           '               x/lr1',
           '               x/lr2']

for metric in metrics:
    build_graphs(metric)
