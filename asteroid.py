from circleshape import CircleShape
import pygame
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) 
        v2 = self.velocity.rotate(-angle)
        r1 = self.radius - ASTEROID_MIN_RADIUS
        r2 = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1],r1)
        a2 = Asteroid(self.position[0], self.position[1],r2)
        a1.velocity = v1
        a1.velocity *= 1.2
        a2.velocity = v2
        a2.velocity *= 1.2
        

    