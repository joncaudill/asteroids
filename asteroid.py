import pygame
import random

from constants import *

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * super().velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(spawn_angle)
        vector_b = self.velocity.rotate(-1 * spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid_b = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid_a.velocity = vector_a * 1.2
        new_asteroid_b.velocity = vector_b * 1.2