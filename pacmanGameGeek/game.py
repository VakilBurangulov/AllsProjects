import datetime
import random


import pygame as pg
import pygame_menu

pg.init()
W, H = 1000, 1000
display = pg.display.set_mode((W, H))
X, Y = 10, 10
count = 0
time = None
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# maze = []
# for y in range(Y):
#     maze.append([])
#     for x in range(X):
#         r = random.randint(0, 1)
#         maze[y].append(r)


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False

    def kill(self):
        self.dead = True
        super().kill()


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((100, 100))
        self.image.fill('white')
        self.rect = self.image.get_rect(bottomright=(x, y))

    def draw(self):
        display.blit(self.image, self.rect)


class Fruit(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False

    def draw(self):
        if not self.dead:
            display.blit(self.image, self.rect)
        else:
            return


class Player(Sprite):
    def __init__(self):
        super().__init__(150, 150, 'img/pacman.png')
        self.image_ = self.image
        self.image_right = self.image
        self.image_left = pg.transform.flip(self.image, True, False)
        self.image_top = pg.image.load('img/pacman_top.png')
        self.image_bottom = pg.transform.flip(self.image_top, False, True)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            if self.rect.centerx > 0:
                self.speedx = -3
                self.speedy = 0
                self.image = self.image_left
            else:
                self.rect.centerx = 10
        elif keys[pg.K_d]:
            if self.rect.centerx < W:
                self.speedx = 3
                self.speedy = 0
                self.image = self.image_right
            else:
                self.rect.centerx = W-10
        elif keys[pg.K_w]:
            if self.rect.centery > 0:
                self.speedy = -3
                self.speedx = 0
                self.image = self.image_top
            else:
                self.rect.centery = 10
        elif keys[pg.K_s]:
            if self.rect.centery < H:
                self.speedy = 3
                self.speedx = 0
                self.image = self.image_bottom
            else:
                self.rect.centery = H-10

        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self):
        display.blit(self.image, self.rect)


def add_fruits(fruits):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 0:
                fruit_x = ((x+1)*100) - 50
                fruit_y = ((y + 1) * 100) - 50
                fruit = Fruit(fruit_x, fruit_y)
                fruits.add(fruit)


def add_walls(walls):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 1:
                wall_x = (x+1)*100
                wall_y = (y+1)*100
                wall = Wall(wall_x, wall_y)
                walls.add(wall)


def collided_walls(pacman: Player):
    if pacman.image == pacman.image_left:
        pacman.speedx = 0
    elif pacman.image == pacman.image_right:
        pacman.speedx = 0
    elif pacman.image == pacman.image_top:
        pacman.speedy = 0
    elif pacman.image == pacman.image_bottom:
        pacman.speedy = 0


def main():
    pacman = Player()
    walls = pg.sprite.Group()
    fruits = pg.sprite.Group()
    add_fruits(fruits)
    add_walls(walls)
    global count
    count = 0
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return

        pacman.update()
        walls.update()
        fruits.update()
        if pg.sprite.spritecollide(pacman, walls, False):
            collided_walls(pacman)
        if pg.sprite.spritecollide(pacman, fruits, True):
            count += 1
        if len(fruits) == 0:
            show_end_screen()
            return
        display.fill('black')
        pacman.draw()
        fruits.draw(display)
        walls.draw(display)
        pg.display.update()
        pg.time.delay(1000 // 60)


def show_end_screen():
    end_menu = pygame_menu.Menu('Игра окончена', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    end_menu.add.label(f'Всего очков: {count}', font_size=30)
    end_menu.add.button('Заново', main)
    end_menu.add.button('Выйти', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def show_start_screen():
    menu = pygame_menu.Menu('Pac-Man', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Начать', main)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(display)


if __name__ == "__main__":
    show_start_screen()
