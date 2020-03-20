import pandas as pd
import matplotlib.pyplot as plt


def read_csv(path):
    csv_file = pd.read_csv(path, header=None)
    return csv_file


def clean(csv_file, flag=False):
    if flag:
        # 取10列
        csv_file = csv_file[csv_file.columns.values[0:10]]
        # label 列置零
        csv_file[csv_file.columns.values[0]] = 0
        print(csv_file.columns.values)

    return csv_file


def show_plot_save(csv_file, out_path, header=False, style=0):

    labels, x, y, z = csv_file[0], csv_file[1], csv_file[2], csv_file[3]

    # print(plt.style.available)
    # plt.style.use('bmh')

    fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    vertical_line = plt.axvline(x=0, color='purple', ls='--')
    horizontal_line = plt.axhline(y=0, color='purple', ls='--')

    def update_labels_line(_labels_line, _labels, style):
        _new_x = [i for i in range(len(_labels)) if _labels[i] == style]
        _labels_line.set_xdata(_new_x)
        _labels_line.set_ydata([15 for _ in range(len(_new_x))])
        fig.canvas.draw_idle()

    if style == 1:
        labels_line = plt.plot([], [], 's', color='orange')[0]
    elif style == 2:
        labels_line = plt.plot([], [], 's', color='blue')[0]
    elif style == 3:
        labels_line = plt.plot([], [], 's', color='purple')[0]
    elif style == 4:
        labels_line = plt.plot([], [], 's', color='slategrey')[0]
    update_labels_line(labels_line, labels, style)

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

    csv_file.to_csv(out_path, index=False, header=header)


if __name__ == '__main__':

    # 0:unknown
    # 1:freestyle
    # 2:breaststroke
    # 3:butterfly
    # 4:backstroke
    swim_style = 1
    # style_team_hand_00.csv
    # input_path = '../data/processed/train_2/4/backstroke_4_right_01.csv'
    # output_path = '../data/processed/train_1_V2/freestyle_team2_right_19.csv'
    valid_path = r'../data/valid_data/freestyle_team1_right_05.csv'
    #
    data = read_csv(valid_path)
    # clean option
    clean_flag = False
    data = clean(data, clean_flag)

    show_plot_save(data, valid_path, clean_flag, swim_style)
