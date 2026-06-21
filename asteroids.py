import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroids(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        first_movement = self.velocity.rotate(new_angle)
        second_movement = self.velocity.rotate(- new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroids(self.position.x ,self.position.y,new_radius)
        second_asteroid = Asteroids(self.position.x ,self.position.y,new_radius)
        first_asteroid.velocity = first_movement * 1.2
        second_asteroid.velocity = second_movement * 1.2


