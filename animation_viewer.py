from pico2d import *

open_canvas()
img = load_image('sprite_sheet_example.png')


frame_width = 50  # 프레임 가로 크기
frame_height = 37  # 프레임 세로 크기
top_img = 407 # 이미지의 최대 y좌표


def character_run():
    line = 2
    frame = 0
    for x in range(0, 35, 1):
        clear_canvas()
        img.clip_draw(frame * frame_width, top_img - line * frame_height, frame_width, frame_height, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.05)


def character_slide():
    print("Character Slide")
    line = 4
    frame = 0
    for x in range(0, 35, 1):
        clear_canvas()
        img.clip_draw(frame * frame_width, top_img - line * frame_height, frame_width, frame_height, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.05)
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
    character_slide()
    delay(1)
    # character_jump()
    # delay(1)
    # character_attack()
    # delay(1)