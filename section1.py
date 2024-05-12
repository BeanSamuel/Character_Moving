import pygame, sys

def main():
    # Initialize Pygame
    pygame.init()
    # Set the window title
    pygame.display.set_caption("Moving Animation")
    # Set the window size
    width_screen, height_screen = 640, 360
    screen = pygame.display.set_mode((width_screen, height_screen))

    # Load the background image
    img_bg = pygame.image.load("background.png")
    width_bg, height_bg = img_bg.get_width(), img_bg.get_height()

    # Load the character images
    img_characters = [pygame.image.load("image1.png"), pygame.image.load("image2.png")]
    width_character, height_character = img_characters[0].get_width(), img_characters[0].get_height()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # return 
        for i in range( width_screen // width_bg ):
            screen.blit(img_bg, (i * width_bg, 0))
        pygame.display.update()

if __name__ == "__main__":
    '''
    Initialize Pygame
    Load the background image
    Load the character images
    Show the static background image
    '''
    main()
