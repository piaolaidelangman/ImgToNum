# 图片转为数字显示  
## 一、思路 
——1.先是每个图片，读取为灰度图，0-255映射为0-9，通过/26  
——2.通过 ```print()``` 输出到控制台，然后通过 ```os.system('cls')``` 清空控制台，为下一张图片做准备

## ffmpeg处理视频命令  
——1. 从指定时间开始剪切t秒  
ffmpeg -ss 00:00:30 -t 600 -i src.mp4  -codec copy out.mp4   
ffmpeg -ss 00:01:00 -t 120 -i 青春期猪头少年不做怀梦少女的梦.mkv  -codec copy out.mp4  
——2. 从(x,y)开始裁剪(w,h)的画面  
ffmpeg -i in.mp4 -vf crop=w:h:x:y out.mp4  
ffmpeg -i new.mp4 -vf crop=640:480:0:0 newout.mp4  

## 20210814 七夕更新  
### 已实现：
  可通过摄像头和视频文件两种方式使用  
  采用了最大池化和均值两种方式处理图像
  ![image text](https://github.com/piaolaidelangman/ImgToNum/raw/main/result.jpg)
### 未实现：
  任何分辨率图片自动压缩到120*160
  更精确的显示