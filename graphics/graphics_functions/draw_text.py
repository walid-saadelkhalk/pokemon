import pygame
from graphics.graphics_attributes import *

clock = pygame.time.Clock()

def draw_text(screen, text_content, font_long, rectangle, y_begin, y_delta, max_lines):
    global num_words
    words = text_content.split(' ')
    space_width, _ = font_long.size(' ')

    lines = []
    current_line = []
    current_line_width = 0
    for word in words[:num_words]:
        word_width, word_height = font_long.size(word)

        if current_line_width + word_width <= rectangle.width:
            current_line.append(word)
            current_line_width += word_width + space_width
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_line_width = word_width + space_width

    lines.append(' '.join(current_line))

    y = y_begin
    for line in lines[-max_lines:]:
        text = font_long.render(line, True, 'black')
        text_rect = text.get_rect(center=(rectangle.centerx, y))
        text.set_clip(text_rect)
        screen.blit(text, text_rect)
        y += y_delta

    clock.tick(2)
    num_words += 1

# def erase_text(screen, rectangle, y_begin, y_delta, max_lines):
#     erase_surface = pygame.Surface((rectangle.width, max_lines * y_delta))
#     erase_surface.fill((255, 255, 255)) 

#     text_rect = erase_surface.get_rect(center=(rectangle.centerx, y_begin))
#     screen.blit(erase_surface, text_rect)
