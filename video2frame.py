from itertools import count
from re import I
from typing import Counter
import cv2
import os
from tqdm import tqdm



input_dir = '/mnt/data/2022_11_3'
output_dir = '/mnt/data/2022_11_3_frame'



dirs = os.listdir(input_dir) # climb, cut, launcher

for dir in dirs:
    input_action_file = input_dir + '/' + dir # ./climb, ./cut, ./launcher
    output_action_file = output_dir + '/' + dir 
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
input_dir = sym.join(input_dir.split('/')[0:-1])
output_dir = sym.join(output_dir.split('/')[0:-1])




