#преобразование видео в кадры


import cv2
import numpy as np
import os
import datetime
import math
from moviepy.editor import VideoFileClip


# try:
#     if not os.path.exists('./source/frames'):
#         os.makedirs('./source/frames')
# except OSError:
#     print('Error: Creating directory of /source/frames')


def main(video_file, count):
    try:
        if not os.path.exists('./source/frames'):
            os.makedirs('./source/frames')
    except OSError:
        print('Error: Creating directory of /source/frames')
    #count = int(input())
    data = cv2.VideoCapture(video_file)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = data.get(cv2.CAP_PROP_FPS)
    seconds = round(frames / fps)
    video_clip = VideoFileClip(video_file)
    saving_frames = math.ceil(count/seconds)
    print("seconds", seconds)
    print(saving_frames)
    step = 1/saving_frames
    
    part = 0
    for curren_duration in np.arange(0, video_clip.duration, step):
        name = './source/frames/frame' + str(part) + '.jpg'
        video_clip.save_frame(name, curren_duration)
        part += 1
    return {'seconds': seconds, 'fps': saving_frames}


# main('./source/video/video.mp4')
