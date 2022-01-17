from cv2 import VideoCapture
from cv2 import CAP_PROP_FRAME_COUNT
from cv2 import cvtColor
from cv2 import IMREAD_COLOR
from cv2 import resize
from cv2 import imwrite


def check(path):
    data = [0, 0, 0]
    video = VideoCapture(path)
    data[0] = video.get(3)  # 宽
    data[1] = video.get(4)  # 高
    data[2] = int(video.get(CAP_PROP_FRAME_COUNT))  # 总帧数
    return data


def split_video(win, pb, video_path, save_path, file_type, vw, vh, vf):
    video = VideoCapture(video_path)
    n = len(str(vf)) + 1
    pic_size = (vw, vh)
    count = 0

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        gray = cvtColor(frame, IMREAD_COLOR)
        r_size = resize(gray, pic_size)
        _save_path = save_path + '/' + str(count).zfill(n) + file_type
        imwrite(_save_path, r_size)
        count += 1
        pb["value"] = count
        win.update()
        if count >= vf + 1:
            break
    return
