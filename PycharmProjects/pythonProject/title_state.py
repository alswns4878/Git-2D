import game_framework
from pico2d import *
import play_state

image = None
def enter():
    global image
    image = load_image("title.png")

def exit():
    global image
    del image


def update():
    pass


def handle_events():
    events = get_events()
    for event in events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
