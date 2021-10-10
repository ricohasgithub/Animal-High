
import pygame

from random import randrange

from utils.utils import *
from utils.button import Point
from utils.button import Button

if __name__ == "__main__":

    pygame.init()

    # Set up display and timer (timer is needed for the textbox)
    window = pygame.display.set_mode((800, 600))

    r_button = Button(100, 50, Point(650, 500), (255, 0, 0))
    g_button = Button(100, 50, Point(650, 400), (0, 255, 0))
    b_button = Button(100, 50, Point(650, 300), (0, 0, 255))

    # Main event loop
    run = True
    
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # Check all display events
            if r_button.on_click(event) == True:
                pass
            if g_button.on_click(event) == True:
                pass
            if b_button.on_click(event) == True:
                pass

        window.fill((255, 255, 255))

        # Render all display elements
        r_button.render(window)
        g_button.render(window)
        b_button.render(window)

        render_text(window, "Hello world", Point(20, 20))

        # Update the screen display
        pygame.display.flip()

    pygame.quit()