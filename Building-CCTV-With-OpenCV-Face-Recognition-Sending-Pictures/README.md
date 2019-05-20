# Building CCTV With OpenCV Face Recognition Sending Pictures

English Version.(中文版本请下拉)

Use Socket for information transmission.

The *send.py* and *receive.py* annotations are already exhaustive, see the annotations for their principles.

First, put the [receiver script](./receive.py) on the server side. Open the terminal and enter the following command:

```sh
python3 receive.py
```

Run the program.

If the program is executed correctly, in the first line of execution, you will see the following information:

***当前服务器ip地址为: xxx.xxx.xxx.xxx, 接收服务端口号为: xxxx***

Please note the IP address and port number and keep the program running.

-----------------------------------------------------------------------------------------------

Please put *send.py* and *Train.xml* in the same folder and on the client side with the camera.

After properly configuring the IP and port of the [client script](send.py), open the terminal and enter the following command:

```sh
python3 send.py
```

After capturing the face, the program will take a screen shot, save the picture as *camera.png*, and send it to the server.

# opencv智能识别人脸并截图转发

使用Socket进行信息传输。

*send.py*和*receive.py*注释已经很详尽，请参见注释了解其原理。

首先请将[接收端脚本](./receive.py)放在服务器端。打开终端，输入以下命令：

```sh
python3 receive.py
```

运行程序。

如果程序正确执行，那么在程序执行的第一行，你将会看到以下信息:

***当前服务器ip地址为: xxx.xxx.xxx.xxx, 接收服务端口号为: xxxx***

请记下ip地址和端口号，并保持程序一直运行。

-----------------------------------------------------------------

请将*send.py*和*Train.xml*放在同一个文件夹下，放在装有摄像头的客户端。

在正确配置[客户端脚本](send.py)的ip和端口后，打开终端，输入以下命令：

```sh
python3 send.py
```

程序会在捕获到人脸后，将其截屏，图片保存为*camera.png*, 并发送到服务器上。