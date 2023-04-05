import pygame
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.1

# Particle class
class Particle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.radius = radius
        self.color = color

    def update(self):
        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy

        # Update velocity based on gravity
        self.vy += GRAVITY

        # Bounce off walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.vx *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")
clock = pygame.time.Clock()

# Create particles
particles = []
for _ in range(10):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    radius = random.randint(10, 30)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particle = Particle(x, y, radius, color)
    particles.append(particle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill((255, 255, 255))

    # Update particles
    for particle in particles:
        particle.update()
        particle.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
