# -*- coding=utf-8 -*-

# 导入库 Import Library
import socket
import os
import sys
import struct
import cv2
import numpy as np


def get_pic():


    # 调用摄像头 Call Camera
    cap = cv2.VideoCapture(0)
    # 人脸识别器分类器 Train.xml为模型 Face Recognizer Classifier Train.xml as the training model
    classfier = cv2.CascadeClassifier("Train.xml")
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        # 灰度转换 Grayscale transformation
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，scaleFactor和minNeighbors分别为图片缩放比例和需要检测的有效点数 
        # Face detection, scaleFactor and minNeighbors are the scaling ratio of images and the number of valid points to be detected, respectively.
        faceRects = classfier.detectMultiScale(
            grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        cv2.imshow("Camera", frame)
        if len(faceRects) > 0:  # 大于0则检测到人脸 Face Detected When More than 0
            print("检测到人脸！")
            cv2.imwrite("./camera.png", frame)  # 保存路径 Saved path
            print("成功将图片保存到camera.png")
            cap.release()
            break
        # 设定每1ms获取摄像头的图片一次 Set up to capture the camera image once per ms
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def socket_client():
    try:
        # socket参数配置 Parameter configuration
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 8008)) # 在这里填入正确的ip 和端口号 fill in correct ip and port number here  
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        filepath = "./camera.png"
        if os.path.isfile(filepath):
            # 发送文件名和大小信息(这里废弃文件的其它属性) Send file name and size information (other properties of  files are discarded here)
            # 128si: 定义这些信息由128位长度字符串和int数字组成 128si: Defines that this information consists of 128-bit length strings and interger
            # 打包数据 Pack data
            fhead = struct.pack('128si', os.path.basename(
                filepath).encode('utf-8'), os.stat(filepath).st_size)
            s.send(fhead)
            print("正在将路径为 {0} 的文件发送到服务器......".format(filepath))

            fp = open(filepath, 'rb')
            while True:
                data = fp.read(1024)
                if not data:
                    print('文件 {0} 发送完毕...'.format(os.path.basename(filepath)))
                    break
                s.send(data)
        s.close()
        break


if __name__ == '__main__':
    get_pic()
    socket_client()
