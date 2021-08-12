# 图片转为数字显示  
## 一、思路 
——1.先是每个图片，读取为灰度图，0-255映射为0-9，通过/26  
——2.通过 ```print()``` 输出到控制台，然后通过 ```os.system('cls')``` 清空控制台，为下一张图片做准备

ffmpeg -ss 00:00:30 -t 600 -i src.mp4  -codec copy out.mp4  
ffmpeg -ss 00:01:00 -t 120 -i 青春期猪头少年不做怀梦少女的梦.mkv  -codec copy out.mp4

ffmpeg -ss 00:00:04  -i out.mp4  -codec copy new.mp4