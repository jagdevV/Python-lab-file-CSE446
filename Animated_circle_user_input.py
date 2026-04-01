import pygame
import sys

WIDTH, HEIGHT = 800, 600
CIRCLE_RADIUS = 30
CIRCLE_COLOR = (0, 255, 0)
SPEED = 5
FPS = 60
BG_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
dx = 0
dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -SPEED
            if event.key == pygame.K_DOWN:
                dy = SPEED
            if event.key == pygame.K_LEFT:
                dx = -SPEED
            if event.key == pygame.K_RIGHT:
                dx = SPEED
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                dy = 0
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                dx = 0

    x += dx
    y += dy

    x = max(CIRCLE_RADIUS, min(WIDTH - CIRCLE_RADIUS, x))
    y = max(CIRCLE_RADIUS, min(HEIGHT - CIRCLE_RADIUS, y))

    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)