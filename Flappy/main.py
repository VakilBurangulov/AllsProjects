import random
import pygame as pg
import pygame_menu

pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
PIPE_WIDTH = 80
PIPE_GAP = 250
SPEED = 5
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score = 0
font = pg.font.Font(None, 36)
pg.display.set_caption("Flappy Bird")

def draw_score():
    score_text = font.render(f"Score:{score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


def caption_score():
    pg.display.set_caption(f'Flappy Bird Score: {score}')


class Bird(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('res/bird.png')
        self.image = pg.transform.scale(self.image, size=[BIRD_WIDTH, BIRD_HEIGHT])
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        self.sprite_copy = self.image
        self.gravity = 1
        self.lift = -15
        self.velocity = 0

    def update(self):
        self.image = pg.transform.rotate(self.sprite_copy, -self.velocity)
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = self.lift


class Pipe(pg.sprite.Sprite):
    TOP = 1
    BOTTOM = 2

    def __init__(self, type, gap_start):
        super().__init__()
        self.image = pg.image.load('res/pipe.png')
        self.image = pg.transform.scale(self.image, [PIPE_WIDTH, self.image.get_height() / 2])
        if type == self.TOP:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottomleft=(SCREEN_WIDTH, gap_start))

        elif type == self.BOTTOM:
            self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH, gap_start + PIPE_GAP))
        self.passed = False

    def update(self):
        self.rect.x -= SPEED
        if self.rect.right < 0:
            self.kill()


def make_pipes():
    gap_start = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
    top_pipe = Pipe(Pipe.TOP, gap_start)
    bottom_pipe = Pipe(Pipe.BOTTOM, gap_start)
    pipes.add(top_pipe, bottom_pipe)


# bird = Bird()
pipes = pg.sprite.Group()


# make_pipes()


def main():
    global score
    score = 0
    bird = Bird()
    pipes.empty()
    make_pipes()
    clock = pg.time.Clock()
    while True:

        # 1
        events = pg.event.get()
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    bird.jump()

            if e.type == pg.QUIT:
                return
        # 2

        bird.update()
        pipes.update()
        if pipes.sprites()[-1].rect.x <= SCREEN_WIDTH / 2:
            make_pipes()
        for p in pipes:
            if p.rect.right < bird.rect.left and not p.passed:
                p.passed = True
                score += 0.5

        collisions = pg.sprite.spritecollide(bird, pipes, False)
        if collisions:
            show_end_screen()
            return
        # 3
        screen.fill(WHITE)
        pipes.draw(screen)
        draw_score()
        caption_score()
        screen.blit(bird.image, bird.rect)
        pg.time.delay(30)
        pg.display.update()


def show_end_screen():
    end_menu = pygame_menu.Menu('Game over', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    end_menu.add.label(f'Total score: {score}', font_size=30)
    end_menu.add.button('Again', main)
    end_menu.add.button('Exit', pygame_menu.events.EXIT)
    end_menu.mainloop(screen)


def show_start_screen():
    menu = pygame_menu.Menu('Hello', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Start', main)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


if __name__ == '__main__':
    show_start_screen()
    main()
