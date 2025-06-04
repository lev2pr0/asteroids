# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this allows us to use code from
# the constants & player (Player class) modules
# through out this file
from constants import *
from player import Player

# variables for game loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# gameloop function to:
# - handle events
# - update game state
# - render game objects
def gameloop():
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, BLACK)
        Player.draw(player, screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        player.update(dt)

# main function to:
# - initialize pygame
# - print game information
# - call gameloop function
def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    gameloop()

# if/else statement to:
# - check if this file is being run directly
# - call main function if it is
if __name__ == "__main__":

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y, PLAYER_RADIUS)

    main()
