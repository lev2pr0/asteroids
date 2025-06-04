# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this allows us to use code from
# the constants & circleshape (CircleShape class) modules
# through out this file
from constants import *
from circleshape import CircleShape

# Player class inheriting from CircleShape
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = PLAYER_RADIUS

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        self.screen = screen
        self.width = 2
        self.color = "white"
        return pygame.draw.polygon(self.screen, self.color, self.triangle(), self.width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
