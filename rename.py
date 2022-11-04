# rename
import os
import glob
from PIL import Image, ImageFilter
import argparse


'''
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", help="the path of files to be renamed")
parser.add_argument("--start_num", help="start number of name")
parser.add_argument("--prefix", help="prefix of new file name")
parser.add_argument("--suffix", help="suffix of old file name")
args = parser.parse_args()
'''

path = '/home/demachilab/extra_launcher/'
start_num = 366
prefix = 'launcher'
suffix = '.jpg'


files=glob.glob(path + "*" + suffix)
print('files name: ', files)
file_indexs = [a for a in range(0,len(files))]

# index = 0
# num = 0


for index in file_indexs:
    new_name = path + prefix + "-"+str(int(start_num)+index) + suffix
    print("processing file: {0}".format(new_name))
    
    os.rename(files[index], new_name)

