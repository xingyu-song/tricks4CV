# show mAP
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import json

# define lists
bbox_mAP = []
bbox_mAP_50 = []
bbox_mAP_75 = []
bbox_mAP_s = []
bbox_mAP_m = []
bbox_mAP_l = []

loss = []
loss_cls = []
loss_bbox = []
loss_obj = []

# read json file
with open('/home/demachilab/mmdetection-master/checkpoints/yolox/yolox_s_8x8_700e_orginal3cls/20220901_232029.log.json') as f:
    for line in f.readlines():
        line = json.loads(line)
        
        '''
        if 'loss_cls' in line:
            loss.append(line['loss'])
            loss_cls.append(line['loss_cls'])
            loss_bbox.append(line['loss_bbox'])
            loss_obj.append(line['loss_obj'])

        '''
        if 'bbox_mAP' in line:
            bbox_mAP.append(line['bbox_mAP'])
            bbox_mAP_50.append(line['bbox_mAP_50'])
            bbox_mAP_75.append(line['bbox_mAP_75'])
            bbox_mAP_l.append(line['bbox_mAP_l'])
            bbox_mAP_m.append(line['bbox_mAP_m'])
            bbox_mAP_s.append(line['bbox_mAP_s'])

        
    epoch = line['epoch']

# define plot


plt.plot(bbox_mAP, label = 'bbox_mAP')
plt.plot(bbox_mAP_50, label = 'bbox_mAP_50')
plt.plot(bbox_mAP_75, label = 'bbox_mAP_75')
plt.plot(bbox_mAP_l, label = 'bbox_mAP_l')
plt.plot(bbox_mAP_m, label = 'bbox_mAP_m')
plt.plot(bbox_mAP_s, label = 'bbox_mAP_s')
'''

plt.plot(loss, label='loss')
plt.plot(loss_cls, label='loss_cls')
plt.plot(loss_bbox, label='loss_bbox')
plt.plot(loss_obj, label='loss_obj')
'''

plt.xlabel('Epoch', fontdict={'size': 16})
plt.xticks(size=16)
plt.yticks(size=16)
plt.ylabel('mAP', fontdict={'size': 16})
plt.xlim(0, 450)
plt.legend(loc='upper right')

plt.show()



