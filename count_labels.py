import json 
import os
import pandas as pd
import matplotlib.pyplot as plt
input_dir = '/mnt/data/labelme'

files = os.listdir(input_dir)
class_num = 3
labels = []
for file in files:
    if file.split('.')[-1] == 'json':
        file_path = input_dir + '/' + file
        f = open(file_path)
        data = json.load(f)
        f.close()
        i = 0
        for shape in data['shapes']:
            label = shape['label']
            labels.append(label)

#print(labels)
res = pd.value_counts(labels)
print(res)
# res.head(3).plot.bar()
# plt.show()
#     for l in labels:
#         dict[l] = dict.get(l, 0) + 1

# print(dict)
# p1 = plt.bar(x, height=y1, width=0.3,label='image',tick_label=str1)
# p1 = plt.bar(x+bar_width, height=y2, width=0.3,label='bbox',tick_label=str1)

# plt.figure(num = 1)
# plt.legend()
# plt.title('class_status')

# plt.savefig('柱状统计图')

# #饼状图绘制
# plt.figure(num=2,figsize=(6,6))
# explode=[0.01,0.01,0.01,0.01,0.01]
# plt.pie(number_img,explode=explode,labels=str1,autopct='%1.1f%%')
# plt.title('image_numbers')
# plt.savefig('images统计饼状图')

# plt.figure(num=3,figsize=(6,6))
# explode=[0.01,0.01,0.01,0.01,0.01]
# plt.pie(number_bbox,explode=explode,labels=str1,autopct='%1.1f%%')
# plt.title('bbox_numbers')
# plt.savefig('bbox统计饼状图')

# plt.show()
