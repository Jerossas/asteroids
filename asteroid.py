from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, width=LINE_WIDTH)

    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
