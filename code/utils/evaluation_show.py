import os
import numpy as np
import matplotlib.pyplot as plt
from utils import clean_label_show
import constants


def show_plot(file_path, out_path, predicted_labels, header=False, style=0):

    # if os.path.splitext(file_path)[-1] == '.csv':
    #     data = clean_label_show.read_csv(file_path)
    #     labels, x, y, z = data[0], data[1], data[2], data[3]
    #
    #     predicted_labels_total = np.zeros(shape=len(data))
    #     for i in range(1, int(len(data) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
    #         # print(i * window_length * (1 - window_repetitive_rate) + window_length)
    #         predicted_labels_total[int(i * constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE))] = predicted_labels[i - 1]

    if os.path.splitext(file_path)[-1] == '.txt':
        data, labels = clean_label_show.read_txt(file_path)
        temp = data.T
        x, y, z = temp[0], temp[1], temp[2]

        predicted_labels_total = np.zeros(shape=len(data))
        for i in range(1, int(len(data) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
            # print(i * window_length * (1 - window_repetitive_rate) + window_length)
            predicted_labels_total[int(i * constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE))] = predicted_labels[i - 1]

    # print(plt.style.available)
    # plt.style.use('bmh')

    fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    vertical_line = plt.axvline(x=0, color='purple', ls='--')
    horizontal_line = plt.axhline(y=0, color='purple', ls='--')

    def update_labels_line(_labels_line, _labels, style, predicted_lines, predicted_label):
        _new_x = [i for i in range(len(_labels)) if _labels[i] == style]
        _labels_line.set_xdata(_new_x)
        _labels_line.set_ydata([15 for _ in range(len(_new_x))])
        fig.canvas.draw_idle()

        _new_y = [j for j in range(len(predicted_label)) if predicted_label[j] == style]
        predicted_lines.set_xdata(_new_y)
        predicted_lines.set_ydata([20 for _ in range(len(_new_y))])
        fig.canvas.draw_idle()

    labels_line = plt.plot([], [], 's', color='orange')[0]
    predicted_line = plt.plot([], [], 's', color='orange')[0]
    update_labels_line(labels_line, labels, 1, predicted_line, predicted_labels_total)

    labels_line = plt.plot([], [], 's', color='blue')[0]
    predicted_line = plt.plot([], [], 's', color='blue')[0]
    update_labels_line(labels_line, labels, 2, predicted_line, predicted_labels_total)

    labels_line = plt.plot([], [], 's', color='purple')[0]
    predicted_line = plt.plot([], [], 's', color='purple')[0]
    update_labels_line(labels_line, labels, 3, predicted_line, predicted_labels_total)

    labels_line = plt.plot([], [], 's', color='slategrey')[0]
    predicted_line = plt.plot([], [], 's', color='slategrey')[0]
    update_labels_line(labels_line, labels, 4, predicted_line, predicted_labels_total)

    def on_key_press(event):
        if event.key == 'a' or event.key == 'd':
            try:
                change_index = int(vertical_line.get_xdata())
                labels[change_index: change_index + 4] = style if event.key == 'a' else 0
                # ax.lines.remove(ax.lines[-1])
            except (TypeError, Exception):
                pass
            update_labels_line(labels_line, labels, style)
        elif event.key == 'q' or event.key == 'e':
            try:
                cur_index = int(vertical_line.get_xdata())
                move_len = -1 if event.key == 'q' else 1
                vertical_line.set_xdata(cur_index + move_len)

                if labels[cur_index] == style:
                    head_index = cur_index
                    rear_index = cur_index

                    while labels[head_index] == style:
                        head_index = head_index - 1
                    head_index = head_index + 1

                    while labels[rear_index] == style:
                        rear_index = rear_index + 1

                    labels[head_index: rear_index] = 0
                    labels[head_index + move_len: rear_index + move_len] = style

                update_labels_line(labels_line, labels, style)
            except TypeError:
                pass
        elif event.key == 'left' or event.key == 'right':
            try:
                ax_temp = event.inaxes
                x_min, x_max = ax_temp.get_xlim()
                # delta = int((x_max - x_min) * 0.5) * (-1 if event.key == 'left' else 1)
                delta = 5 * (-1 if event.key == 'left' else 1)
                ax_temp.set(xlim=(x_min + delta, x_max + delta))
                cur_index = int(vertical_line.get_xdata())
                vertical_line.set_xdata(cur_index + delta)
            except (TypeError, Exception):
                pass
            # update_labels_line(labels_line, labels)
            fig.canvas.draw_idle()

    def on_scroll(event):
        try:
            ax_temp = event.inaxes
            x_min, x_max = ax_temp.get_xlim()
            delta = (x_max - x_min) / 10
            if event.button == 'up':
                ax_temp.set(xlim=(x_min + delta, x_max - delta))
                # print("up", event.inaxes)
            elif event.button == 'down':
                ax_temp.set(xlim=(x_min - delta, x_max + delta))
            fig.canvas.draw_idle()
        except (TypeError, AttributeError):
            pass

    def motion(event):
        try:
            vertical_line.set_xdata(int(event.xdata))
            horizontal_line.set_ydata(event.ydata)
            fig.canvas.draw_idle()
        except TypeError:
            pass

    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)

    fig.canvas.mpl_connect('scroll_event', on_scroll)
    fig.canvas.mpl_connect('motion_notify_event', motion)
    fig.canvas.mpl_connect('key_press_event', on_key_press)

    plt.plot(x, color='tomato', label='x')
    plt.plot(y, color='forestgreen', label='y')
    plt.plot(z, color='steelblue', label='z')

    plt.grid()
    plt.legend()
    plt.show()

    if os.path.splitext(file_path)[-1] == '.csv':
        data.to_csv(out_path, index=False, header=header)
    if os.path.splitext(file_path)[-1] == '.txt':
        with open(out_path, 'w', encoding='utf-8') as f:
            rewrite_lines = []
            for _ in range(len(data)):
                rewrite_lines.append('[%f, %f, %f, %f, %f, %f, %f, %f, %f, %d]\n' % (data[_][0],
                                                                                     data[_][1],
                                                                                     data[_][2],
                                                                                     data[_][3],
                                                                                     data[_][4],
                                                                                     data[_][5],
                                                                                     data[_][6],
                                                                                     data[_][7],
                                                                                     data[_][8],
                                                                                     labels[_]))
            f.writelines(rewrite_lines)
