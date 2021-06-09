# 视频逐帧分割

### 用于将视频逐帧分割的程序

​	运行时把三个.py文件放在同一目录下然后打开“mainwindow.py”

### 用到的库

​	main.py

​		tkinter：GUI界面（自带）

​		time：计时（自带）

​	winfunction.py

​		tkinter：GUI界面（自带）

​		os：获取桌面路径（自带）

​	videoprocess.py

​		OpenCV(cv2)：处理视频（自行安装）

### 更新日志

​	2021/06/08 - v1.0.0 - 第一个可用的版本

​	2021/06/09 - v1.1.0 - 添加了命令行参数，可以通过拖曳文件到“main.py”上的方式快速打开视频文件，你也可以使用pyinstaller将“main.py”打包成exe文件，仍可进行文件拖拽

​		