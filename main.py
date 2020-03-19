import pygame
pygame.init()
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
running = True
r = 0
v = 10   # пикселей в секунду
clock = pygame.time.Clock()
pos = False
screen.fill((0, 0, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0, 0, 255))
            pos = event.pos
            r = 0
    r += v * clock.tick() / 1000  # v * t в секундах
    if pos:
        pygame.draw.circle(screen, (255, 255, 0), (pos[0], pos[1]), int(r))
    pygame.display.flip()