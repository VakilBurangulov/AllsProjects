import random

import pygame as pg
import pygame_menu

pg.init()
W, H = 720, 480
display = pg.display.set_mode((W, H))
GAP = 234/2
W_C, H_C = 234, 333
Public_Domain = ['diamonds', 'hearts', 'clubs', 'spades']


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        super().update()

    def draw(self):
        display.blit(self.image, self.rect)


class Two(Sprite):
    def __init__(self, x, y, domain):
        self.domain = domain
        if self.domain == 'diamonds':
            image_path = 'img/diamonds/diamonds_2.png'
        elif self.domain == 'hearts':
            image_path = 'img/hearts/hearts_2.png'
        elif self.domain == 'clubs':
            image_path = 'img/clubs/clubs_2.png'
        elif self.domain == 'spades':
            image_path = 'img/spades/spades_2.png'
        self.image_path = image_path
        super().__init__(x, y, self.image_path)


twoes = pg.sprite.Group

for i in Public_Domain:
    domain = i
    y = H - 333 / 2
    x = random.randint(0 + W_C, W - W_C)
    two = Two(x, y, domain)
    twoes.add(two)


def main():
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return

        twoes.update()

        display.fill('white')
        twoes.draw()
        pg.display.update()


if __name__ == '__main__':
    main()

