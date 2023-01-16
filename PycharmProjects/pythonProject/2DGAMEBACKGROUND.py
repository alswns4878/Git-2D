from pico2d import *


class Background:
    def __init__(self):
        self.image1 = load_image("background_layer_1.png")
        self.image2 = load_image("background_layer_2.png")
        self.image3 = load_image("background_layer_3.png")
        self.tile = load_image("tile1.png")
        self.lamp = load_image("lamp.png")
        self.grass1 = load_image("grass_1.png")
        self.grass2 = load_image("grass_2.png")
        self.grass3 = load_image("grass_3.png")
        self.rock2 = load_image("rock_2.png")
        self.rock3 = load_image("rock_3.png")
        self.fence = load_image("fence_1.png")
        self.shop = load_image("shop_anim.png")
        self.frame =0
    def draw(self):
        global running

        self.image1.draw(800, 450)
        self.image2.draw(800, 450)
        self.image3.draw(800, 450)

        self.shop.clip_draw(self.frame * 500, 0, 500, 500, 400, 304)
        self.frame = (self.frame + 1) % 6
        for x in range(13):
            self.tile.draw(x *136, 34)
        self.lamp.draw(100, 136)
        for x in range(2, 4):
            self.lamp.draw(x *400, 136)
        for x in range(1, 10, 2):
            self.grass2.draw(x* 160, 69)
        self.fence.draw(1000, 94)
        self.rock3.draw(1300, 97)

class Background2:
    def __init__(self):
        self.image1 = load_image("background_layer_1.png")
        self.image2 = load_image("background_layer_2.png")
        self.image3 = load_image("background_layer_3.png")

        self.tile1 = load_image("tile1.png")
        self.tile2 = load_image("tile2.png")
        self.lamp = load_image("lamp.png")
        self.rock2 = load_image("rock_2.png")
        self.rock3 = load_image("rock_3.png")
        self.soil = load_image("soil.png")
        self.sign = load_image("sign.png")
    def draw(self):
        global running

        self.image1.draw(800, 450)
        self.image2.draw(800, 450)
        self.image3.draw(800, 450)
        self.sign.draw(950, 192)
        self.rock2.draw(1020, 152)
        for x in range(7):
            self.tile1.draw(x * 136, 34)
        for x in range(3):
            self.tile2.draw((x * 270)+ 1020, 102)
        self.lamp.draw(400, 136)
        self.lamp.draw(1450, 202)
        self.rock3.draw(200, 97)
        for x in range(5):
            self.soil.draw((x *210) +990, 34)


class Player:
    def __init__(self):
        self.x, self.y = 40, 102
        self.frame = 0
        self.imageRight = load_image("Warrior_Sheet-Effect.png")
        self.imageLeft = load_image("Warrior_Sheet-Effect.Left.png")

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.imageRight.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        self.x += dir * 5
        self.y += diry * 5


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

                dir += 3
            elif event.key == SDLK_LEFT:

                dir -= 3

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 3
            elif event.key == SDLK_LEFT:
                dir += 3

            elif event.key == SDLK_ESCAPE:
                running = False


open_canvas(1600, 900)
background = Background()
background2 = Background2()
player = Player()
running = True
frame = 0
dir = 0
diry = 0

while running:
    handle_events()
    player.update()
    clear_canvas()

    background.draw()

    background2.draw()

    player.draw()
    update_canvas()

    delay(0.05)
close_canvas()
