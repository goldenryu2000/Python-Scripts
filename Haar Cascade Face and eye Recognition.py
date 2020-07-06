#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[7]:


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("Haar Cascade/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("Haar Cascade/haarcascade_eye_tree_eyeglasses.xml")
while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret==False:
        continue
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    eyes = eye_cascade.detectMultiScale(gray_frame,1.3,6)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),4)
    for (a,b,c,d) in eyes:
        cv2.rectangle(frame, (a,b),(a+c,b+d),(255,255,0),4)
        
    cv2.imshow("Video" , frame)
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




