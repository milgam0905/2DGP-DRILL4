from pico2d import *

open_canvas()
img = load_image('sprite_sheet_example.png')


frame_width = 50  # 프레임 가로 크기
frame_height = 38  # 프레임 세로 크기
top_img = 407 # 이미지의 최대 y좌표


def character_run():
    print("Character Run")
    line = 2
    frame = 0
    clear_canvas()
    img.clip_draw(frame * frame_width, top_img - line * frame_height, frame_width, frame_height, 400, 300, 300, 300)
    update_canvas()
    delay(0.05)


def character_slide():
    print("Character Slide")
    pass


def character_jump():
    print("Character Jump")
    pass


def character_attack():
    print("Character Attack")
    pass


while(1):
    character_run()
    delay(1)
    # character_slide()
    # delay(1)
    # character_jump()
    # delay(1)
    # character_attack()
    # delay(1)