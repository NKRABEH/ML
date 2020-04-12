from PIL import Image 
import os
import sys

#rotation angle
angle = int(sys.argv[2])
class_directory = './Data_processing/{}'.format(sys.argv[1])
file_names = os.listdir(class_directory)
for file in file_names:
    if file.endswith('.jpg') or file.endswith('.png') : 
        file_name = class_directory + '/' + file
        image=Image.open(file_name)
        image = image.rotate(angle)
        image.save(file_name)
        
print('operation completed') 