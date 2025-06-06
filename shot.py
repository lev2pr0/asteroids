import pygame
from circleshape import CircleShape
from constants import *

# Shot class inheriting from CircleShape
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        self.screen = screen
        self.width = 0
        self.color = "white"
        return pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def update(self, dt):
        self.position += dt * self.velocity
