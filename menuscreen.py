import pygame
import backplayer
import game_settings

def run():

    pygame.init()

    # Set up the window
    screen_width = 600
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Menu Screen")

    #defining the menu screen imagaae
    menuimg= pygame.image.load("menu.jpg")
    menuimg= pygame.transform.scale(menuimg,(screen_width,screen_height))

    # Set up the fonts
    #font = pygame.font.SysFont("Arial", 32)
    sound = pygame.mixer.Sound('bgmusic.mp3')


    # Define the button rectangles
    start_button_rect = pygame.Rect(screen_width // 2 - 220, screen_height // 2 + 15 , 150, 50)
    quit_button_rect = pygame.Rect(screen_width // 2 - 220, screen_height // 2 + 195, 150, 50)
    settings_button = pygame.Rect(screen_width//2-220,screen_height//2 + 105, 150, 50 )

    # Main loop
    while True:

        #playing the background music
        sound.play()


        #displaying the menu screen 
        screen.blit(menuimg,(0,0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    print("Start button clicked!")
                    
                    backplayer.bg_with_player()
                elif settings_button.collidepoint(mouse_pos):
                    print("settings")
                    game_settings.run()
                    
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

        


        pygame.display.update()
