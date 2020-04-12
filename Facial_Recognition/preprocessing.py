import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import sys

#Set source image directory
directory = "./Data_processing/{}".format(sys.argv[1])

#The desired save location and name of subject for training
try:
    os.mkdir(directory+'_processed')
except: 
    print('A directory for the same class already exists, this will overwrite it.')
    
saveDirectory = directory+'_processed'


#for face identification statistics 
i,j=0,0


#face extraction (identification + segmentation) 
def extract_face(filename, required_size=(224, 224)):
    # load image from file
    pixels = cv2.imread(filename)  # le parmètre entré estun fichier image
    #image already in target size, probably face already extracted 
    if np.shape(pixels)==(224,224,3):
        face_array=pixels[:,:,::-1]
        return face_array
    
    # create the detector, using default weights
    detector = MTCNN()
    
    # detect faces in the image
    results = detector.detect_faces(pixels)
    #face could not be detected
    if results == []:
        return(results)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = np.asarray(image)
    face_array=face_array[:,:,::-1]
    return face_array



for filename in os.listdir(directory):
    #Only use .jpg and .png files
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".JPG"):
        #Set image path to be the path to the image file
        imagePath = directory +'/' + filename
    else:
        continue    

    #Read the jth image
    j+=1
    
    #progress line 
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*j, (j/len( os.listdir(directory))*100))
    sys.stdout.flush()
    
    try :
        image = extract_face(imagePath)
        #a face was detected
        if image != [] :
            image = np.asarray(image, dtype=np.float32)
            saveName = saveDirectory + "/" + filename
            cv2.imwrite(saveName, image[:, :, ::-1])

        #ith face extractionsuccess 
        i+=1

    except:
        print(' an error was thrown. ') 

print('operation completed')
print("{} faces extracted out of {} images. ". format(i,j))