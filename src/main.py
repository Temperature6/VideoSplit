import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import winfunction
import videoprocess
import time

# 全局变量
win_w = 500
win_h = 400
default_path = winfunction.desk_path
file_path = ''
default_dir = winfunction.desk_path
dir_path = ''
supported_type = [("MP4视频", ".mp4")]
video_w = 0
video_h = 0
video_f = 0
finished = False

# 窗体
win = tk.Tk()
winfunction.center(win, win_w, win_h)
win.title("视频逐帧分割")


def show(text):
    info_lb.insert(END, text)
    info_lb.see(END)


def update_pb():
    if finished:
        pb["value"] = 0
        win.update()
        return


def start(exit_=False):
    update_pb()
    global finished
    if path_v.get() == '':
        path_in.focus()
        return
    elif out_v.get() == '':
        out_in.focus()
    elif file_type.get() == '':
        file_type.set(".jpg")

    vw = v_width.get()
    vh = v_height.get()
    vf = v_frames.get()
    pb['maximum'] = vf

    show("正在处理视频...")
    finished = False
    s = time.time()
    videoprocess.split_video(win, pb, path_v.get(), out_v.get(), file_type.get(), vw, vh, vf)
    e = time.time()
    finished = True
    if (exit_):
        sys.exit(0)
    else:
        show("处理完成，用时 {0} 秒".format(round(e - s, 2)))
        pb["value"] = 0
        win.update()
    return


# 视频路径输入
def path_button_click(h=True, auto_run=False):
    global file_path, path_v, video_f, video_h, video_w, default_path
    update_pb()
    if h:
        file_path = winfunction.open_file("打开视频文件", default_path, supported_type)
        if file_path == '':
            return
    default_path = winfunction.local_dir(file_path)
    path_v.set(file_path)
    info_lb.insert(END, "视频文件:{0}".format(file_path))
    show("正在读取视频信息...")
    try:
        data = videoprocess.check(file_path)
        video_w = data[0]
        video_h = data[1]
        video_f = data[2]
        show("原视频->宽：{0} 像素".format(video_w))
        show("原视频->高：{0} 像素".format(video_h))
        show("原视频->总帧数：{0} 帧".format(video_f))
        v_width.set(video_w)
        v_height.set(video_h)
        v_frames.set(video_f)
        show("完成")
        if auto_run:
            start(True)
    except Exception:
        show("出现问题")


tk.Label(win, text="视频路径", font=('', 14)).place(x=2, y=20)
path_v = tk.StringVar()
path_in = tk.Entry(win, textvariable=path_v,
                   highlightcolor='LightBlue',
                   highlightthickness=2, width=40)
path_in.place(x=90, y=20)
path_in.focus()
ttk.Button(win, text="打开文件", command=lambda: path_button_click()).place(x=400, y=20)


# 输出文件夹输入
def dir_button_click():
    update_pb()
    global dir_path, out_v, default_dir
    dir_path = winfunction.open_directory("选择输出文件夹", default_dir)
    if dir_path == "":
        return
    elif winfunction.check_contain_chinese(dir_path):
        tk.messagebox.showerror("错误", "输出路径中不能包含中文")
        out_in.focus()
        return
    default_dir = winfunction.local_dir(dir_path)
    out_v.set(dir_path)
    show("输出路径:{0}".format(dir_path))


tk.Label(win, text="输出位置", font=('', 14)).place(x=2, y=65)
out_v = tk.StringVar()
out_in = tk.Entry(win, textvariable=out_v,
                  highlightcolor='LightBlue',
                  highlightthickness=2, width=40)
out_in.place(x=90, y=65)
ttk.Button(win, text="打开目录", command=lambda: dir_button_click()).place(x=400, y=65)

# 视频信息
tk.LabelFrame(win, text="视频信息", height=70, width=490).place(x=5, y=100)  # 框
tk.Label(win, text="宽", font=('', 14)).place(x=8, y=125)
tk.Label(win, text="高", font=('', 14)).place(x=120, y=125)
tk.Label(win, text="导出帧数", font=('', 14)).place(x=230, y=125)
v_width = tk.IntVar()
v_height = tk.IntVar()
v_frames = tk.IntVar()
tk.Entry(win, textvariable=v_width, highlightcolor='LightBlue', highlightthickness=2, width=10).place(x=40, y=125)
tk.Entry(win, textvariable=v_height, highlightcolor='LightBlue', highlightthickness=2, width=10).place(x=150, y=125)
tk.Entry(win, textvariable=v_frames, highlightcolor='LightBlue', highlightthickness=2, width=10).place(x=320, y=125)

# 文件类型
file_type = tk.StringVar()
type_com = ttk.Combobox(win, textvariable=file_type, width=5)
type_com["value"] = [".jpg", ".png", ".bmp"]
type_com.current(0)
type_com.place(x=420, y=125)

# 进度条
pb = ttk.Progressbar(win, orient="horizontal", length=380, mode="determinate")
pb.place(x=5, y=180)

# 开始按钮


start_button = ttk.Button(win, text="开始", command=lambda: start()).place(x=400, y=178)


# 信息栏
def print_start_info():
    info_lb.insert(END, "Hi!   :)")
    info_lb.insert(END, "GitHub链接:https://github.com/Temperature6/VideoSplit")
    info_lb.insert(END, "—————————————————————————————")


info_frame = tk.Frame(win, width=500, height=200)
info_frame.place(x=0, y=220)
sby = tk.Scrollbar(info_frame)
sby.pack(side=LEFT, ipady=60)
sbx = tk.Scrollbar(info_frame, orient=HORIZONTAL)
sbx.pack(side=BOTTOM, ipadx=215)
info_lb = tk.Listbox(info_frame,
                     yscrollcommand=sby.set,
                     xscrollcommand=sbx.set,
                     width=65, height=8)
sby.config(command=info_lb.yview)
sbx.config(command=info_lb.xview)
info_lb.pack(side=LEFT)
info_lb.see(END)

print_start_info()

try:
    if len(sys.argv) == 2:
        p = sys.argv[1]
        file_path = p
        path_v.set(p)
        path_button_click(False)
    elif len(sys.argv) > 2:
        file_path = sys.argv[1]
        path_v.set(file_path)
        out_v.set(sys.argv[2])
        path_button_click(False, True)
except IndexError:
    pass
win.mainloop()
