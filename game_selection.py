import pygame
import menu_objects 



pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([720, 640])



running = True

menu_dim = (640,300)
menu_pos = (40,300)

menu = menu_objects.Menu_Container((0,0,0),menu_dim,menu_pos)


button_text = ['Select Games','Settings','Exit']
menu_buttons = [menu_objects.Button(button_text[i],(255,0,0),(menu_dim[0]*.8,menu_dim[1]*.2),(menu_pos[0]+60,menu_pos[1]+(i*80)+40)) for i in range(3)]



while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    menu.draw(screen)
    for each in menu_buttons:
        each.draw(screen)
    pygame.display.flip()



pygame.quit()
