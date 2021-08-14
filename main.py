# coding=utf-8
import numpy as np
import cv2
import time
import os
#像素映射到字符输出
# pix=('.','1','2','3','4','5','6','7','8','9','*','&','^','+','=','%','$','#','@','0')
# pix=('.','1','^','+','4','%','=','#','8','*','0','&','2','3','6','5','$','7','@','9')
pix=('`','.','"','~','^','/','o','1','+','2','i','c','x','*','#','8','m','9','@')

Compression_Ratio_X=4   #纵向压缩
Compression_Ratio_Y=8   #横向压缩
num_show_char=3         #每个像素显示次数
char_num=26
picnum=0
def img_to_char(img):
    # img = cv2.resize(img, (72,96))
    # print(np.shape(img))
    # return 
    height, width = np.shape(img)
    # global picnum
    # # picnum=0
    # # img=img.swapaxes(0,1)
    # if picnum<10:
    #     cv2.imwrite('movie/'+str(picnum)+'.jpg',np.array(img))
    #     picnum+=1
    show_str=''
    for i in range(0,height):
        if i>80:
            break
        for j in range(0,width):
            img[i][j] = img[i][j]/char_num
        show_str=''
        for j in range(0,width):
            for k in range(num_show_char):
                show_str+=pix[int(img[i][j])]
            # print(pix[19-img[i][j]],end='')   #倒转  
            # print(pix[int(img[i][j])]+pix[int(img[i][j])],end='')     #双倍
            # print(pix[int(img[i][j])]+pix[int(img[i][j])]+pix[int(img[i][j])],end='')
        print(show_str)
            # print(chr(img[i][j]),end='')
    time.sleep(0.1)
    # os.system('cls')

def zip_pic_maxpooling(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #480 640
    height, width = np.shape(img)
    new_img=[]

    i=0
    while i<height:
        row=[]
        j=0
        while j<width:
            pix=0
            for k in range(0,Compression_Ratio_X-1):
                for m in range(0,Compression_Ratio_Y-1):
                    if i+k<height and j+m<width:
                        pix=max(pix,img[i+k][j+m])
            row.append(int(pix))
            j+=Compression_Ratio_Y
        if len(row)>0:
            new_img.append(row)
        i+=Compression_Ratio_X
    return new_img

def zip_pic_mean(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #480 640
    height, width = np.shape(img)
    new_img=[]
    # global picnum
    # if picnum<10:
    #     cv2.imwrite('movie/'+str(picnum*10)+'.jpg',np.array(img))
    #     picnum+=1
    i=0
    while i<height:
        row=[]
        j=0
        while j<width:
            pix=0
            num=0
            for k in range(0,Compression_Ratio_X-1):
                for m in range(0,Compression_Ratio_Y-1):
                    if i+k<height and j+m<width:
                        pix+=img[i+k][j+m]
                        num+=1
            row.append(int(pix/num))
            j+=Compression_Ratio_Y
        if len(row)>0:
            new_img.append(row)
        i+=Compression_Ratio_X
    print(np.shape(new_img))
    return new_img

def open_by_camera():
    # 默认情况下得到的值是 640X480。
    # 但是我可以使用 ret=cap.set(3,320)和 ret=cap.set(4,240) 来把宽和高改成 320X240。
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)#摄像头
    i=0
    ######################################################################
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            # img_to_char(frame)
            # img_to_char(zip_pic_maxpooling(frame))
            img_to_char(zip_pic_mean(frame))

            # cv2.imwrite('capture/'+str(i)+'.jpg',frame)
            i=i+1
        else:
            break
    cap.release()
def open_by_file():
    ##读取视频文件
    videoCapture = cv2.VideoCapture("newout.mp4")#1080 1920  
    # videoCapture = cv2.VideoCapture("movie.mp4")# 720 960
    #读帧
    success, img = videoCapture.read()
    i = 0
    while success and i<1000:
        i = i + 1
        # 处理每一帧图片
        img_to_char(zip_pic_maxpooling(img))
        success, img = videoCapture.read()

if __name__ == '__main__':
    open_by_camera()
    # open_by_file()






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