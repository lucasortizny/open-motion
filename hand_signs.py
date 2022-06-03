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
    if results.multi_hand_landmarks:
        try:
            rightHand = results.multi_hand_landmarks[0]
            leftHand = results.multi_hand_landmarks[1]



            #MAPPING LANDMARKS

            x_pos_of_wrist_right = rightHand.landmark[0].x
            y_pos_of_wrist_right = rightHand.landmark[0].y


            #THUMB_JOINTS

            x_pos_of_thumb_1_right = rightHand.landmark[1].x
            y_pos_of_thumb_1_right = rightHand.landmark[1].y

            x_pos_of_thumb_2_right = rightHand.landmark[2].x
            y_pos_of_thumb_2_right = rightHand.landmark[2].y

            x_pos_of_thumb_3_right = rightHand.landmark[3].x
            y_pos_of_thumb_3_right = rightHand.landmark[3].y

            x_pos_of_thumb_4_right = rightHand.landmark[4].x
            y_pos_of_thumb_4_right = rightHand.landmark[4].y



            #INDEX_JOINTS
                    
            x_pos_of_index_1_right = rightHand.landmark[5].x
            y_pos_of_index_1_right = rightHand.landmark[5].y

            x_pos_of_index_2_right = rightHand.landmark[6].x
            y_pos_of_index_2_right = rightHand.landmark[6].y

            x_pos_of_index_3_right = rightHand.landmark[7].x
            y_pos_of_index_3_right = rightHand.landmark[7].y

            x_pos_of_index_4_right = rightHand.landmark[8].x
            y_pos_of_index_4_right = rightHand.landmark[8].y

            #MIDDLE FINGER JOINTS

            x_pos_of_middle_1_right = rightHand.landmark[9].x
            y_pos_of_middle_1_right = rightHand.landmark[9].y

            x_pos_of_middle_2_right = rightHand.landmark[10].x
            y_pos_of_middle_2_right = rightHand.landmark[10].y

            x_pos_of_middle_3_right = rightHand.landmark[11].x
            y_pos_of_middle_3_right = rightHand.landmark[11].y

            x_pos_of_middle_4_right = rightHand.landmark[12].x
            y_pos_of_middle_4_right = rightHand.landmark[12].y
                    
            #RING FINGER JOINTS

            x_pos_of_ring_1_right = rightHand.landmark[13].x
            y_pos_of_ring_1_right = rightHand.landmark[13].y

            x_pos_of_ring_2_right = rightHand.landmark[14].x
            y_pos_of_ring_2_right = rightHand.landmark[14].y

            x_pos_of_ring_3_right = rightHand.landmark[15].x
            y_pos_of_ring_3_right = rightHand.landmark[15].y

            x_pos_of_ring_4_right = rightHand.landmark[16].x
            y_pos_of_ring_4_right = rightHand.landmark[16].y

            #PINKY FINGER JOINTS

            x_pos_of_pinky_1_right = rightHand.landmark[17].x
            y_pos_of_pinky_1_right = rightHand.landmark[17].y

            x_pos_of_pinky_2_right = rightHand.landmark[18].x
            y_pos_of_pinky_2_right = rightHand.landmark[18].y

            x_pos_of_pinky_3_right = rightHand.landmark[19].x
            y_pos_of_pinky_3_right = rightHand.landmark[19].y

            x_pos_of_pinky_4_right = rightHand.landmark[20].x
            y_pos_of_pinky_4_right = rightHand.landmark[20].y




            #MAPPING LANDMARKS LEFT HAND

            x_pos_of_wrist_left = leftHand.landmark[0].x
            y_pos_of_wrist_left  = leftHand.landmark[0].y


            #THUMB_JOINTS

            x_pos_of_thumb_1_left  = leftHand.landmark[1].x
            y_pos_of_thumb_1_left  = leftHand.landmark[1].y

            x_pos_of_thumb_2_left  = leftHand.landmark[2].x
            y_pos_of_thumb_2_left  = leftHand.landmark[2].y

            x_pos_of_thumb_3_left  = leftHand.landmark[3].x
            y_pos_of_thumb_3_left  = leftHand.landmark[3].y

            x_pos_of_thumb_4_left  = leftHand.landmark[4].x
            y_pos_of_thumb_4_left  = leftHand.landmark[4].y



            #INDEX_JOINTS
                    
            x_pos_of_index_1_left  = leftHand.landmark[5].x
            y_pos_of_index_1_left  = leftHand.landmark[5].y

            x_pos_of_index_2_left  = leftHand.landmark[6].x
            y_pos_of_index_2_left  = leftHand.landmark[6].y

            x_pos_of_index_3_left  = leftHand.landmark[7].x
            y_pos_of_index_3_left  = leftHand.landmark[7].y

            x_pos_of_index_4_left  = leftHand.landmark[8].x
            y_pos_of_index_4_left  = leftHand.landmark[8].y

            #MIDDLE FINGER JOINTS

            x_pos_of_middle_1_left  = leftHand.landmark[9].x
            y_pos_of_middle_1_left  = leftHand.landmark[9].y

            x_pos_of_middle_2_left  = leftHand.landmark[10].x
            y_pos_of_middle_2_left  = leftHand.landmark[10].y

            x_pos_of_middle_3_left  = leftHand.landmark[11].x
            y_pos_of_middle_3_left  = leftHand.landmark[11].y

            x_pos_of_middle_4_left  = leftHand.landmark[12].x
            y_pos_of_middle_4_left  = leftHand.landmark[12].y
                    
            #RING FINGER JOINTS

            x_pos_of_ring_1_left  = leftHand.landmark[13].x
            y_pos_of_ring_1_left  = leftHand.landmark[13].y

            x_pos_of_ring_2_left  = leftHand.landmark[14].x
            y_pos_of_ring_2_left  = leftHand.landmark[14].y

            x_pos_of_ring_3_left  = leftHand.landmark[15].x
            y_pos_of_ring_3_left  = leftHand.landmark[15].y

            x_pos_of_ring_4_left  = leftHand.landmark[16].x
            y_pos_of_ring_4_left  = leftHand.landmark[16].y

            #PINKY FINGER JOINTS

            x_pos_of_pinky_1_left  = leftHand.landmark[17].x
            y_pos_of_pinky_1_left  = leftHand.landmark[17].y

            x_pos_of_pinky_2_left  = leftHand.landmark[18].x
            y_pos_of_pinky_2_left  = leftHand.landmark[18].y

            x_pos_of_pinky_3_left  = leftHand.landmark[19].x
            y_pos_of_pinky_3_left  = leftHand.landmark[19].y

            x_pos_of_pinky_4_left  = leftHand.landmark[20].x
            y_pos_of_pinky_4_left  = leftHand.landmark[20].y



            if step == 0:
                #check for raised thumbs
                is_left_thumb_raised = y_pos_of_thumb_4_left < y_pos_of_thumb_3_left and y_pos_of_thumb_3_left < y_pos_of_thumb_2_left and y_pos_of_thumb_2_left < y_pos_of_thumb_1_left
                is_right_thumb_raised = y_pos_of_thumb_4_right < y_pos_of_thumb_3_right and y_pos_of_thumb_3_right < y_pos_of_thumb_2_right and y_pos_of_thumb_2_right < y_pos_of_thumb_1_right
                is_left_index_out = x_pos_of_index_4_left < x_pos_of_index_3_left and x_pos_of_index_3_left < x_pos_of_index_2_left and x_pos_of_index_2_left < x_pos_of_index_1_left 
                is_right_index_out =  x_pos_of_index_4_right > x_pos_of_index_3_right and x_pos_of_index_3_right > x_pos_of_index_2_right and x_pos_of_index_2_right > x_pos_of_index_1_right


                pass_to_check = is_left_thumb_raised and is_right_thumb_raised and is_left_index_out and is_right_index_out
                if pass_to_check:
                    return True

            elif step == 1:
                #check for right thumb closed
                is_thumb_closed = y_pos_of_thumb_4_right > y_pos_of_thumb_3_right
                if is_thumb_closed:
                    return True
                
            elif step == 2:
                #check for left thumb closed
                is_thumb_closed = y_pos_of_thumb_4_left > y_pos_of_thumb_3_left
                if is_thumb_closed:
                    return True
            elif step == 3:
                is_right_index_closed = x_pos_of_index_4_right < x_pos_of_index_2_right
                if is_right_index_closed:
                    return True             
            elif step == 4:
                #check for left index closed
                is_left_index_closed = x_pos_of_index_4_left > x_pos_of_index_2_left
                if is_left_index_closed:
                    return True
            elif step == 5:
                is_right_thumb_closed = y_pos_of_thumb_4_right > y_pos_of_thumb_3_right
                is_left_thumb_closed = y_pos_of_thumb_4_left > y_pos_of_thumb_3_left
                is_right_index_closed = x_pos_of_index_4_right < x_pos_of_index_2_right
                is_left_index_closed = x_pos_of_index_4_left > x_pos_of_index_2_left
                if is_right_thumb_closed and is_left_thumb_closed and is_right_index_closed and is_left_index_closed:
                    return True
                    
        except:
            print('FIX HANDS')
        

