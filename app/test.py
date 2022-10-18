import cv2
import time
#获取摄像头
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#打开摄像头
cap.open(0)
while cap.isOpened():
    #获取画面
    flag, frame = cap.read()
 
    ######################画面处理1##########################
    #灰度图
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.medianBlur(frame, 5)
    img_blur = cv2.GaussianBlur(frame, ksize=(21, 21),
                                sigmaX=0, sigmaY=0)
    frame = cv2.divide(frame, img_blur, scale=255)
 
    #画面显示
    cv2.imshow('mytest', frame)
    #设置退出按钮
    key_pressed = cv2.waitKey(100)
    print('单机窗口，输入按键，电脑按键为',key_pressed,'按esc键结束')
    if key_pressed == 27:
        break
#关闭摄像头
cap.release()
#关闭图像窗口
cv2.destroyAllWindows()
time.sleep(10)