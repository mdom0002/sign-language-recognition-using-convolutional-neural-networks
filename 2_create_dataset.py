import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.

path='data'

IMG_SIZE = 96

def create_train_data():      #function header
    training_data = []        #declare empty array
    label=0
    for (dirpath,dirnames,filenames) in os.walk(path):         
        for dirname in dirnames:                                # for each directory name
            print(dirname)
            for(direcpath,direcnames,files) in os.walk(path+"/"+dirname):
                for file in files:                               #for each file in the directory
                        actual_path=path+"/"+dirname+"/"+file     #sets actual_path as path/dirctoryname/filename
                        print(files)
                        # label=label_img(dirname)
                        path1 =path+"/"+dirname+'/'+file
                        img=cv2.imread(path1,cv2.IMREAD_GRAYSCALE)  # greyscale of image with the specific path           
                        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))  #resize to 96 as initialized before
                        training_data.append([np.array(img),label])  #append the image and label(first case will be 0) to training_data array declared before
            label=label+1               #increment label value by 1
            print(label)
    shuffle(training_data)              #shuffle the array
    np.save('train_data.npy', training_data)   #save array to binary file in numpy format
    print(training_data)
    return training_data                      #return the array containing images and labels

create_train_data()                             #call the function
