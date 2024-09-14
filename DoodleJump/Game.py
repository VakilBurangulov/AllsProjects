import random
import pygame as pg
import pygame_menu

pg.init()
W, H = 480, 640
display = pg.display.set_mode((W, H))
GRAVITY = 1
JUMP = -30
PLATFORM_WIDTH = 105
MIN_GAP = 90
MAX_GAP = 180
score = 0
font_name = pg.font.match_font('Comic Sans', True, False)
font = pg.font.Font(font_name, size=36)


def draw_text(text: str, x, y):
    score_text = font.render(text, True, (0, 0, 0))
    display.blit(score_text, (x, y))


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False




    def kill(self):
        self.dead = True
        super().kill()


class Player(Sprite):
    def __init__(self):
        super().__init__(W // 2, H // 4, 'img/doodle_left.png')
        self.image_left = self.image
        self.image_right = pg.transform.flip(self.image_left, True, False)
        self.image_hat_top = pg.image.load('img/doodle_hat_top.png')
        self.image_hat_top_right = pg.transform.flip(self.image_hat_top, True, False)
        self.image_hat_left = pg.image.load('img/doodle_hat_left.png')
        self.image_hat_right = pg.transform.flip(self.image_hat_left, True, False)
        self.speed = 0
        self.usebonus = False
        self.Hat = False

    def update(self):
        if self.dead:
            show_end_screen()

            return
        keys = pg.key.get_pressed()
        if self.usebonus:
            if self.Hat:
                if keys[pg.K_a]:
                    self.rect.x -= 5
                    self.image = self.image_hat_left
                if keys[pg.K_d]:
                    self.rect.x += 5
                    self.image = self.image_hat_right
                if not keys[pg.K_a] and not keys[pg.K_d]:
                    if self.image == self.image_hat_right:
                        self.image = self.image_hat_top_right
                    if self.image == self.image_hat_left:
                        self.image = self.image_hat_top
                if self.rect.left > W:
                    self.rect.left = 0
                if self.rect.right < 0:
                    self.rect.left = W
                self.speed += GRAVITY
                self.rect.y += self.speed
                if self.rect.y > H:
                    self.kill()
        if not self.usebonus:
            if keys[pg.K_a]:
                self.rect.x -= 5
                self.image = self.image_left
            if keys[pg.K_d]:
                self.rect.x += 5
                self.image = self.image_right
            if self.rect.left > W:
                self.rect.left = 0
            if self.rect.right < 0:
                self.rect.left = W
            self.speed += GRAVITY
            self.rect.y += self.speed
            if self.rect.y > H:
                self.kill()

    def draw(self):
        if self.dead:
            draw_text('Game over', W//2-70, H//2-10)
        else:
            display.blit(self.image, self.rect)


doodle = Player()


class BasePlatform(Sprite):
    def on_collision(self, player):
        if not player.usebonus:
            player.speed = JUMP

    def update(self):
        super().update()
        if self.rect.top > H:
            self.kill()
            spawn_platform()

    def attach_bonus(self):
        if random.randint(0, 100) > 90:
            Bonus = random.choice([Spring, Hat, JetPack])
            obj = Bonus(self)
            platforms.add(obj)


class NormalPlatform(BasePlatform):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/green.png')


class SpringPlatform(BasePlatform):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/purple.png')

    def on_collision(self, player):
        if not player.usebonus:
            player.speed = 2*JUMP


class BreakablePlatform(BasePlatform):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/red.png')
        self.image_broken = pg.image.load('img/red_broken.png')
        self.breakble = False

    def on_collision(self, player):
        if not player.usebonus:
            if not self.breakble:
                player.speed = JUMP
                self.image = self.image_broken
                self.breakble = True


class MovingPlatform(BasePlatform):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/blue.png')
        self.direction = random.randint(0, 1)

    def update(self):
        super().update()
        if self.direction == 1:
            self.rect.x += 3
        if self.direction == 0:
            self.rect.x -= 3
        if self.rect.right > W:
            self.direction = 0
        if self.rect.left < 0:
            self.direction = 1
        if self.rect.top > H:
            self.kill()
            spawn_platform()


platforms = pg.sprite.Group()


def spawn_platform():
    platform = platforms.sprites()[-1]
    y = platform.rect.y - random.randint(MIN_GAP, MAX_GAP)
    x = random.randint(0 + PLATFORM_WIDTH, W - PLATFORM_WIDTH)
    types = [
        NormalPlatform,
        SpringPlatform,
        BreakablePlatform,
        MovingPlatform
    ]

    plat = random.choice(types)
    platform = plat(x, y)
    platform.attach_bonus()
    platforms.add(platform)


platform = NormalPlatform(W // 2 - PLATFORM_WIDTH // 2, H - 50)
platforms.add(platform)


def is_top_collision(player: Player, platform: BasePlatform):
    if player.rect.colliderect(platform.rect):
        if player.speed > 0:
            if player.rect.bottom < platform.rect.bottom:
                platform.on_collision(player)


class BaseBonus(Sprite):
    def __init__(self, image_path, plat: BasePlatform):
        img = pg.image.load(image_path)
        w = img.get_width()
        h = img.get_height()
        rect = plat.rect
        x = random.randint(rect.left + w // 2, rect.right - w // 2)
        y = rect.top - h // 2
        super().__init__(x, y, image_path)
        self.platform = plat
        self.dx = self.rect.x - self.platform.rect.x

    def on_collision(self, player):
        global score
        score += 1000
        self.kill()

    def update(self):
        self.rect.x = self.platform.rect.x + self.dx
        if self.platform.dead:
            self.kill


class Spring(BaseBonus):
    def __init__(self, plat):
        super().__init__('img/spring.png', plat)

    def on_collision(self, player):
        player.speed = - 50
        self.image = pg.image.load('img/spring_1.png')


class Hat(BaseBonus):
    def __init__(self, plat):
        super().__init__('img/hat_top.png', plat)
        self.player = doodle
        self.use = False

    def on_collision(self, player):
        self.use = True
        player.Hat = True
        player.usebonus = True
        player.speed = -500

    def update(self):
        if self.use:
            if self.player.speed > -100:
                self.player.usebonus = False
                self.player.Hat = False
                self.use = False
                self.player.image = pg.image.load('img/doodle_left.png')
                self.kill()
                print(self.player.Hat)




class JetPack(BaseBonus):
    def __init__(self, plat):
        super().__init__('img/jetpack_0.png', plat)
        self.image_left = pg.image.load('img/jetpack_1.png')
        self.image_right = pg.transform.flip(self.image_left, True, False)
        self.player = doodle
        self.use = False

    def on_collision(self, player):
        player.speed = -300
        self.image = pg.image.load('img/jetpack_1.png')
        self.use = True

    def update(self):
        super().update()
        if self.use:

            self.rect = self.image.get_rect(bottomleft=(self.player.rect.top, self.player.rect.left))
            if self.player.speed < -100:
                keys = pg.key.get_pressed()
                if keys[pg.K_a]:
                    self.rect.x -= 5
                    self.image = self.image_left
                if keys[pg.K_d]:
                    self.rect.x += 5
                    self.image = self.image_right
            else:
                self.kill()


class BaseEnemy(Sprite):
    def update(self):
        if self.rect.y > H:
            self.kill()

    def on_collision(self, player):
        if player.speed >= -30:
            player.kill()


class Hole(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/hole.png')


class Left_Right_Enemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/enemy_l_r.png')
        self.direction = random.randint(0, 1)

    def update(self):
        if self.direction == 1:
            self.rect.x += 3
        if self.direction == 0:
            self.rect.x -= 3
        if self.rect.right > W:
            self.direction = 0
        if self.rect.left < 0:
            self.direction = 1


class Ud_Down_Enemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, 'img/enemy_l_r.png')
        self.direction = random.randint(0, 1)

    def update(self):
        if self.direction == 1:
            self.rect.y -= 3
        if self.direction == 0:
            self.rect.y += 3
        if self.rect.right > H:
            self.direction = 1
        if self.rect.left < 0:
            self.direction = 0


enemies = pg.sprite.Group()


def spawn_enemy(delay):
    if delay > 5000:
        delay = 0
        type = [
            Hole,
            Left_Right_Enemy,
            Ud_Down_Enemy,

        ]
        Enemy = random.choice(type)
        x = random.randint(0, W-80)
        e = Enemy(x, -H)
        enemies.add(e)
    return delay


def main():
    doodle = Player()
    global score
    score = 0
    passed_time = 0
    while True:

        # 1
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return
        # 2
        doodle.update()
        enemies.update()
        platforms.update()

        hit_enemy = pg.sprite.spritecollide(doodle, enemies, True)
        if hit_enemy:

            doodle.kill()
        if pg.sprite.spritecollide(doodle, platforms, False, collided=is_top_collision):
            doodle.speed = JUMP
        if len(enemies) > 1:
            x = random.randint(0, len(enemies)-1)
            list(enemies)[x].kill()
        if len(platforms) < 25:
            spawn_platform()
        if passed_time > 5:
            spawn_enemy(passed_time)
        if doodle.speed < 0 and doodle.rect.bottom < H / 2:
            doodle.rect.y -= doodle.speed

            score += 1
            for platform in platforms:
                platform.rect.y -= doodle.speed
            for e in enemies:
                e.rect.y -= doodle.speed
            passed_time = spawn_enemy(passed_time)
        # 3
        display.fill('white')
        platforms.draw(display)
        enemies.draw(display)
        doodle.draw()
        pg.display.update()
        passed_time += pg.time.delay(1000 // 60)


def show_end_screen():
    end_menu = pygame_menu.Menu('Игра окончена', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    end_menu.add.label(f'Всего очков: {score}', font_size=30)
    end_menu.add.button('Заново', main)
    end_menu.add.button('Выйти', pygame_menu.events.EXIT)
    end_menu.mainloop(display)


def show_start_screen():
    menu = pygame_menu.Menu('Doodle Jump', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Начать', main)
    menu.add.button('Выйти', pygame_menu.events.EXIT)
    menu.mainloop(display)


if __name__ == '__main__':
    show_start_screen()
    main()
