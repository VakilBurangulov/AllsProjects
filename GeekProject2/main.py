import pygame
import random

pygame.init()

W, H = 800, 600

display = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

 
def draw_score(score):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, 48)
    render = font.render(str(score), 1, 'green')
    render_hitbox = render.get_rect(topleft=(0, 0))
    display.blit(render, render_hitbox)


class BackGround:
    def __init__(self):
        self.bg = pygame.image.load('res/fon.png')

    def draw(self):
        display.blit(self.bg, (0, 0))


class Crosshair:

    def __init__(self):
        self.sprite = pygame.image.load('res/crosshair_small.png')
        self.hitbox = self.sprite.get_rect()

    def draw(self):
        display.blit(self.sprite, self.hitbox)

    def move(self):
        self.hitbox.center = pygame.mouse.get_pos()


class Target:
    def __init__(self):
        self.sprite = pygame.image.load('res/target_small.png')
        self.hitbox = self.sprite.get_rect()
        self.hits_number = 0

    def draw(self):
        display.blit(self.sprite, self.hitbox)

    def move(self):
        if self.is_clicked_by(crosshair):
            w = self.hitbox.width
            h = self.hitbox.height
            self.hitbox.x = random.randint(0, W - w)
            self.hitbox.y = random.randint(0, H - h)
            self.hits_number += 1

    def is_clicked_by(self, small_crosshair: Crosshair):
        if where_mouse_pressed(0):
            horiz = self.hitbox.left < small_crosshair.hitbox.centerx < self.hitbox.right
            vert = self.hitbox.top < small_crosshair.hitbox.centery < self.hitbox.bottom
            return horiz and vert


def is_key_pressed(key):
    return pygame.key.get_pressed()[key]


def where_mouse_pressed(mouse_key):
    buttons = pygame.mouse.get_pressed(num_buttons=5)
    if buttons[mouse_key]:
        return pygame.mouse.get_pos()


crosshair = Crosshair()
target = Target()
background = BackGround()

def main():
    while True:
        # 1) Считывание ввода
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return
        # -----------------
        # 2) Обновление состояния игры
        crosshair.move()
        target.move()
        # hitbox.x = 10
        # hitbox.y = 10
        # -----------------
        # 3) Отрисовка обновленного состояния
        background.draw()
        draw_score(target.hits_number)
        target.draw()
        crosshair.draw()
        pygame.display.update()
        # -----------------


if __name__ == '__main__':
    main()
