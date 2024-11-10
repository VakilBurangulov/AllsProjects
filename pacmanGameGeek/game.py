import random

import pygame as pg
import pygame_menu

pg.init()
W, H = 1000, 1000
display = pg.display.set_mode((W, H))
pg.display.set_icon(pg.image.load('img/scooby.jpg'))
pg.display.set_caption('Scooby')
X, Y = 10, 10
count = 0
maze = []
ghosts = []
now_maze = None
all_count = 0


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

maze_2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

maze_3 = [
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

maze_4 = [
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

maze_5 = [
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


def maze_upload(x):
    global maze
    maze = x


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
        self.image = pg.image.load('img/wall.jpg')
        self.rect = self.image.get_rect(bottomright=(x, y))

    def draw(self):
        display.blit(self.image, self.rect)


class Fruit(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('img/food.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False

    def draw(self):
        if not self.dead:
            display.blit(self.image, self.rect)
        else:
            return


class Ghost(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/ghost.jpg')
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
                if maze[y][x] == 3:
                    pacman_y = ((y+1) * 100) - 50
                    pacman_x = ((x + 1) * 100) - 50
                    rects.append([pacman_x, pacman_y])
        super().__init__(rects[start_point][0], rects[start_point][1], 'img/scooby.jpg')
        self.image_ = self.image
        self.image_left = pg.transform.flip(self.image, True, False)
        self.vector = ''
        self.speedx = 0
        self.speedy = 0

    def update(self):
        if not self.dead:
            keys = pg.key.get_pressed()
            if keys[pg.K_a]:
                if self.rect.centerx > 0:
                    self.speedx = -3
                    self.speedy = 0
                    self.vector = 'left'
                    self.image = self.image_left
                else:
                    self.rect.centerx = 10
            elif keys[pg.K_d]:
                if self.rect.centerx < W:
                    self.speedx = 3
                    self.speedy = 0
                    self.vector = 'right'
                    self.image = self.image_
                else:
                    self.rect.centerx = W-10
            elif keys[pg.K_w]:
                if self.rect.centery > 0:
                    self.speedy = -3
                    self.speedx = 0
                    self.vector = 'bottom'
                else:
                    self.rect.centery = 10
            elif keys[pg.K_s]:
                if self.rect.centery < H:
                    self.speedy = 3
                    self.speedx = 0
                    self.vector = 'top'
                else:
                    self.rect.centery = H-10

            self.rect.x += self.speedx
            self.rect.y += self.speedy
        else:
            show_bad_end_screen()

    def draw(self):
        display.blit(self.image, self.rect)


class Portal(Sprite):
    def __init__(self):
        start_point = random.randint(0, 2)
        rects = []
        for y in range(10):
            for x in range(10):
                if maze[y][x] == 3:
                    pacman_y = ((y + 1) * 100) - 50
                    pacman_x = ((x + 1) * 100) - 50
                    rects.append([pacman_x, pacman_y])

        super().__init__(rects[start_point][0], rects[start_point][1], 'img/portal.jpg')
        self.on = False

    def draw(self):
        if self.on:
            display.blit(self.image, self.rect)


def add_fruits(fruits):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 0:
                fruit_x = ((x+1)*100) - 50
                fruit_y = ((y + 1) * 100) - 50
                fruit = Fruit(fruit_x, fruit_y)
                fruits.add(fruit)


def add_ghosts():
    count = 0
    rects = []
    while count < 5:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if maze[y][x] == 0:
                count += 1
                maze[y][x] = 2
                ghost_x = ((x+1) * 100) - 50
                ghost_y = ((y+1) * 100) - 50
                rects.append([ghost_x, ghost_y])
    ghost1 = Ghost(rects[0][0], rects[0][1])
    ghost2 = Ghost(rects[1][0], rects[1][1])
    ghost3 = Ghost(rects[2][0], rects[2][1])
    ghost4 = Ghost(rects[3][0], rects[3][1])
    ghost5 = Ghost(rects[4][0], rects[4][1])
    ghosts.clear()
    ghosts.append((ghost1, ghost2, ghost3, ghost4, ghost5))


def add_walls(walls):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 1:
                wall_x = (x+1)*100
                wall_y = (y+1)*100
                wall = Wall(wall_x, wall_y)
                walls.add(wall)


def collided_walls(pacman: Player):
    if pacman.vector == 'left':
        pacman.speedx = 0
        pacman.rect.centerx += 10
    elif pacman.vector == 'right':
        pacman.speedx = 0
        pacman.rect.centerx -= 10
    elif pacman.vector == 'bottom':
        pacman.speedy = 0
        pacman.rect.centery += 10
    elif pacman.vector == 'top':
        pacman.speedy = 0
        pacman.rect.centery -= 10


def remove_ghosts(ghost: Ghost):
    if ghost.mov == 0:
        ghost.mov = 1
    else:
        ghost.mov = 0


def count_update():
    global all_count
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 0:
                all_count += 1
    print(all_count)


def main(x):
    global now_maze, count, ghosts, all_count
    now_maze = x
    all_count = 0
    maze_upload(x)
    pacman = Player()
    portal = Portal()
    walls = pg.sprite.Group()
    fruits = pg.sprite.Group()
    add_ghosts()
    add_fruits(fruits)
    add_walls(walls)
    count_update()
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
        if portal.on:
            if pacman.rect.colliderect(portal.rect):
                show_good_end_screen()
                return
        for ghost in ghosts[0]:
            if pacman.rect.colliderect(ghost.rect):
                show_bad_end_screen()
                return
        for ghost in ghosts[0]:
            if pg.sprite.spritecollide(ghost, walls, False):
                remove_ghosts(ghost)
        if pg.sprite.spritecollide(pacman, walls, False):
            collided_walls(pacman)
        if pg.sprite.spritecollide(pacman, fruits, True):
            count = all_count - len(fruits)
        if len(fruits) == 0:
            portal.on = True
        display.fill('black')
        pacman.draw()
        for ghost in ghosts[0]:
            ghost.draw()
        fruits.draw(display)
        walls.draw(display)
        portal.draw()
        pg.display.update()
        pg.time.delay(1000 // 60)


def show_bad_end_screen():
    end_menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    end_menu.add.label(f'Ты проиграл', font_size=30)
    end_menu.add.label(f'Всего очков: {count}', font_size=30)
    end_menu.add.button('Главное меню', show_start_screen)
    end_menu.add.button('Заново', main, now_maze)
    end_menu.add.button('Выйти', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def show_good_end_screen():
    end_menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    end_menu.add.label(f'Ты выиграл', font_size=30)
    end_menu.add.label(f'Всего очков: {count}', font_size=30)
    end_menu.add.button('Главное меню', show_start_screen)
    end_menu.add.button('Заново', main, now_maze)
    end_menu.add.button('Выйти', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def show_start_screen():
    menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Уровень 1', main, maze_1)
    menu.add.button('Уровень 2', main, maze_2)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(display)


if __name__ == "__main__":
    show_start_screen()
