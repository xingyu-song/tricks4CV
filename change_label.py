import json 
import os
input_dir = '/mnt/data/labelme'

files = os.listdir(input_dir)

for file in files:
    if file.split('.')[-1] == 'json':
        file_path = input_dir + '/' + file
        f = open(file_path)
        data = json.load(f)
        f.close()
        i = 0
        for shape in data['shapes']:
            label = shape['label']
            
            if label == 'person':
                print(data['imagePath'])
                data['shapes'][i]['label'] = 'human'
                with open(file_path, 'w') as r:
                    json.dump(data, r)
                r.close()
            i += 1
            
