import random
from circleshape import *
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first = self.velocity.rotate(angle)
            second = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_first.velocity = first * 1.2
            asteroid_second.velocity = second * 1.2
