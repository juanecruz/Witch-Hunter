import pygame,sys,win
from settings import * #settings hace parte del simon dice 
from sprites import *
import random


class Game: #acá se dara los contructores
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.beeps = [Audio(BEEP1), Audio(BEEP2), Audio(BEEP3), Audio(BEEP4)]
        self.flash_colours = [YELLOW, BLUE, RED, GREEN]
        self.colours = [DARKYELLOW, DARKBLUE, DARKRED, DARKGREEN]
        self.win = False
        self.lose = False

        self.buttons = [
            Button(110, 50, DARKYELLOW),
            Button(330, 50, DARKBLUE),
            Button(110, 270, DARKRED),
            Button(330, 270, DARKGREEN),
        ]

    def get_high_score(self): # donde se marca el puntaje maximo
        with open("high_score.txt", "r") as file:
            score = file.read()
        return int(score)

    def save_score(self): #guardar el puntaje
        with open("high_score.txt", "w") as file:
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

    def new(self): #cada vezque se inicia o se reinicie la partida esta funcion sirve para esto
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
        self.high_score = self.get_high_score()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.clicked_button = None
            self.events()
            self.draw()
            self.update()
            if self.score >= 8:
                win.main()


    def update(self):
        if not self.waiting_input:
            pygame.time.wait(1000)
            self.pattern.append(random.choice(self.colours))
            for button in self.pattern:
                self.button_animation(button)
                pygame.time.wait(200)
            self.waiting_input = True


        else:
            # pushed the correct button
            if self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                self.button_animation(self.clicked_button)
                self.current_step += 1

                # pushed the last button
                if self.current_step == len(self.pattern):
                    self.score += 1
                    self.waiting_input = False
                    self.current_step = 0

            # pushed the wrong button
            elif self.clicked_button and self.clicked_button != self.pattern[self.current_step]:
                self.game_over_animation()
                self.save_score()
                self.playing = False

    def button_animation(self, colour): 
        for i in range(len(self.colours)):
            if self.colours[i] == colour:
                sound = self.beeps[i]
                flash_colour = self.flash_colours[i]
                button = self.buttons[i]

        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = flash_colour
        sound.play()
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, ANIMATION_SPEED * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (button.x, button.y))
                pygame.display.update()
                self.clock.tick(FPS)
        self.screen.blit(original_surface, (0, 0))

    def game_over_animation(self): #cada vez que pierda utiliza en 
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((self.screen.get_size()))
        flash_surface = flash_surface.convert_alpha()
        for beep in self.beeps:
            beep.play()
        r, g, b = WHITE
        for _ in range(3):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, ANIMATION_SPEED * step):
                    self.screen.blit(original_surface, (0, 0))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(FPS)
        sys.exit()

    def draw(self): # se forma los cuadrados
        self.screen.fill(BGCOLOUR)
        UIElement(300, 20, f"Score: {str(self.score)}").draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()

    def events(self): # acá es para salir del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.clicked(mouse_x, mouse_y):
                        self.clicked_button = button.colour


game = Game()

while not game.lose:
    game.new()
    game.run()

