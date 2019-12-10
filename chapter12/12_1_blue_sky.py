#!/usr/bin/env python3

import sys
import pygame
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Sky")

    bg_color = (0, 0, 255)

    while True:
        # Do some stuff
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
