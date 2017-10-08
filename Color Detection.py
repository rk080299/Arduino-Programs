
#Program for detecting blue objects


import cv2
import numpy as np


cap=cv2.VideoCapture(0)

while(1):
	_, img = cap.read()
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	blue_lower=np.array([110,115,150])                    #HSV range for blue color
	blue_upper=np.array([130,255,255])                    #NOTE HSV range is device dependent
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	bmask = cv2.GaussianBlur(blue, (5,5),0)
	kernal=np.ones((5,5))                                 
	blue=cv2.erode(blue,kernal)
	blue=cv2.dilate(blue,kernal)
	res=cv2.bitwise_and(img,img,mask=blue)
	
        (_,contours, hierarchy) = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)          #for creating contour
  
        if len(contours)>0:
        	largest = 0
        	area = 0
        	for i in range(len(contours)):
            
           		temp_area = cv2.contourArea(contours[i])
          
            		if temp_area > area:
               			area = temp_area
                		largest = i
    
		coordinates = cv2.moments(contours[largest])
       		x = int(coordinates['m10']/coordinates['m00'])
        	y = int(coordinates['m01']/coordinates['m00'])                        #Centroid of object detecting
		diam = int(np.sqrt(area)/4)
     
        	cv2.circle(res,(x,y),diam,(0,255,0),1)
       
		
	cv2.imshow("color Tracking",img)
	cv2.imshow("rk",res)                                                        #Display original and mask images
	

	if cv2.waitKey(10) & 0xFF ==ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
