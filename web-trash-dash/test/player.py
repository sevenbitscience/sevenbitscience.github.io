import pygame


class Player:
    position = [100, 400]
    velocity = [0, 0]
    speed = 2
    # drag = 0.1
    frame = 0
    costume = 0
    walk = [pygame.image.load("assets/gfx/walking/DinoR1.png"), pygame.image.load("assets/gfx/walking/DinoR2.png"),
            pygame.image.load("assets/gfx/walking/DinoR3.png"), pygame.image.load("assets/gfx/walking/DinoR4.png"),
            pygame.image.load("assets/gfx/walking/DinoR5.png"), pygame.image.load("assets/gfx/walking/DinoR6.png")]
    idle = pygame.image.load("assets/gfx/dino.png")
    duck_walk = [pygame.image.load("assets/gfx/DuckDino/DuckR1.png"), pygame.image.load(
        "assets/gfx/DuckDino/DuckR2.png"),
                 pygame.image.load("assets/gfx/DuckDino/DuckR3.png"), pygame.image.load(
            "assets/gfx/DuckDino/DuckR4.png"),
                 pygame.image.load("assets/gfx/DuckDino/DuckR5.png"), pygame.image.load(
            "assets/gfx/DuckDino/DuckR6.png")]
    duck_idle = pygame.image.load("assets/gfx/DuckDino/DuckIdle.png")
    robo_walk = [pygame.image.load("assets/gfx/RoboDino/ROBOR1.png"), pygame.image.load(
        "assets/gfx/RoboDino/ROBOR2.png"),
                 pygame.image.load("assets/gfx/RoboDino/ROBOR3.png"), pygame.image.load(
            "assets/gfx/RoboDino/ROBOR4.png"),
                 pygame.image.load("assets/gfx/RoboDino/ROBOR5.png"), pygame.image.load(
            "assets/gfx/RoboDino/ROBOR6.png")]
    robo_idle = pygame.image.load("assets/gfx/RoboDino/dinoBotIdle.png")
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