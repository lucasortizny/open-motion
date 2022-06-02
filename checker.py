import cv2
import mediapipe as mp
import hand_signs
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)
timer_started = False
test_mode = False
step = 0
tests = [{'Tetris Hands':'NOT PASSED'},{'Right Thumb Closed':'NOT PASSED'},{'Left Thumb Closed':'NOT PASSED'},{'Left Index Closed':'NOT PASSED'},{'Right Index Closed':'NOT PASSED'},{'Closed Hands':'NOT PASSED'}]

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
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    
   
    
    #FLIP THE IMAGE
    image = cv2.flip(image, 1)


    #LOGIC TO ENTER TESTING MODE
    if test_mode :
        cv2.putText(image,'Testing Mode',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
        for index,test in enumerate(tests):
            cv2.putText(image,f'{list(test.keys())[0]} : status {list(test.values())[0]}',(200,int(400*(index*0.1))),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)


    else:
        #CHECK TO SEE IF BOTH HANDS ARE RAISED
        test_check = hand_signs.check_for_both_hands(results,image)


        #IF BOTH HANDS ARE RAISED AND A TIMER HAS NOT BEEN STARTED
        if test_check and not timer_started:
            timer_started = True
            timer = hand_signs.start_test_timer()


        #IF BOTH HANDS ARE RAISED AND A TIMER HAS BEEN STARTED CHECK TO SEE UNTIL IT HITS
        #5 SECONDS. AFTER 5 SECONDS, IMPLEMENT TEST MODE
        if test_check and timer_started:
            if int(time.time() - timer) in [1,2,3,4]:
                cv2.putText(image,f'Hold for {5-int(time.time() - timer)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
            if time.time() - timer > 5:              
                test_mode = True
        
        #IF THE HANDS GET LOWERED AT ANY POINT, THE 5 SECONDS MUST BE STARTED OVER AGAIN    
        if not test_check:
            timer_started = False


    
    cv2.imshow('frame',image)





    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()