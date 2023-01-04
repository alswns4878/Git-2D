from pico2d import*

def handle_events():
    global running
    global dir
    global diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
            elif event.key == SDLK_ESCAPE:
                running = False
open_canvas()
grass = load_image("grass.png")
character = load_image("run_animation.png")

running = True
x = 800 // 2
y = 800 // 2
frame =0
dir = 0
diry =0
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame *100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame+1) % 10
    x += dir * 5
    y += diry *5
    delay(0.02)

close_canvas()


