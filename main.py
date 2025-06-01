from constants import *

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def gameloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK)
        pygame.display.flip()

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    gameloop()











if __name__ == "__main__":
    main()