def check_for_input_tetris(results,image):
    if results.multi_hand_landmarks:
        try:
            rightHand = results.multi_hand_landmarks[0]
            leftHand = results.multi_hand_landmarks[1]



            #MAPPING LANDMARKS

            x_pos_of_wrist_right = rightHand.landmark[0].x
            y_pos_of_wrist_right = rightHand.landmark[0].y


            #THUMB_JOINTS

            x_pos_of_thumb_1_right = rightHand.landmark[1].x
            y_pos_of_thumb_1_right = rightHand.landmark[1].y

            x_pos_of_thumb_2_right = rightHand.landmark[2].x
            y_pos_of_thumb_2_right = rightHand.landmark[2].y

            x_pos_of_thumb_3_right = rightHand.landmark[3].x
            y_pos_of_thumb_3_right = rightHand.landmark[3].y

            x_pos_of_thumb_4_right = rightHand.landmark[4].x
            y_pos_of_thumb_4_right = rightHand.landmark[4].y



            #INDEX_JOINTS
                    
            x_pos_of_index_1_right = rightHand.landmark[5].x
            y_pos_of_index_1_right = rightHand.landmark[5].y

            x_pos_of_index_2_right = rightHand.landmark[6].x
            y_pos_of_index_2_right = rightHand.landmark[6].y

            x_pos_of_index_3_right = rightHand.landmark[7].x
            y_pos_of_index_3_right = rightHand.landmark[7].y

            x_pos_of_index_4_right = rightHand.landmark[8].x
            y_pos_of_index_4_right = rightHand.landmark[8].y

            #MIDDLE FINGER JOINTS

            x_pos_of_middle_1_right = rightHand.landmark[9].x
            y_pos_of_middle_1_right = rightHand.landmark[9].y

            x_pos_of_middle_2_right = rightHand.landmark[10].x
            y_pos_of_middle_2_right = rightHand.landmark[10].y

            x_pos_of_middle_3_right = rightHand.landmark[11].x
            y_pos_of_middle_3_right = rightHand.landmark[11].y

            x_pos_of_middle_4_right = rightHand.landmark[12].x
            y_pos_of_middle_4_right = rightHand.landmark[12].y
                    
            #RING FINGER JOINTS

            x_pos_of_ring_1_right = rightHand.landmark[13].x
            y_pos_of_ring_1_right = rightHand.landmark[13].y

            x_pos_of_ring_2_right = rightHand.landmark[14].x
            y_pos_of_ring_2_right = rightHand.landmark[14].y

            x_pos_of_ring_3_right = rightHand.landmark[15].x
            y_pos_of_ring_3_right = rightHand.landmark[15].y

            x_pos_of_ring_4_right = rightHand.landmark[16].x
            y_pos_of_ring_4_right = rightHand.landmark[16].y

            #PINKY FINGER JOINTS

            x_pos_of_pinky_1_right = rightHand.landmark[17].x
            y_pos_of_pinky_1_right = rightHand.landmark[17].y

            x_pos_of_pinky_2_right = rightHand.landmark[18].x
            y_pos_of_pinky_2_right = rightHand.landmark[18].y

            x_pos_of_pinky_3_right = rightHand.landmark[19].x
            y_pos_of_pinky_3_right = rightHand.landmark[19].y

            x_pos_of_pinky_4_right = rightHand.landmark[20].x
            y_pos_of_pinky_4_right = rightHand.landmark[20].y




            #MAPPING LANDMARKS LEFT HAND

            x_pos_of_wrist_left = leftHand.landmark[0].x
            y_pos_of_wrist_left  = leftHand.landmark[0].y


            #THUMB_JOINTS

            x_pos_of_thumb_1_left  = leftHand.landmark[1].x
            y_pos_of_thumb_1_left  = leftHand.landmark[1].y

            x_pos_of_thumb_2_left  = leftHand.landmark[2].x
            y_pos_of_thumb_2_left  = leftHand.landmark[2].y

            x_pos_of_thumb_3_left  = leftHand.landmark[3].x
            y_pos_of_thumb_3_left  = leftHand.landmark[3].y

            x_pos_of_thumb_4_left  = leftHand.landmark[4].x
            y_pos_of_thumb_4_left  = leftHand.landmark[4].y



            #INDEX_JOINTS
                    
            x_pos_of_index_1_left  = leftHand.landmark[5].x
            y_pos_of_index_1_left  = leftHand.landmark[5].y

            x_pos_of_index_2_left  = leftHand.landmark[6].x
            y_pos_of_index_2_left  = leftHand.landmark[6].y

            x_pos_of_index_3_left  = leftHand.landmark[7].x
            y_pos_of_index_3_left  = leftHand.landmark[7].y

            x_pos_of_index_4_left  = leftHand.landmark[8].x
            y_pos_of_index_4_left  = leftHand.landmark[8].y

            #MIDDLE FINGER JOINTS

            x_pos_of_middle_1_left  = leftHand.landmark[9].x
            y_pos_of_middle_1_left  = leftHand.landmark[9].y

            x_pos_of_middle_2_left  = leftHand.landmark[10].x
            y_pos_of_middle_2_left  = leftHand.landmark[10].y

            x_pos_of_middle_3_left  = leftHand.landmark[11].x
            y_pos_of_middle_3_left  = leftHand.landmark[11].y

            x_pos_of_middle_4_left  = leftHand.landmark[12].x
            y_pos_of_middle_4_left  = leftHand.landmark[12].y
                    
            #RING FINGER JOINTS

            x_pos_of_ring_1_left  = leftHand.landmark[13].x
            y_pos_of_ring_1_left  = leftHand.landmark[13].y

            x_pos_of_ring_2_left  = leftHand.landmark[14].x
            y_pos_of_ring_2_left  = leftHand.landmark[14].y

            x_pos_of_ring_3_left  = leftHand.landmark[15].x
            y_pos_of_ring_3_left  = leftHand.landmark[15].y

            x_pos_of_ring_4_left  = leftHand.landmark[16].x
            y_pos_of_ring_4_left  = leftHand.landmark[16].y

            #PINKY FINGER JOINTS

            x_pos_of_pinky_1_left  = leftHand.landmark[17].x
            y_pos_of_pinky_1_left  = leftHand.landmark[17].y

            x_pos_of_pinky_2_left  = leftHand.landmark[18].x
            y_pos_of_pinky_2_left  = leftHand.landmark[18].y

            x_pos_of_pinky_3_left  = leftHand.landmark[19].x
            y_pos_of_pinky_3_left  = leftHand.landmark[19].y

            x_pos_of_pinky_4_left  = leftHand.landmark[20].x
            y_pos_of_pinky_4_left  = leftHand.landmark[20].y



            #CHECKING FOR HANDSIGN
            is_left_thumb_raised = y_pos_of_thumb_4_left < y_pos_of_thumb_3_left and y_pos_of_thumb_3_left < y_pos_of_thumb_2_left and y_pos_of_thumb_2_left < y_pos_of_thumb_1_left
            is_right_thumb_raised = y_pos_of_thumb_4_right < y_pos_of_thumb_3_right and y_pos_of_thumb_3_right < y_pos_of_thumb_2_right and y_pos_of_thumb_2_right < y_pos_of_thumb_1_right
            is_left_index_out = x_pos_of_index_4_left < x_pos_of_index_3_left and x_pos_of_index_3_left < x_pos_of_index_2_left and x_pos_of_index_2_left < x_pos_of_index_1_left 
            is_right_index_out =  x_pos_of_index_4_right > x_pos_of_index_3_right and x_pos_of_index_3_right > x_pos_of_index_2_right and x_pos_of_index_2_right > x_pos_of_index_1_right
            is_right_thumb_closed = y_pos_of_thumb_4_right > y_pos_of_thumb_3_right
            is_left_thumb_closed = y_pos_of_thumb_4_left > y_pos_of_thumb_3_left
            is_right_index_closed = x_pos_of_index_4_right > x_pos_of_index_2_right
            is_left_index_closed = x_pos_of_index_4_left < x_pos_of_index_2_left
            
            
            
            
            #Check for Tetris HANDS
            tetris_hands = is_left_thumb_raised and is_right_thumb_raised and is_left_index_out and is_right_index_out
            # Check for closed hands
            closed_hands = is_right_thumb_closed and is_left_thumb_closed and is_right_index_closed and is_left_index_closed
            
            #check for tetris_hands
            if tetris_hands:
                return 1
            #check for left_thumb_closed
            if is_left_thumb_closed:
                return 2     
            #check for right_thumb_closed
            if is_right_thumb_closed:
                return 3        
            #check for right_index_closed
            if is_right_index_closed:
                return 4
            #check to see if left index is closed
            if is_left_index_closed:
                return 6
            else:
                return 7
                    
        except:
            print('FIX HANDS')
                    
    
    
    

    
