import pygame
import math
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
BODY_COLOR = (0, 0, 255)
CENTER_BODY_COLOR = (255, 0, 0)
NUM_BODIES = 9
CENTER_BODY_RADIUS = 50
BODY_RADIUS = 10
CENTER_BODY_MASS = 10000
BODY_MASS = 100

# Body class for representing individual bodies
class Body:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.vel_x = 0
        self.vel_y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Orbiting Bodies")

# Create center body
center_body = Body(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, CENTER_BODY_RADIUS, CENTER_BODY_MASS, CENTER_BODY_COLOR)

# Create orbiting bodies
bodies = []
for i in range(NUM_BODIES):
    angle = i * (2 * math.pi / NUM_BODIES)  # Equally spaced angles
    x = center_body.x + math.cos(angle) * (CENTER_BODY_RADIUS + 100)
    y = center_body.y + math.sin(angle) * (CENTER_BODY_RADIUS + 100)
    radius = BODY_RADIUS
    mass = BODY_MASS
    color = BODY_COLOR
    body = Body(x, y, radius, mass, color)
    bodies.append(body)

# Simulation loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60) / 1000.0  # Time elapsed in seconds since last frame

    # Update orbiting bodies based on gravitational attraction towards center body
    for body in bodies:
        dx = center_body.x - body.x
        dy = center_body.y - body.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        force = (CENTER_BODY_MASS * BODY_MASS) / (dist ** 2)  # Newton's law of universal gravitation
        angle = math.atan2(dy, dx)
        body.vel_x = force * math.cos(angle) / body.mass
        body.vel_y = force * math.sin(angle) / body.mass
        body.update(dt)

    # Clear screen
    screen.fill(BG_COLOR)

    # Draw center body
    center_body.draw(screen)

    # Draw orbiting bodies
    for body in bodies:
        body.draw(screen)

    # Update display
    pygame.display.flip()
