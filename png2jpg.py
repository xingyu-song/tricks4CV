from PIL import Image, ImageFilter
for num in range(4,260):
    im = Image.open('/home/demachilab/Downloads/wirecutter_origin/wirecutter-' + str(num)+'.jpg')
    if im.mode != 'RGB':
        im = im.convert('RGB')
        im.save('/home/demachilab/Downloads/wirecutter_origin/wirecutter-' + str(num)+'.jpg', quality=95)
    print(num, im.format, im.size, im.mode)

