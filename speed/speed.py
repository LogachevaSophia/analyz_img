
import os
import sys
import matplotlib.pyplot as plt
import cv2
from PIL import Image


sys.path.insert(1,os.path.join(sys.path[0],'..'))
from frame.frame import main as frame_main

def inputSourceVideo():
    return 'D:/analyz_img/source/video/video.mp4'
# input();



# def main():
#     SourceVideo = inputSourceVideo();
#     frame_main(SourceVideo);
#     pictures = os.listdir('./source/frames')
#     pictures = sorted(pictures)
#     # Создадим фигуру размером 16 на 4 дюйма
#     pic_box = plt.figure(figsize=(20,4))
#     for i, picture in enumerate(pictures):
#     # считываем изображение в picture
#         picture = cv2.imread('./source/frames/' + picture)
#     # конвертируем BGR изображение в RGB
#         picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
#     # добавляем ячейку в pix_box для вывода текущего изображения
#         pic_box.add_subplot(1,12,i+1)
#         plt.imshow(picture)
#     # отключаем отображение осей
#         plt.axis('off')
#     plt.show()    
def main():
    SourceVideo = inputSourceVideo();
    a = frame_main(SourceVideo); 
    seconds = a['seconds'];
    fps = a['fps'];
    img1 = Image.open(r"./source/frames/frame0.jpg");
    img2 = Image.open(r"./source/frames/frame2.jpg");
    
    intermediate = Image.alpha_composite(img1,img2);
                   
    
    
main()
    