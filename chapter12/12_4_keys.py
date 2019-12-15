#!/usr/bin/env python3

import pygame
import sys


def run_game():
    """Just print the key we're getting"""
    pygame.init()
    pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Keys")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    run_game()
