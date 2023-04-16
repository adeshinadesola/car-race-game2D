import pygame
from pygame.locals import*
import menuscreen

def run():


    pygame.init()

    screen_width = 600
    screen_height = 700

    display_window = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Game Settings")

    #image of settings page
    img= pygame.image.load(r"Settings.jpg")
    img= pygame.transform.scale(img,(595,700))
    #locating back button
    back_button_rect =pygame.Rect(screen_width //3 - 60, screen_height - 90, 65, 65)

    running = True

    while running:
        display_window.blit(img,(0,0))

        for each_event in pygame.event.get():
            if each_event.type == QUIT:
                pygame.quit()
                running = False
            if each_event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    menuscreen.run()
                
        # Draw the buttons
        #pygame.draw.rect(display_window, (255, 0, 0), back_button_rect)

        pygame.display.update()