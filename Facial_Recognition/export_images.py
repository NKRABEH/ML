import os 
import sys



data_size = len(os.listdir('./Data_processing/{}_processed'.format(sys.argv[1])))

try:
    os.mkdir('./Dataset/train/{}'.format(sys.argv[1]))
except:
    print('train directory for the same classe already exists, a risk of overwriting images with same filename.')
    
try:
    os.mkdir('./Dataset/validation/{}'.format(sys.argv[1]))
except:
    print('validation directory for the same classe already exists, a risk of overwriting images with same filename.')
             
             
             
i = 0
for file in os.listdir('./Data_processing/{}_processed'.format(sys.argv[1])) : 
    os.rename('./Data_processing/{}_processed/{}'.format(sys.argv[1], file), './Dataset/validation/{}/{}'.format(sys.argv[1],file))
    i+=1
    if i > data_size/ 6:
        break
os.rename('./Data_processing/{}_processed'.format(sys.argv[1]), './Dataset/train/{}'.format(sys.argv[1],file))