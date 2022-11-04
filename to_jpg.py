from ast import Num
from PIL import Image, ImageFilter
for num in range(0, 959):

    dir = '/mnt/data/google/cutter/' + str(num) + '.jpg'
    img = Image.open(dir).convert('RGB')