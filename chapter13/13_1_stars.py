#!/usr/bin/env python3

import pygame


class Stars:
    def __init__(self):
        """Initialize a new Stars object."""
        pygame.init()

        width, height = 1280, 800
        self.screen = pygame.display.set_mode((width, height))
        # Add a clock to limit the frame rate.
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Stars!")

    def run_game(self):
        """Run the primary game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False

            # Insert the game logic here.

            # Then draw everything, flip the display and call clock tick.
            self.screen.fill((200, 200, 200))
            pygame.display.flip()
            self.clock.tick(60)      # Limit the frame rate to 60 FPS

        pygame.quit()


if __name__ == '__main__':
    st = Stars()
    st.run_game()
