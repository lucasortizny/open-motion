import pygame
import sys
import checker

WHITE = (255,255,255)
BLACK = (0,0,0)

class Menu_Container():
    def __init__(self,color, menu_dim,menu_pos):  

        self.top_rect = pygame.Rect(menu_pos,menu_dim)
        self.top_color = color


    def draw(self,screen):
        pygame.draw.rect(screen,self.top_color,self.top_rect)


class Button():
    def __init__(self,text,color,button_dim,button_pos):

        self.pressed = False
        self.text = text
        #rectangle
        self.top_rect = pygame.Rect(button_pos,button_dim)
        self.top_color = color
        
        #text
        self.font = pygame.font.SysFont("Arial", 30)
        self.text_surf = self.font.render(text, 1, (0,0,255))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self,screen):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                        self.button_action()
                        self.pressed = False

    
    def button_action(self):
        if self.text == 'Exit':
            pygame.quit()
            sys.exit()
        else:
            print(f'pressed {self.text}')

        if self.text == 'Settings':
            pygame.quit()
            checker.checker()
