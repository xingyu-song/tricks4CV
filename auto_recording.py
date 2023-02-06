# auto_recording.py
# recording the animation action automaticaly
from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from pynput import keyboard
import threading
import time
import os
import sys
import math
import pyautogui
import pydirectinput
import linecache
import tqdm

def change_screen_to_game():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    time.sleep(0.01)
    pyautogui.keyUp('alt')
    time.sleep(0.01)

def play_animation():
    pydirectinput.keyDown('enter')
    time.sleep(0.00005)
    pydirectinput.keyUp('enter')


def screen_record(record_time, path):
    """
    recording screen in a specific time
    record_time: video time
    path: path of saving video
    """

    flag=False # flag for stop recording  
    screen = ImageGrab.grab()  
    h, w = screen.size  
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  
    video = cv2.VideoWriter(path, fourcc, 20, (h, w))  
    start = time.time()
    while True:
        frame = ImageGrab.grab()
        frame =cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
        video.write(frame)
        now = time.time()
        print(now-start)
        if now-start >= record_time:
            print("Recording finish")
            break
    video.release()


 
if __name__=='__main__':
    change_screen_to_game()

    dir = 'C:/FMServer/cfx-server-data-master/videos'
    for i in range(1876, 40000):
        play_animation()
        if os.path.exists(r'C:\FMServer\cfx-server-data-master\animation_lists\text.txt'):
            animations = open(r'C:\FMServer\cfx-server-data-master\animation_lists\text.txt', 'r')
        else:
            continue
        line = animations.readline().strip()
        # line = linecache.getline(r'C:\FMServer\cfx-server-data-master\animation_lists\text.txt', 1).strip()
        info = line.split(' ')

        dict = info[0]
        anim = info[1]
        duration = float(info[2])
        name = dict + '_' + anim + '.mp4'
        path = dir + '/' + name
        play_animation()
        screen_record(duration, path)


        animations.close()

        os.remove(r'C:\FMServer\cfx-server-data-master\animation_lists\text.txt')
        # open(r'C:\FMServer\cfx-server-data-master\animation_lists\text.txt', 'w').close()
        print(i, 'finished')

        pydirectinput.keyDown('down')
        time.sleep(0.00005)
        pydirectinput.keyUp('down')
