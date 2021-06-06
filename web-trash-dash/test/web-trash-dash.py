import pygame
import random


class Player:
    position = pygame.Vector2()
    position.xy = 100, 400
    velocity = pygame.Vector2()
    velocity.xy = 0, 0
    speed = 2
    # drag = 0.1
    frame = 0
    costume = 0
    walk = [pygame.image.load("assets/gfx/walking/Dino R1.png"), pygame.image.load("assets/gfx/walking/Dino R2.png"),
            pygame.image.load("assets/gfx/walking/Dino R3.png"), pygame.image.load("assets/gfx/walking/Dino R4.png"),
            pygame.image.load("assets/gfx/walking/Dino R5.png"), pygame.image.load("assets/gfx/walking/Dino R6.png")]
    idle = pygame.image.load("assets/gfx/dino.png")
    duck_walk = [pygame.image.load("assets/gfx/DuckDino/Duck R1.png"), pygame.image.load(
        "assets/gfx/DuckDino/Duck R2.png"),
                 pygame.image.load("assets/gfx/DuckDino/Duck R3.png"), pygame.image.load(
            "assets/gfx/DuckDino/Duck R4.png"),
                 pygame.image.load("assets/gfx/DuckDino/Duck R5.png"), pygame.image.load(
            "assets/gfx/DuckDino/Duck R6.png")]
    duck_idle = pygame.image.load("assets/gfx/DuckDino/Duck Idle.png")
    robo_walk = [pygame.image.load("assets/gfx/RoboDino/ROBO R1.png"), pygame.image.load(
        "assets/gfx/RoboDino/ROBO R2.png"),
                 pygame.image.load("assets/gfx/RoboDino/ROBO R3.png"), pygame.image.load(
            "assets/gfx/RoboDino/ROBO R4.png"),
                 pygame.image.load("assets/gfx/RoboDino/ROBO R5.png"), pygame.image.load(
            "assets/gfx/RoboDino/ROBO R6.png")]
    robo_idle = pygame.image.load("assets/gfx/RoboDino/Dino Bot Idle.png")
    rightSprite = idle
    rightSprite = pygame.transform.scale(rightSprite, (60, 60))
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite

    def animate(self):
        if self.frame >= len(self.walk):
            self.frame = 0

        if self.costume == 0:
            self.rightSprite = self.walk[self.frame]
        if self.costume == 1:
            self.rightSprite = self.robo_walk[self.frame]
        elif self.costume == 2:
            self.rightSprite = self.duck_walk[self.frame]

        self.rightSprite = pygame.transform.scale(self.rightSprite, (60, 60))
        self.leftSprite = pygame.transform.flip(self.rightSprite, True, False)
        self.frame += 1

    def reset(self):
        if self.costume == 0:
            self.rightSprite = self.idle
        if self.costume == 1:
            self.rightSprite = self.robo_idle
        elif self.costume == 2:
            self.rightSprite = self.duck_idle

        self.rightSprite = pygame.transform.scale(self.rightSprite, (60, 60))
        self.leftSprite = pygame.transform.flip(self.rightSprite, True, False)



class Trash:
    trashSprites = [pygame.image.load("assets/gfx/appleCore.png"), pygame.image.load("assets/gfx/soda.png")]

    def __init__(self, screenheight):
        self.screenheight = screenheight
        self.size = random.randrange(20, 30)
        self.sprite = self.trashSprites[random.randint(0, len(self.trashSprites)-1)]
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        self.sprite = pygame.transform.rotate(self.sprite, random.randrange(0, 360))
        self.position = pygame.Vector2()
        self.position.xy = random.randrange(370, 1100), random.randrange(-500, -50)
        self.speed = random.randrange(5, 10) / 10

    def fall(self):
        if self.position.y < self.screenheight:
            self.position.y += self.speed
        else:
            self.__init__(self.screenheight)


def check_collision_list(a, b):
    return (a[0] + a[2] > b[0]) and (a[0] < b[0] + b[2]) and (a[1] + a[3] > b[1]) and (a[1] < b[1] + b[3])


