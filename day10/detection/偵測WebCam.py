import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')

# 設定 Webcam
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    print(ret, frame)
    # 將 frame 顯示
    cv2.imshow('Detect face', frame)

    # 按下 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()

