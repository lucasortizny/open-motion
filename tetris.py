from tabnanny import check
import pygame
import cv2
import mediapipe as mp
import hand_signs
import time
import game_selection

def main():

    #intialize
    pygame.init()


    #create display
    width,height = 720,640
    window=pygame.display.set_mode((width,height))


    #initialize Clock for FPS

    



    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands


    #main loop
    with mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
        while cap.isOpened():


            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)          

            #if game esc is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start=False
                    pygame.quit()

            window.fill((255,255,255))



            #OpenCV Logic
            success,img = cap.read()
            image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            

            #Impor the logic that captures the hand input
            action = hand_signs.check_for_input_tetris(results,image)

            



            pygame.display.update()

