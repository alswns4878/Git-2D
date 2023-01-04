from pico2d import *

open_canvas(1056, 672)
grass = load_image("backgroundb1.png")
character = load_image("image1.png")
monster = load_image("Bringer-of-Death_Walk_1.png")

x = 0
frame =0

while (x < 1056):
    clear_canvas()
    grass.draw_now(538, 336)
    monster.draw_now(900, 160)
    character.clip_draw(frame * 140, 0, 140, 93, x, 160)
    update_canvas()
    frame = (frame + 1) % 8
    x += 8
    delay(0.05)

close_canvas()