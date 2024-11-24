import pygame as pg
import pygame_menu

import random

pg.init()

W, H = 1000, 1000
display = pg.display.set_mode((W, H))
maze = []
all_counts = 0
count = 0
now_maze = []
level_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

level_4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def maze_upload(c):
    global maze
    maze = c


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, img_path):
        super().__init__()
        self.image = pg.image.load(img_path)
        self.rect = self.image.get_rect(center=(x, y))
        
    def draw(self):
        display.blit(self.image, self.rect)
        

class Player(Sprite):
    def __init__(self):
        rects = []
        for y in range(10):
            for x in range(10):
                if maze[y][x] == 3:
                    rects.append([((x+1) * 100) - 50, ((y+1) * 100) - 50])
        rect = random.choice(rects)
        super().__init__(rect[0], rect[1], 'img/scooby.jpg')
        self.image_ = self.image
        self.image_left = pg.transform.flip(self.image_, True, False)
        self.image_right = self.image_
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity_y = -3
            self.velocity_x = 0
        elif keys[pg.K_s]:
            self.velocity_y = 3
            self.velocity_x = 0
        elif keys[pg.K_a]:
            self.image = self.image_left
            self.velocity_y = 0
            self.velocity_x = -3
        elif keys[pg.K_d]:
            self.image = self.image_right
            self.velocity_y = 0
            self.velocity_x = 3

        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x
        
        
class Wall(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/wall.jpg')
        
        
class Food(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/food.png')
        

class Ghost(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/ghost.jpg')
        self.vector = random.randint(0, 1)
        self.move = random.randint(0, 1)

    def kill(self):
        upload_move(self)

    def update(self):
        if self.vector == 0:
            if self.move == 0:
                self.rect.y -= 3
            else:
                self.rect.y += 3
        else:
            if self.move == 0:
                self.rect.x -= 3
            else:
                self.rect.x += 3


class Portal(Sprite):
    def __init__(self):
        rects = []
        for y in range(10):
            for x in range(10):
                if maze[y][x] == 3:
                    rects.append([((x + 1) * 100) - 50, ((y + 1) * 100) - 50])
        rect = random.choice(rects)
        super().__init__(rect[0], rect[1], 'img/portal.jpg')
        self.on = False

    def draw(self):
        if self.on:
            super().draw()

    def update(self, player: Player):
        if self.on:
            if player.rect.colliderect(self.rect):
                show_good_end_screen()


def upload_move(ghost):
    if ghost.move == 0:
        ghost.move = 1
    else:
        ghost.move = 0


def add_food(foods):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 0:
                food_y = ((y+1) * 100) - 50
                food_x = ((x+1) * 100) - 50
                food = Food(food_x, food_y)
                foods.add(food)


def add_wall(walls):
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 1:
                wall_y = ((y+1) * 100) - 50
                wall_x = ((x+1) * 100) - 50
                wall = Wall(wall_x, wall_y)
                walls.add(wall)


def add_ghost(ghosts):
    ghost_count = 0
    while ghost_count < 5:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if maze[y][x] == 0:
            ghost_count += 1
            maze[y][x] = 2
            ghost_y = ((y+1) * 100) - 50
            ghost_x = ((x+1) * 100) - 50
            ghost = Ghost(ghost_x, ghost_y)
            ghosts.add(ghost)


def update_all_count():
    global all_counts
    all_counts = 0
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 0:
                all_counts += 1


def collide_player_and_wall(player: Player):
    if player.velocity_y == 3:
        player.velocity_y = 0
        player.rect.y -= 10
    elif player.velocity_y == -3:
        player.velocity_y = 0
        player.rect.y += 10
    elif player.velocity_x == 3:
        player.velocity_x = 0
        player.rect.x -= 3
    else:
        player.velocity_x = 0
        player.rect.x += 3


def main(x):
    global all_counts, count, now_maze
    maze_upload(x)
    now_maze = x
    count = 0
    player = Player()
    portal = Portal()
    ghosts = pg.sprite.Group()
    foods = pg.sprite.Group()
    walls = pg.sprite.Group()
    add_ghost(ghosts)
    update_all_count()
    add_food(foods)
    add_wall(walls)
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return
        player.update()
        portal.update(player)
        ghosts.update()
        foods.update()
        walls.update()

        if pg.sprite.spritecollide(player, foods, True):
            count = all_counts - len(foods)
        if pg.sprite.spritecollide(player, ghosts, False):
            show_bad_end_screen()
        pg.sprite.groupcollide(ghosts, walls, True, False)
        if pg.sprite.spritecollide(player, walls, False):
            collide_player_and_wall(player)
        if len(foods) == 0:
            portal.on = True

        display.fill('black')
        player.draw()
        portal.draw()
        ghosts.draw(display)
        foods.draw(display)
        walls.draw(display)

        pg.display.update()
        pg.time.delay(1000//60)


def show_good_end_screen():
    menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.label(f'You win', font_size=30)
    menu.add.label(f'Your score: {count}/{all_counts}', font_size=30)
    menu.add.button('Again', main, now_maze)
    menu.add.button('Main menu', show_start_screen)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(display)


def show_start_screen():
    menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Level 1', main, level_1)
    menu.add.button('Level 2', main, level_2)
    menu.add.button('Level 3', main, level_3)
    menu.add.button('Level 4', main, level_4)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(display)


def show_bad_end_screen():
    menu = pygame_menu.Menu('Scooby', 300, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.label(f'You lose', font_size=30)
    menu.add.label(f'Your score: {count}/{all_counts}', font_size=30)
    menu.add.button('Again', main, now_maze)
    menu.add.button('Main menu', show_start_screen)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(display)


if __name__ == '__main__':
    show_start_screen()
