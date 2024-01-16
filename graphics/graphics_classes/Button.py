import pygame
from assets import *
from graphics.graphics_attributes import font_button_menu, font_ingame

class Button():
    def __init__(self, x, y, text, font, scale, color, hover_color):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.clicked = False

        self.create_button(x, y, scale)

    def create_button(self, x, y, scale):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def check_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                print (self.text + " Clicked")
                action = True
            else:
                self.image = self.font.render(self.text, True, self.hover_color)
        else:
            self.clicked = False
            self.image = self.font.render(self.text, True, self.color)
        return action
    
    def render(self, screen):
        self.draw(screen)
        return self.check_clicked()




#create button instances
new_game_button = Button(200, 250, "NEW-GAME", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
continue_button = Button(200, 350, "CONTINUE", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
option_button = Button(200, 450, "OPTION", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
attack_button = Button(150, 450, "FIGHT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
object_button = Button(450, 450, "OBJECT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
flee_button = Button(150, 510, "RUN", font_ingame, 1, (0, 0, 0), (50, 50, 50))
change_poke_button = Button(450, 510, "CHANGE POKEMON", font_ingame, 1, (0, 0, 0), (50, 50, 50))
# quit_button = Button.Button(200, 100, "Cliquez-moi", None, 2, (255, 0, 0), (0, 255, 0))