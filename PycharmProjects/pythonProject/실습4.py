from pico2d import *
import random

Background_WIDTH, Background_HEIGHT = 730, 400
def handle_events():
    global running
    global x, y
    global cursor_x, cursor_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             running = False
        elif event.type == SDL_MOUSEMOTION:
             cursor_x, cursor_y = event.x, Background_HEIGHT -1 - event.y

             print("cursor_x=", cursor_x, "cursor_y=" ,cursor_y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             running = False

open_canvas(Background_WIDTH, Background_HEIGHT)
tuk_ground = load_image("background.png")
character_RIGHT = load_image("run_animation.png")
character_LEFT = load_image("run_animation_left.png")
running = True

x, y = Background_WIDTH // 2, Background_HEIGHT // 2
cursor_x =0
cursor_y=0
frame = 0
show_cursor()


while running:
    clear_canvas()

    tuk_ground.draw(Background_WIDTH // 2, Background_HEIGHT //2)
    if x < cursor_x:
        character_RIGHT.clip_draw(frame*100, 0, 100, 100, x, y)
    elif x > cursor_x:
        character_LEFT.clip_draw(frame*100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame+1) % 10

    if x < cursor_x:
        x += 10
    elif x > cursor_x:
        x -= 10
    if y < cursor_y:
        y += 10
    elif y > cursor_y:
        y -= 10

    handle_events()

    delay(0.05)
close_canvas()