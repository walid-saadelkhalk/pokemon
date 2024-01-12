import pygame
from graphics.graphics_attributes import *

def mouse_button_event(event, button_object):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object.get_clicked() == True:
            set_menu(1)