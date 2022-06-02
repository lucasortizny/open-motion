import cv2
import mediapipe as mp
import time

def check_for_both_hands(results,image):
    
    if results.multi_handedness == None:
        cv2.putText(image,'PLEASE RAISE HANDS',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif len(results.multi_handedness) == 1:
        cv2.putText(image,'PLEASE RAISE BOTH HANDS',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    else:    
        test_ready = True
        return test_ready

        
def start_test_timer():
    timer_started = time.time()
    return timer_started


def test_for_gestures(results,image,step):
    tests = ['Tetris Hands','Right Thumb Closed','Left Thumb Closed','Left Index Closed','Right Index Closed','Closed Hands']
    

    
