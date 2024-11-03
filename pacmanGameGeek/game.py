import random

import pygame as pg
import pygame_menu

pg.init()
W, H = 1000, 1000
display = pg.display.set_mode((W, H))
X, Y = 10, 10
count = 0
maze_1 = []
ghosts = []


def maze():
    global maze_1
    maze_1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]


def maze_random():
    maze_r = []
    for y in range(Y):
        maze_r.append([])
        for x in range(X):
            r = random.randint(0, 1)
            maze_r[y].append(r)
    return maze_r


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


class Ghosts(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, color: str):
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False
        self.vector = random.randint(0, 1)
        self.mov = random.randint(0, 1)

    def update(self):
        if self.vector == 0:
            if self.mov == 0:
                self.rect.x -= 3
            else:
                self.rect.x += 3
        else:
            if self.mov == 0:
                self.rect.y -= 3
            else:
                self.rect.y += 3

    def draw(self):
        if not self.dead:
            display.blit(self.image, self.rect)
        else:
            return


class Player(Sprite):
    def __init__(self):
        start_point = random.randint(0, 2)
        rects = []
        for y in range(10):
            for x in range(10):
                if maze_1[y][x] == 3:
                    pacman_y = ((y+1) * 100) - 50
                    pacman_x = ((x + 1) * 100) - 50
                    rects.append([pacman_x, pacman_y])
        super().__init__(rects[start_point][0], rects[start_point][1], 'img/pacman.png')
        self.image_ = self.image
        self.image_right = self.image
        self.image_left = pg.transform.flip(self.image, True, False)
        self.image_top = pg.image.load('img/pacman_top.png')
        self.image_bottom = pg.transform.flip(self.image_top, False, True)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        if not self.dead:
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
        else:
            show_end_screen()

    def draw(self):
        display.blit(self.image, self.rect)


def add_fruits(fruits):
    for y in range(10):
        for x in range(10):
            if maze_1[y][x] == 0:
                fruit_x = ((x+1)*100) - 50
                fruit_y = ((y + 1) * 100) - 50
                fruit = Fruit(fruit_x, fruit_y)
                fruits.add(fruit)


def add_ghosts():
    global ghosts
    count = 0
    rects = []
    colors = ['green', 'yellow', 'blue', 'orange', 'purple']
    while count < 5:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if maze_1[y][x] == 0:
                count += 1
                maze_1[y][x] = 2
                ghost_x = ((x+1) * 100) - 50
                ghost_y = ((y+1) * 100) - 50
                rects.append([ghost_x, ghost_y])
    ghost1 = Ghosts(rects[0][0], rects[0][1], colors[0])
    ghost2 = Ghosts(rects[1][0], rects[1][1], colors[1])
    ghost3 = Ghosts(rects[2][0], rects[2][1], colors[2])
    ghost4 = Ghosts(rects[3][0], rects[3][1], colors[3])
    ghost5 = Ghosts(rects[4][0], rects[4][1], colors[4])
    ghosts.clear()
    ghosts.append((ghost1, ghost2, ghost3, ghost4, ghost5))


def add_walls(walls):
    for y in range(10):
        for x in range(10):
            if maze_1[y][x] == 1:
                wall_x = (x+1)*100
                wall_y = (y+1)*100
                wall = Wall(wall_x, wall_y)
                walls.add(wall)


def collided_walls(pacman: Player):
    if pacman.image == pacman.image_left:
        pacman.speedx = 0
        pacman.rect.centerx += 10
    elif pacman.image == pacman.image_right:
        pacman.speedx = 0
        pacman.rect.centerx -= 10
    elif pacman.image == pacman.image_top:
        pacman.speedy = 0
        pacman.rect.centery += 10
    elif pacman.image == pacman.image_bottom:
        pacman.speedy = 0
        pacman.rect.centery -= 10


def remove_ghosts(ghost: Ghosts):
    if ghost.mov == 0:
        ghost.mov = 1
    else:
        ghost.mov = 0


def main():
    maze()
    pacman = Player()
    walls = pg.sprite.Group()
    fruits = pg.sprite.Group()
    add_ghosts()
    add_fruits(fruits)
    add_walls(walls)
    global count
    global ghosts
    count = 0
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return
        pacman.update()
        for ghost in ghosts[0]:
            ghost.update()
        walls.update()
        fruits.update()
        for ghost in ghosts[0]:
            if pacman.rect.colliderect(ghost.rect):
                pacman.kill()
        for ghost in ghosts[0]:
            if pg.sprite.spritecollide(ghost, walls, False):
                remove_ghosts(ghost)
        if pg.sprite.spritecollide(pacman, walls, False):
            collided_walls(pacman)
        if pg.sprite.spritecollide(pacman, fruits, True):
            count += 1
        if len(fruits) == 0:
            show_end_screen()
            return
        display.fill('black')
        pacman.draw()
        for ghost in ghosts[0]:
            ghost.draw()
        fruits.draw(display)
        walls.draw(display)
        pg.display.update()
        pg.time.delay(1000 // 60)


def show_end_screen():
    end_menu = pygame_menu.Menu('Игра окончена', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    end_menu.add.label(f'Всего очков: {count}', font_size=30)
    end_menu.add.button('Заново', main)
    end_menu.add.button('Выйти', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def show_start_screen():
    menu = pygame_menu.Menu('Pac-Man', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Начать', main)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(display)


if __name__ == "__main__":
    show_start_screen()
