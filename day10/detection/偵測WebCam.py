import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
# 眼睛特徵檔
# eye_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_eye.xml')  # 無戴眼鏡
eye_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_eye_tree_eyeglasses.xml')  # 有戴眼鏡

# 設定 Webcam
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    print(ret, frame)
    # 灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 偵測臉部, 得到臉部區域座標與長寬(x, y, w, h)
    faces = face_cascade.detectMultiScale(
        gray,  # 待偵測圖片
        scaleFactor=1.1,  # 檢測粒度(數字越小越精準(但速度慢), 反之數字越大越模糊(速度快))
        minNeighbors=15,  # 檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
        minSize=(30, 30),  # 搜尋比對最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型
    )
    # 在 face 周圍畫上矩形
    for (x, y, w, h) in faces:
        # 參數: frame, 左上角座標, 右下角座標, BGR色碼, 框線的寬度
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 繪文字
        cv2.putText(frame, 'Vincent', (x, y-7), 16, 1.2, (255, 0, 0), 2)

        # 在 face 內進行眼部偵測
        roi_color = frame[y:y + h, x:x + w]  # 人臉區域-彩色(y, x)
        roi_gray = gray[y:y + h, x:x + w]  # 人臉區域-灰階(y, x)
        # 眼睛偵測
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # 眼睛繪製
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # 將 frame 顯示
    cv2.imshow('Detect face', frame)

    # 按下 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()

