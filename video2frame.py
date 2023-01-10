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
    input_action_file = input_path + '/' + dir # ./climb, ./cut, ./launcher
    output_action_file = output_path + '/' + dir 
    video_files = os.listdir(input_action_file) # all videos for the action
    
    for file in video_files:
        video_name = file.split('.')[0]
        input_file = input_action_file + '/' + file
        output_file = output_action_file + '/' + video_name
        print('segmenting:', video_name)
        print('input:', input_file)
        print('output:', output_file)

        if not os.path.exists(output_file):
            os.makedirs(output_file)

        cap = cv2.VideoCapture(input_file)
        success, _ = cap.read()    
        count = 1     
        with tqdm() as pbar:
            while success:
                pbar.update() 
                success, frame = cap.read()
                try:
                    out = output_file + '/' + str(int(count)) + '.jpg'
                    cv2.imwrite(out, frame)
                    count += 1
                except:
                    break

        
            cap.release()

sym = '/'
input_path = sym.join(input_path.split('/')[0:-1])
output_path = sym.join(output_path.split('/')[0:-1])




