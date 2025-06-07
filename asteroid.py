import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        self.screen = screen
        self.width = 2
        self.color = "white"
        return pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vector = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = vector * 1.2
        new_asteroid2.velocity = vector2 * 1.2

        new_asteroid1.draw(self.screen)
        new_asteroid2.draw(self.screen)
