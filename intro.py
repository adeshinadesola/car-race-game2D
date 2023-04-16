import pygame
import menuscreen
from moviepy.editor import VideoFileClip

def play_intro():
    pygame.init()

    # Set up the window
    screen_width = 600
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("CAR DRIVE 2D")

    #load sound
    sound = pygame.mixer.Sound('introaudio.mp3')

    # Load the video
    video = VideoFileClip('video01.avi')  # replace with the path to your video file
    #video.resize()
    #video.resize(2)
    #clip_resized = video.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
    #clip_resized.write_videofile("intro.mp4")
    #video = pygame.transform.scale(video,(500,700))

    # Main loop
    while True:

        #playing sound
        sound.play()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get the current frame of the video
        frame = video.get_frame(pygame.time.get_ticks() / 1000)

        # Convert the frame to a Pygame surface
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Blit the surface onto the screen
        screen.blit(surface, (0,0))

        # Update the display
        pygame.display.update()

        # Check if the video has ended
        if pygame.time.get_ticks() / 1000 >= video.duration:
            sound.stop()
            menuscreen.run()

            #logic for menu screen
            #backplayer.bg_with_player()
            #pygame.quit()
            #quit()

            

