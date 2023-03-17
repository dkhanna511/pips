# importing the module
import cv2
import numpy as np
#adapted from online tutorial, added in aspects to record the actual button push for x and y recognition for particle video
import os
firstimage='/home/dheerajk/ATS_Work/datasets/demoATSDatasetImages/frame_0000.jpg' #PUT IN IMAGE NAME, can convert to arg
#this will be your labeled image
# function to display the coordinates of
global CORLIST
CORLIST=np.zeros((1,2))
global GCOUNTER
GCOUNTER=0
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, str(x) + ',' +
        #            str(y), (x, y), font,
        #            1, (255, 0, 0), 2)
        cv2.circle(img, (x, y), 3, (0, 255, 0))
        cv2.imshow('image', img)
        #GCOUNTER=GCOUNTER+1
        global GCOUNTER
        global CORLIST
        if GCOUNTER>0:

            CORLIST=np.append(CORLIST,[[x,y]],axis=0)
        else:
            CORLIST[GCOUNTER][0]=x
            CORLIST[GCOUNTER][1]=y
        GCOUNTER+=1
if __name__ == "__main__":
    # reading the image
    print('we are creating an x y numpy array \n press any key to kill the session and output text \n you must set your first image name at the top of the file \n click until you are done')
    fd=open('xy_out.txt','w').close() #clears the file

    img = cv2.imread(firstimage, 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    #print(XLIST)
    #print(torch.tensor(YLIST))
    # close the window
    #xy1 = torch.from_numpy(CORLIST)  # B, N_*N_, 2cv2
    #print(xy1)
    np.savetxt('xy_out.txt',CORLIST)
    #j=np.loadtxt('xy_out.txt')
    #this is how you load in the numpy array
    cv2.destroyAllWindows()
