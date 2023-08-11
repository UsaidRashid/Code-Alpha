import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Game")
pacman_image = pygame.image.load("pacman.png")
wall_image = pygame.image.load("wall.png")
ghost_image = pygame.image.load("ghost.png")
pacman_image = pygame.transform.scale(pacman_image, (30, 30))
wall_image = pygame.transform.scale(wall_image, (30, 30))
ghost_image = pygame.transform.scale(ghost_image, (30, 30))
dot_radius = 10
dots = [(50, 50), (150, 150), (250, 250)]
stage = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
pacman_rect = pacman_image.get_rect()
pacman_rect.center = (WIDTH // 2, HEIGHT // 2)
ghost_rect = ghost_image.get_rect()
ghost_rect.center = (WIDTH // 2 + 50, HEIGHT // 2+ 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_rect.move_ip(-2, 0)
    if keys[pygame.K_RIGHT]:
        pacman_rect.move_ip(2, 0)
    if keys[pygame.K_UP]:
        pacman_rect.move_ip(0, -2)
    if keys[pygame.K_DOWN]:
        pacman_rect.move_ip(0, 2)
    for y, row in enumerate(stage):
        for x, cell in enumerate(row):
            if cell == 1 and pacman_rect.colliderect(pygame.Rect(x * 30, y * 30, 30, 30)):
                pacman_rect.move_ip(0, 0)
    ghost_rect.move_ip(random.choice([-2, 2]), random.choice([-2, 2]))
    if ghost_rect.colliderect(pacman_rect):
        running = False 
    eaten_dots = [dot for dot in dots if pacman_rect.colliderect(pygame.Rect(dot[0] - dot_radius, dot[1] - dot_radius, dot_radius * 2, dot_radius * 2))]
    for dot in eaten_dots:
        dots.remove(dot)
    screen.fill((0, 0, 0))
    for y, row in enumerate(stage):
        for x, cell in enumerate(row):
            if cell == 1:
                screen.blit(wall_image, (x * 30, y * 30))
    for dot in dots:
        pygame.draw.circle(screen, (255, 255, 255), dot, dot_radius)
    screen.blit(pacman_image, pacman_rect)
    screen.blit(ghost_image, ghost_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
