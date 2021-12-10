# Pygame_Drawing
# AUthout: Samson
# 9 November 2021

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = ( 0,  0,  0)
RED   = (255,0,0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    # Create the main loop
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Change the environment
        # Draw the environment
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [100, 100, 75, 30])
        # Update the screen
        pygame.display.flip()
        # Tick the clock
        clock.tick(75)
if __name__ == "__main__":
    main()

