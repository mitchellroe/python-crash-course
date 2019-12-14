#!/usr/bin/env python3


import sys
import pygame


def main():
    """Run the game"""

    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("This is my pygame.")

    image = pygame.image.load('images/my-dino.bmp')
    image_rect = image.get_rect()

    while True:
        # Watch for keyboard and mouse input.
        for event in pygame.event.get():
            if event.type() == pygame.QUIT():
                sys.exit()



if __name__ == '__main__':
    main()
