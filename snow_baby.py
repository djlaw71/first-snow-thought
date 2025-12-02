import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Snow – Exmoor")
clock = pygame.time.Clock()

SKY = (5, 5, 20)
SNOWFLAKE = (230, 240, 255)
FUR_DARK = (45, 25, 20)
FUR_LIGHT = (100, 70, 50)
EYES = (180, 240, 255)
THOUGHT = (200, 220, 255)

baby_x, baby_y = WIDTH//2, HEIGHT - 150
thought_alpha = 0
thought_text = None
font = pygame.font.SysFont("arialunicode", 32, bold=True)

snowflakes = []
for _ in range(180):
    snowflakes.append({
        'x': random.randint(0, WIDTH),
        'y': random.randint(-HEIGHT, 0),
        'speed': random.uniform(0.5, 2),
        'size': random.randint(2, 6)
    })

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)

    # hills
    pygame.draw.circle(screen, (15, 15, 40), (200, HEIGHT+100), 400)
    pygame.draw.circle(screen, (20, 20, 50), (700, HEIGHT+100), 500)

    # snowflakes
    for flake in snowflakes:
        flake['y'] += flake['speed']
        if flake['y'] > HEIGHT:
            flake['y'] = random.randint(-50, -5)
            flake['x'] = random.randint(0, WIDTH)
        pygame.draw.circle(screen, SNOWFLAKE, (int(flake['x']), int(flake['y'])), flake['size'])

    # newborn
    pygame.draw.ellipse(screen, FUR_DARK, (baby_x-80, baby_y-40, 160, 100))
    pygame.draw.ellipse(screen, FUR_LIGHT, (baby_x-70, baby_y-35, 140, 90))
    pygame.draw.circle(screen, FUR_DARK, (baby_x+60, baby_y-50), 50)
    pygame.draw.circle(screen, FUR_LIGHT, (baby_x+65, baby_y-55), 45)
    pygame.draw.circle(screen, (0, 0, 0), (baby_x+80, baby_y-60), 12)        # pupil
    pygame.draw.circle(screen, EYES, (baby_x+82, baby_y-62), 8)            # iris – fixed!
    pygame.draw.circle(screen, SNOWFLAKE, (baby_x+100, baby_y-60), 5)      # snow on nose

    # first thought
    if random.random() < 0.003 and thought_alpha == 0:
        thought_text = font.render("mum... this isn't home", True, THOUGHT)
        thought_alpha = 255

    if thought_alpha > 0:
        thought_text.set_alpha(thought_alpha)
        screen.blit(thought_text, (baby_x-120, baby_y-130))
        thought_alpha -= 0.8

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
