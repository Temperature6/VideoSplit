from tkinter import filedialog
import os

desk_path = os.path.join(os.path.expanduser('~'), "Desktop")


def center(win_name, ww, wh, fixed=True):
    """
    用于使窗体居中
    :param win_name: 窗体名称
    :param ww: 设置窗体宽度
    :param wh: 设置窗体高度
    :param fixed: 固定窗体大小
    :return: 无返回值
    """
    sw = win_name.winfo_screenwidth()
    sh = win_name.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (ww, wh, (sw - ww) / 2, (sh - wh) / 2)
    win_name.geometry(alignstr)

    if fixed:
        win_name.resizable(0, 0)
    return


def open_file(title, path, file_type):
    """
    用于打开文件的函数
    :param title: 文件对话框标题
    :param path: 默认打开路径
    :param file_type: 支持的文件类型
    :return:返回打开的文件路径
    """
    o_path = filedialog.askopenfilename(title=title,
                                        filetypes=file_type,
                                        initialdir=path)
    return o_path


def open_directory(title, path):
    """
    打开目录
    :param title:对话框标题
    :param path:打开路径
    :return:返回打开的路径
    """
    o_dir = filedialog.askdirectory(title=title, initialdir=path)
    return o_dir


def local_dir(path):
    for x in range(len(path) - 1, 0, -1):
        if path[x] == '\\' or path[x] == '/':
            return path[0:x]


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
