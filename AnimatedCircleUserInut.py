import pygame
import sys

radius = int(input("Enter circle size (e.g., 20-50): "))
speed = float(input("Enter speed (e.g., 2-10): "))
fps = int(input("Enter FPS (e.g., 30-120): "))

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Moving Circle")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 20)

x, y = width // 2, height // 2

# -------- MAIN LOOP --------
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), int(radius))

    # -------- DISPLAY INFO --------
    info_text = [
        f"X: {int(x)} Y: {int(y)} Speed: {round(speed, 2)} Size (Radius): {radius} 25FPS: {fps}"
    ]

    for i, text in enumerate(info_text):
        render = font.render(text, True, BLACK)
        screen.blit(render, (10, 10 + i * 25))

    pygame.display.flip()
    clock.tick(fps)