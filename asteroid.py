from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, width=LINE_WIDTH)

    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)


    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)

            first_asteroid_vector = self.velocity.rotate(new_angle)
            second_asteroid_vector = self.velocity.rotate(-1*new_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius) 
            second_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)

            first_asteroid.velocity = first_asteroid_vector * 1.2
            second_asteroid.velocity = second_asteroid_vector * 1.2



