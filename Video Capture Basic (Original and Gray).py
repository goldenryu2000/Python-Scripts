#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
cap = cv2.VideoCapture(0)  #capturing the default video device.... For other devices just hit and try with other values 
while True: 
    ret,frame = cap.read() #reading the input frame by frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the color space to grayscale
    if ret == False: #if the read() returns an error
        continue
    cv2.imshow("Video Wbcam", frame) #original video stream
    cv2.imshow("Gray Frame" , gray_frame) #grayscale video stream
    
    #to stop the webcam when "q" is pressed.
    key_pressed = cv2.waitKey(1) & 0xFF  #converting the 32-bit output by waitKey() into an 8-bit to match the ASCII code(0-255)
    if key_pressed == ord('q'): #checking if the pressed key is a 'q'.... ord('q') returns the ASCII code of the character
        break
cap.release() #release the video capture device
cv2.destroyAllWindows() #destroy all the windows


# In[ ]:




