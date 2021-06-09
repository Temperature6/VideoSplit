from PIL import ImageGrab
import time

def shottime():
    data = time.time()
    timeArray = time.localtime(data)
    st_time = time.strftime('%Y%m%d%H%M%S', timeArray)
    return st_time


image = ImageGrab.grabclipboard() # 获取剪贴板文件
save_name = "PrtScr{0}".format(shottime()) + ".png"
image.save(save_name)
