import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30
try:
    j = pygame.joystick.Joystick(0)
    j.init()

except:
    print('Джойстик подключен\8')
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    mouse = pygame.mouse
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3
    if mouse.get_pressed()==(1,0,0): (x,y) = mouse.get_pos()
    if pressed[pygame.K_0]: is_blue = not is_blue

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)