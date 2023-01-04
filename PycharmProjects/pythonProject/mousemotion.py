from pico2d import *
import random

Background_WIDTH, Background_HEIGHT = 730, 400
def handle_events():
    global running
    global x, y
    global cursor_positionY
    global cursor_positionX
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     cursor_positionX = event.x, cursor_positionY = event.x, Background_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif x == cursor_positionX and y == cursor_positionY:
            running =False

open_canvas(Background_WIDTH, Background_HEIGHT)
tuk_ground = load_image("background.png")
character = load_image("run_animation.png")
cursorimage = load_image("Bringer-of-Death_Walk_1.png")

running = True
x, y = Background_WIDTH // 2, Background_HEIGHT // 2
frame = 0
hide_cursor()
cursor_positionX, cursor_positionY = random.randint(1, 730), random.randint(1, 400)

while running:
    clear_canvas()

    tuk_ground.draw(Background_WIDTH // 2, Background_HEIGHT //2)
    cursorimage.draw(cursor_positionX, cursor_positionY)
    character.clip_draw(frame*100, 0, 100, 100, cursor_positionX, cursor_positionY)
    update_canvas()
    frame = (frame+1) % 10
    handle_events()

    delay(0.05)
close_canvas()