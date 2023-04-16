import pygame , random,sys
from verticalplayer import player1
#from coin import coins

def bg_with_player():
    # code for background scroll
    width = 500
    height = 700

    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("CAR DRIVE 2D")

    background = pygame.image.load("backgroundimg.jpg")
    background = pygame.transform.scale(background,(500,700))
    overlap = pygame.image.load("backgroundimg.jpg")
    overlap = pygame.transform.scale(overlap,(500,700))
    b_pos = 300
    o_pos =0
    c_pos=0
    speed= 0.1

    #call for player from vertical player
    p = player1(250,height-100)

        #movement of player
    moving_left = False
    moving_right = False

    #coin falling

    #j=[0,1,2]
    n= random.randint(1,4)

    #c= coins(width-(n*100), 80)
    #coin_image = pygame.image.load(f'coin.png')


    #centre of images for collision

    def get_image_hcenter(image):
        """Get the center coordinates of an image in Pygame"""
        rect = image.get_rect()
        center_x = rect.centerx
        
        return center_x
    def get_image_vcenter(image):
        """Get the center coordinates of an image in Pygame"""
        rect = image.get_rect()
        center_y = rect.centery
        return center_y
    
     # Set up the columns
    COLUMN_WIDTH = 600// 4
    COLUMNS = [COLUMN_WIDTH + i for i in [5,100,203]]


    #call for player from vertical player
    p = player1(250,height-100)

        #movement of player
    moving_left = False
    moving_right = False

    #loading banner
    game_banner= pygame.image.load('banner.jpg')
    game_banner= pygame.transform.scale(game_banner ,(80,80))
    score_board = pygame.Rect(20,110,120,210)

    # Load the object images
    object_images = []
    for i in range(1, 4):
        image = pygame.image.load(f"onecoin.jpg").convert_alpha()
        image2 = pygame.image.load(f"twocoins.jpg").convert_alpha()
        image3 = pygame.image.load(f"barrier.jpg").convert_alpha()
        
        object_images.append(pygame.transform.scale(image, (80,80)))
        object_images.append(pygame.transform.scale(image2, (80,100)))
        object_images.append(pygame.transform.scale(image3, (80,80)))

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the variables for the falling object
    object_rect = None
    object_image = None
    falling = False
    falling_column = None
    collision=0
    score=0

    #text to be displayed
    pygame.font.init()
    Font = pygame.font.SysFont('Arial', 30)

    # Set up the speed and the acceleration
    speed = 0.5
    acceleration = 0.0000001

    #collizion variables
    rect1 = pygame.Rect(get_image_hcenter(p.image),get_image_vcenter(p.image),100,100)
    rect2 = pygame.Rect(get_image_hcenter(image2),get_image_vcenter(image2),100,100)
    rect3 = pygame.Rect(get_image_hcenter(image),get_image_vcenter(image),100,100)
    rect4 = pygame.Rect(get_image_hcenter(image3),get_image_vcenter(image3),100,100)





    running = True

    while running:
        if b_pos >= height:
            b_pos = -height
        if o_pos >= height:
            o_pos = -height

        b_pos += speed
        o_pos += speed
        screen.blit(overlap,(0, b_pos))
        screen.blit(background, (0,o_pos))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #movement control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
            if event.type == pygame.KEYUP:
                moving_left= False
                moving_right= False

             # Check if an object is currently falling
        if not falling:
            # Randomly choose a column for the object to fall in
            falling_column = random.choice(COLUMNS)

            # Randomly choose an object image
            object_image = random.choice(object_images)

            # Set up the object's rect
            object_rect = object_image.get_rect(x=falling_column, y=0)

            # Set the falling flag to True
            falling = True

        # Move the object down the screen
        object_rect.y += speed
        speed += acceleration

        # Check if the object has reached the bottom of the screen
        if object_rect.y >= height:
            # Reset the falling flag
            falling = False

        # Draw the columns
        #for column in COLUMNS:
            #pygame.draw.line(screen, (255, 255, 255), (column, 0), (column, height))

        # Draw the falling object
        if falling:
            screen.blit(object_image, object_rect)

        if pygame.Rect.colliderect(rect1,rect3) == True:
            score= score+1
        if pygame.Rect.colliderect(rect1,rect3) == True:
            score= score+2
            

        if pygame.Rect.colliderect(rect1,rect4) == True:
            collision= collision +1
            running = False
            
        #displaying score window
        
        #pygame.draw.rect(score_board,(255,0,0))
        #pygame.Rect(20,110,120,210)
        

        #update the score
        score_text = Font.render("coins: " + str(score), True, (255, 0, 0))
        screen.blit(score_text, (20, 120))

        #display game banner
        screen.blit(game_banner,(20,20))

       


            # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(320)



            

        p.draw(screen)
        
    #    c.draw(screen)

        #if c_pos >= width:
        #   c_pos = -width
        #screen.blit(coin_image,(c_pos,0))
        
        
        
        
        
        p.update(moving_left,moving_right)
        # Draw the buttons





        pygame.display.update()

    while running == False:

        # Game over screen
        game_over_text = Font.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over_text, (200, 200))
        pygame.display.flip()
    


    

    

            




    # Quit the game
    pygame.quit()

    

