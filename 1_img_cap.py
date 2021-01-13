# organize imports
import cv2
import numpy as np
import os

IMG_SIZE=96

# region of interest (ROI) coordinates  - a sample area within the area of an image - in this case, the green rectangle which you see in the camera
top, right, bottom, left = 100, 150, 400, 450    

exit_con='**'

a=''

dir0=input('enter the directory name : ')   #enter a directory name, means a folder name in our case eg: ImageProcessing

try:
    os.mkdir(dir0)       #make directory with the input name
except:
    print('contain folder in same name')   #if a folder already exists then print

# get the reference to the webcam
camera = cv2.VideoCapture(0)

while(True):

    a=input('exit: ** or enter the label name : ')  #insert the label name or input ** to exit

    if a==exit_con:       #if user input is **, break from the loop
        break

    dir1=str(dir0)+'/'+str(a)    #dir1 = directoryname given before as dir0 / label name given as a -basically makes a path- eg: ImageProcessing/Signs
    print(dir1)    

    try:
        os.mkdir(dir1)    #make directory - basically creates a folder with the label name inserted by user inside the directory input by the user
    except:
        print('contain folder')

    i=0   #i initialized as 0 which would be the name of the first jpg file

    while(True):
        (t, frame) = camera.read()

        

        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)

        # get the ROI  - ROI = image[y1:y2, x1:x2]
        roi = frame[top:bottom, right:left]

        # convert the roi to grayscale and blur it
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        #resize img
        gray = cv2.resize(gray, (IMG_SIZE,IMG_SIZE))

        #write img file to directory
        cv2.imwrite("%s/%s/%d.jpg"%(dir0,a,i),gray)   #write the image to %s/%s/%d.jpg which would be replaced by dir0/a/i.jpg - eg: ImageProcessing/Signs/0.jpg
        i+=1   #increment value of i  ,ie, i = i + 1
        print(i)
        if i>500:
            break

        # draw the segmented hand
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

        cv2.imshow("Video Feed 1", gray)   #display the resized frame

        cv2.imshow("Video Feed", frame)   #display the whole camera frame
        # observe the keypress by the user
        keypress = cv2.waitKey(1)

        # if the user pressed "Esc", then stop looping
        if keypress == 27:
            break

# free up memory
camera.release()
cv2.destroyAllWindows()

    


