import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

# variables for game loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

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

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if CircleShape.collide(player, asteroid) == True:
                sys.exit("Game over!")

        for asteroid in asteroids:
            for shot in shots:
                if Shot.collide(shot, asteroid) == True:
                    asteroid.kill()
                    shot.kill()



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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y, PLAYER_RADIUS, shots)
    asteroid_field = AsteroidField()

    main()