def main():
    # start pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 640))
    # pygame.display.set_caption("Trash dash")

    title_screen = pygame.image.load("assets/gfx/TitleScreen.png")
    title_screen = pygame.transform.scale(title_screen, (1280, 640))

    hud_icon_size = 60
    trash_pile = pygame.image.load("assets/gfx/soda.png")
    trash_pile = pygame.transform.scale(trash_pile, (hud_icon_size, hud_icon_size))
    coin = pygame.image.load("assets/gfx/coin.png")
    coin = pygame.transform.scale(coin, (hud_icon_size, hud_icon_size))
    timer_icon = pygame.image.load("assets/gfx/hourglass-icon.png")
    timer_icon = pygame.transform.scale(timer_icon, (hud_icon_size, hud_icon_size))
    backpack_icon = pygame.image.load("assets/gfx/backpack-icon.png")
    backpack_icon = pygame.transform.scale(backpack_icon, (hud_icon_size, hud_icon_size))

    score_font = pygame.font.Font("assets/Fonts/Press_Start_2P/PressStart2P-Regular.ttf", 50)
    score_color = (191, 69, 69)
    trash_text = score_font.render(str(0), True, score_color)
    score_text = score_font.render(str(0), True, score_color)
    backpack_text = score_font.render(str(10), True, score_color)
    score_holder = pygame.Rect(10, 550, 600, 80)
    barriers = [(0, 0, 320, 200), (100, 200, 70, 130)]
    shop_hitbox = (100, 230, 70, 70)

    # Load assets for inside
    upgrades_font = pygame.font.Font("assets/Fonts/Press_Start_2P/PressStart2P-Regular.ttf", 18)
    upgrade_text_color = (36, 36, 36)
    start_button = (985, 435, 205, 90)
    start_text = upgrades_font.render("Next day", True, upgrade_text_color)
    quit_button = (985, 320, 205, 90)
    quit_text = upgrades_font.render("Quit", True, (181, 23, 2))
    inside = pygame.image.load("assets/gfx/inside.png")
    inside = pygame.transform.scale(inside, (1280, 640))
    winScreen = pygame.image.load("assets/gfx/WinScreen.png")
    winScreen = pygame.transform.scale(winScreen, (1280, 640))
    GameWon = False
    winButton = (825, 255, 100, 55)
    backpack_button = (435, 255, 100, 55)
    speed_button = (570, 255, 100, 55)
    atm_button = (700, 255, 100, 55)
    selected_icon = (94, 71, 13, 13)
    costume1 = (72, 263, 71, 38)
    costume2 = (185, 263, 71, 38)
    costume3 = (299, 263, 71, 38)

    trash_collected = 0
    prev_trash = 0
    balance = 0
    trash_price = 5
    backpack = 10

    running = False

    begin_button = (328, 191, 746, 72)
    screen.blit(title_screen, (0, 0))
    # pygame.draw.rect(screen, (0, 0, 0), begin_button)
    pygame.display.update()
    on_title = True

    while on_title:
        clock.tick(8)
        select = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                select = True
        if select:
            mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3, 3)
            if check_collision_list(mouse_pos, begin_button):
                # select_sound.play()
                on_title = False

    while True:
        while not running:
            clock.tick(10)
            select = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    select = True

            if select:
                mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3, 3)
                if check_collision_list(mouse_pos, start_button):
                    running = True
                elif check_collision_list(mouse_pos, quit_button):
                    pygame.time.wait(int(select_sound.get_length()*1000))
                    pygame.quit()
                    return
                elif check_collision_list(mouse_pos, speed_button):
                    if dino.speed < 10 and balance >= dino.speed * 20:
                        balance -= dino.speed * 20
                        dino.speed += 1
                        score_text = score_font.render(str(balance), True, score_color)
                elif check_collision_list(mouse_pos, backpack_button):
                    if backpack < 30 and balance >= backpack * 3:
                        balance -= backpack * 3
                        backpack += 5
                        score_text = score_font.render(str(balance), True, score_color)
                        backpack_text = score_font.render(str(backpack), True, score_color)
                elif check_collision_list(mouse_pos, atm_button):
                    if trash_price < 20 and balance >= trash_price * 10:
                        balance -= trash_price * 10
                        trash_price += 2
                        score_text = score_font.render(str(balance), True, score_color)
                elif check_collision_list(mouse_pos, costume1):
                    selected_icon = (94, 71, 13, 13)
                    dino.costume = 0
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, costume2):
                    selected_icon = (215, 71, 13, 13)
                    dino.costume = 1
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, costume3):
                    selected_icon = (329, 71, 13, 13)
                    dino.costume = 2
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, winButton):
                        GameWon = True
                        pygame.time.delay(10)
                        screen.blit(winScreen, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(50)
                        if not GameWon:
                            balance -= 1000

            screen.blit(inside, (0, 0))
            pygame.draw.rect(screen, (13, 219, 67), selected_icon)
            # pygame.draw.rect(screen, (13, 219, 67), costume3)
            screen.blit(quit_text, (1050, 363))
            screen.blit(start_text, (1010, 474))

            # pygame.draw.rect(screen, (13, 219, 67), backpack_button, 0, 20)
            screen.blit(upgrades_font.render(str(backpack*3), True, score_color), (462, 272))
            # pygame.draw.rect(screen, (13, 219, 67), speed_button, 0, 20)
            screen.blit(upgrades_font.render(str((dino.speed * 20)), True, score_color), (595, 272))
            # pygame.draw.rect(screen, (13, 219, 67), atm_button, 0, 20)
            screen.blit(upgrades_font.render(str((trash_price * 10)), True, score_color), (728, 272))
            # pygame.draw.rect(screen, (13, 219, 67), winButton)
            if not GameWon:
                screen.blit(upgrades_font.render(str(1000), True, score_color), (846, 272))
            # box_text(screen, fact_font, 1000, 1190, 90, fact, score_color)
            pygame.draw.rect(screen, (38, 24, 24), score_holder, 0, 10)
            screen.blit(trash_pile, (20, 560))
            screen.blit(trash_text, (80, 567))
            screen.blit(coin, (200, 560))
            screen.blit(score_text, (270, 567))
            screen.blit(backpack_icon, (450, 560))
            screen.blit(backpack_text, (510, 567))

            pygame.display.update()


if __name__ == "__main__":
    main()
