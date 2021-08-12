# coding=utf-8
import numpy as np
import cv2
import time
import os
#像素映射到字符输出
pix=('.','1','2','3','4','5','6','7','8','9','*','&','^','+','=','%','$','#','@','0')

def img_to_char(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize(img, (72,96))
    height, width = np.shape(img)

    # img=img.swapaxes(0,1)
    # # cv2.imwrite('movie/'+str(i)+'.jpg',img)
    # height, width = np.shape(img)

    for i in range(0,height):
        if i>60:
            break
        for j in range(0,width):
            img[i][j] = img[i][j]/13
        for j in range(0,width):

            # print(pix[19-img[i][j]],end='')
            print(pix[img[i][j]],end='')

            # print(chr(img[i][j]),end='')
            
        print()
    time.sleep(0.05)
    os.system('cls')


def open_by_camera():
    # 默认情况下得到的值是 640X480。
    # 但是我可以使用 ret=cap.set(3,320)和 ret=cap.set(4,240) 来把宽和高改成 320X240。
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 180)  #设置宽度
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 64)  #设置长度
    cap.set(3, 100)  #设置宽度
    cap.set(4, 32)  #设置长度
    i=0
    ######################################################################
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            img_to_char(frame)
            cv2.imwrite('capture/'+str(i)+'.jpg',frame)
            i=i+1
        else:
            break
    cap.release()
    # out.release()
def main():

    ###########测试
    # videoCapture = cv2.VideoCapture("new.mp4")#1080 1920  
    # videoCapture = cv2.VideoCapture("movie.mp4")# 720 960
    # videoCapture = cv2.VideoCapture(1)# 摄像头

    # #读帧
    # success, img = videoCapture.read()
    # i = 0
    # while success and i<1000:
    #     i = i + 1
    #     # 保存每一帧图片
    #     # print(type(img),np.shape(img))
    #     img_to_char(img)
    #     success, img = videoCapture.read()
    print()
if __name__ == '__main__':
    # main()
    open_by_camera()






'''
    print(cap.get(CV_CAP_PROP_FRAME_WIDTH))
    print(cap.get(CV_CAP_PROP_FRAME_HEIGHT))
    print(cap.get(CV_CAP_PROP_FPS))
    print(cap.get(CV_CAP_PROP_BRIGHTNESS))
    print(cap.get(CV_CAP_PROP_CONTRAST))
    print(cap.get(CV_CAP_PROP_SATURATION))
    print(cap.get(CV_CAP_PROP_HUE))
    print(cap.get(CV_CAP_PROP_EXPOSURE))
'''