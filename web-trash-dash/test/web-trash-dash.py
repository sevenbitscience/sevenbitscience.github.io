import pygame


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
                pygame.quit()
                break

    while True:
        while not running:
            select = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    select = True

            if select:
                mouse_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3, 3)
                if check_collision_list(mouse_pos, start_button):
                    # select_sound.play()
                    running = True
                elif check_collision_list(mouse_pos, quit_button):
                    select_sound.play()
                    pygame.time.wait(int(select_sound.get_length()*1000))
                    return
                elif check_collision_list(mouse_pos, speed_button):
                    if dino.speed < 10 and balance >= dino.speed * 20:
                        # select_sound.play()
                        balance -= dino.speed * 20
                        dino.speed += 1
                        score_text = score_font.render(str(balance), True, score_color)
                    else:
                        full_sound.play()
                elif check_collision_list(mouse_pos, backpack_button):
                    if backpack < 30 and balance >= backpack * 3:
                        # select_sound.play()
                        balance -= backpack * 3
                        backpack += 5
                        score_text = score_font.render(str(balance), True, score_color)
                        backpack_text = score_font.render(str(backpack), True, score_color)
                    else:
                        full_sound.play()
                elif check_collision_list(mouse_pos, atm_button):
                    if trash_price < 20 and balance >= trash_price * 10:
                        # select_sound.play()
                        balance -= trash_price * 10
                        trash_price += 2
                        score_text = score_font.render(str(balance), True, score_color)
                    else:
                        full_sound.play()
                elif check_collision_list(mouse_pos, costume1):
                    # select_sound.play()
                    selected_icon = (94, 71, 13, 13)
                    dino.costume = 0
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, costume2):
                    # select_sound.play()
                    selected_icon = (215, 71, 13, 13)
                    dino.costume = 1
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, costume3):
                    # select_sound.play()
                    selected_icon = (329, 71, 13, 13)
                    dino.costume = 2
                    dino.reset()
                    pygame.display.set_icon(dino.rightSprite)
                elif check_collision_list(mouse_pos, winButton):
                    if GameWon or balance >= 1000:
                        # select_sound.play()
                        GameWon = True
                        pygame.time.delay(10)
                        screen.blit(winScreen, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(50)
                        if not GameWon:
                            balance -= 1000
                    else:
                        full_sound.play()

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

            clock.tick(10)
            pygame.display.update()


if __name__ == "__main__":
    main()
