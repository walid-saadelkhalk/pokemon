import pygame
from graphics.graphics_attributes import *

class Image:
    def __init__(self, image, image_pos):
        self.__image = image
        self.__image_pos = image_pos
        self.__image_surface = None 

    def get_image(self):
        return self.__image

    def set_image(self, image):
        self.__image = image
        self.__image_surface = None
        
    def get_image_pos(self):
        return self.__image_pos

    def get_image_surface(self):
        if self.__image_surface is None:
            self.__image_surface = pygame.image.load(self.__image).convert_alpha()
        return self.__image_surface

    def draw_image(self, screen):
        screen.blit(self.get_image_surface(), self.__image_pos)