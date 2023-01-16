from pico2d import*

from pythonProject import title_state, game_framework


class Grass:
    def __init__(self):
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image("run_animation.png")

    def update(self):

        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    delay(0.01)

boy = None
grass = None
running = None


def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True


def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

# open_canvas()
# enter()
# while running:
#     handle_events()
#     update()
#     draw()
#
# exit()
# close_canvas()
