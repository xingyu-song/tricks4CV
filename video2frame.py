# video2frame.py
# convert video into frames

from itertools import count
from re import I
from typing import Counter
import cv2
import os
from tqdm import tqdm

# input path, output path and output video type

'''
directory structure:
input_path
├── action1
│   ├── video1_1.mp4
│   ├── video1_2.mp4
│   ├── ...
├── action2
│   ├── video2_1.mp4
│   ├── video2_2.mp4
│   ├── ...
├── ......
'''

# configuration
input_path = '/mnt/data/2022_11_3' # input path lead to the directory contains videos need to be convert
output_path = '/mnt/data/2022_11_3_frame' # output path

# list all directories of the input path
dirs = os.listdir(input_path) # climb, cut, launcher

# each directory in the directoy list 
for dir in dirs:
    # add the directory name into the input path
    input_dir_path = input_path + '/' + dir # path of input directories
    # add the directory name into the output path
    output_dir_path = output_path + '/' + dir # path of output directories
    # list all videos in the directroy
    videos_list = os.listdir(input_dir_path)
    
    # each video in the videos list
    for video in videos_list: # 'video' with extension filename
        # obtain the video name without extension (".mp4", ".avi")
        video_name = video.split('.')[0]
        # obtain the full path of input video file path ("xxx/xxx/dir_name/video_name.mp4")
        input_video_path = input_dir_path + '/' + video
        # obtain the folder contains frames of a video
        output_framefolder_path = output_dir_path + '/' + video_name
        
        print('segmenting:', video_name)
        print('input:', input_video_path)
        print('output:', output_framefolder_path)

        # create the folder of output frame if possible
        if not os.path.exists(output_framefolder_path):
            os.makedirs(output_framefolder_path)

        # capture the video from the path 
        cap = cv2.VideoCapture(input_video_path)
        # if captured successfully 
        success, _ = cap.read()    
        count = 1 # count of frame

        # initialize the progress bar
        with tqdm() as pbar: # progerss bar
            # captured successfully
            while success:
                pbar.update() 
                success, frame = cap.read()
                try:
                    # output the frames
                    out = output_framefolder_path + '/' + str(int(count)) + '.jpg'
                    # write into folders
                    cv2.imwrite(out, frame)
                    count += 1
                except:
                    break

        
            cap.release()

sym = '/'
input_path = sym.join(input_path.split('/')[0:-1])
output_path = sym.join(output_path.split('/')[0:-1])




