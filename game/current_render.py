from graphics.graphics_functions import render_main
# from graphics.graphics_functions import render_combat
from graphics.graphics_classes.Button import *
from graphics.graphics_attributes import *

state = render_main.render_main_menu

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state