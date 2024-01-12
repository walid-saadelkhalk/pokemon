from graphics.graphics_attributes import *
from graphics.graphics_classes.Button_rect import *
from graphics.graphics_classes.Button_image import *
from graphics.graphics_functions.draw_text import *

def render_pokemon_choices():
    rectangle = pygame.draw.rect(screen, 'white', (50, 20, 700, 160), 0, 15)
    draw_text(screen, text_choix, font_ingame, rectangle, 50, 50, max_lines=6)
    carapuce = Image('./assets/images/carapuce_2.png', (-30, 250))
    carapuce.draw_image(screen)
    salameche = Image('./assets/images/salameche_2.png', (250, 250))
    salameche.draw_image(screen)
    carapuce = Image('./assets/images/bulbizarre_2.png', (530, 250))
    carapuce.draw_image(screen)
    water = Message(20, 300, 200, 50, 'Type Eau', 'black', 'white')
    water.message_render(font_long, screen)
    fire = Message(300, 300, 200, 50, 'Type Feu', 'black', 'white')
    fire.message_render(font_long, screen)
    grass = Message(580, 300, 200, 50, 'Type Plante', 'black', 'white')
    grass.message_render(font_long, screen)
    