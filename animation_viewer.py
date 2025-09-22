from pico2d import *

open_canvas()
img = load_image('sprite_sheet_example.png')


def character_run():
    print("Character Run")
    pass


def character_slide():
    print("Character Slide")
    pass


def character_jump():
    print("Character Jump")
    pass


def character_attak():
    print("Character Attak")
    pass


while(1):
    img.draw(400, 300)
    update_canvas()
    character_run()
    delay(1)
    character_slide()
    delay(1)
    character_jump()
    delay(1)
    character_attak()
    delay(1)