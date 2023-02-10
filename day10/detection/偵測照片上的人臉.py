'''
安裝 OpenCV 步驟
一、安裝 PIL :
pip install pillow

二、安裝 py-opencv :
安裝:
pip install opencv-python
pip install opencv-contrib-python
'''
import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
print(face_cascade)

# 讀影像檔
frame = cv2.imread('../sample_image/test.jpg')
print(frame)



