# change_resolution.py
# change the resolution of videos

import cv2, os
import shutil
from tqdm import tqdm

# input directory, output directory and output video type
# directory where the video file located 
input_dir = '/mnt/data/testing/ISCN_20220708_v2/7' # input file directory
output_dir = '/mnt/data/testing/ISCN_20220708_v2/1080/7' # output file directory 
output_type = '.avi' # output file type

# list all video files in the input path
dirs = os.listdir(input_dir) 

# every video files in dirs
for dir in dirs:
    file_dir_d = input_dir + "/" + str(dir)
    #print(file_dir_d)
    files = os.listdir(file_dir_d) # all files 
    #print(files)
    out = output_dir + '/' + dir # output folders
    if not os.path.exists(out):
        os.makedirs(out)
    
    # every file in folders
    for file in files:
        file_dir_e = file_dir_d + "/" + str(file)
        print('input: ', file_dir_e)
        file_n = os.path.splitext(file_dir_e)[0]
        filename = file_n.split('/')
        output = out + '/' + filename[-1] + output_type
        print('output: ', output)
        
        # video property 
        cap = cv2.VideoCapture(file_dir_e)
        fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #duration = frame_count / fps
        print(
            'fps:', fps, '\n'
            'height*width:', height, '*', width, '\n'
            'frame_count:', frame_count, '\n'
            #'duration:', duration
            )

        if height == 1080:
            shutil.move(file_dir_e, output)
        else: 
            # convert video
            success, _ = cap.read()
            if output_type == '.mp4':
                fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
            else:
                fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
            videowriter = cv2.VideoWriter(output, fourcc, 30, (1080,1920)) # 2k: 2048x1080 1080: 1920x1080 720p: 1280x720
            print('resizing ', file_n)
            with tqdm() as pbar:
                while success:
                    pbar.update()
                    success, img1 = cap.read()
                    try:
                        img1 = cv2.flip(img1, 0)
                        img1 = cv2.flip(img1, 180)
                        img = cv2.resize(img1, (1080,1920), interpolation=cv2.INTER_LINEAR) 
                        videowriter.write(img)
                    except:
                        break
            
            
    
