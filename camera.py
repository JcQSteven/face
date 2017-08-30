# coding=utf-8
import cv2
import os
import time


def face_detect(img,photo):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#获取灰度
    cv2.equalizeHist(gray, gray)#灰度直方化
    face_cascade = cv2.CascadeClassifier('/Users/steven/Desktop/face/haarcascade_frontalface_alt.xml')#定义分类器

    faces = face_cascade.detectMultiScale(#脸部探测
        gray,

        scaleFactor=1.15,

        minNeighbors=5,

        minSize=(5, 5),

        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:#画长方图
        cv2.rectangle(img, (x - 50, y - 100), (x + w + 50, y + w + 50), (0, 255, 0), 2)
        #dim=(x+w+100,y+w+150)
        #resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

        if len(photo)==0:
            datetime = get_time()
            file_path = '/Users/steven/Desktop/face/cv/' + datetime + '.jpeg'
            cv2.imwrite(file_path, img)
            photo.append(file_path)
            print 'camera:', file_path

    return img


def camera(photo):
    cv2.namedWindow('camera', 1)
    # video = 'http://192.168.31.104:8081'
    capture = cv2.VideoCapture(0)
    num = 0
    while capture.isOpened():
        ret, frame = capture.read()
        new_frame = face_detect(frame,photo)
        cv2.imshow('camera', new_frame)
        key = cv2.waitKey(10)

        if key == 27:
            photo.append('1')
            print'esc break---'
            break

    capture.release()
    cv2.destroyWindow('camera')

def get_time():
    datetime=datetime = time.strftime('%Y%m%d%H%M%S')
    return datetime

def file_exsit(file_path):
    if os.path.exsits(file_path):
        return 1
    else:
        return 0