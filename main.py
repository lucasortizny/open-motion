import numpy as np
import cv2 
import argparse
import sys
import time
import mediapipe
import cv2
import mediapipe as mp
def checker():
  
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_hands = mp.solutions.hands




  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FPS,30)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
  cap.set(cv2.CAP_PROP_FPS,60)
  
  exit_touched = False

  with mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue
      
      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = hands.process(image)
      
      # Draw the hand annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


      if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
          for id,lm in enumerate(handLms.landmark):
            h,w,c = image.shape
            cx,cy = int(lm.x*w),int(lm.y*h)
            if id == 8:
              cv2.circle(image,(cx,cy),5,(255,0,255),cv2.FILLED)





      if exit_touched == True:
        break
      # Flip the image horizontally for a selfie-view display.
      
      image = cv2.flip(image, 1)
      cv2.putText(image,'Exit',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
      cv2.imshow('frame',image)

      if cv2.waitKey(5) & 0xFF == 27:
        break

      
      
      

  cap.release()


