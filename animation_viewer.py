from pico2d import *

open_canvas()
img = load_image('sprite_sheet_example.png')


frame_width = 50  # 프레임 가로 크기
frame_height = 37  # 프레임 세로 크기
top_img = 407 # 이미지의 최대 y좌표

def draw_frame(frame = 0, line = 0):
    for x in range(0, 35, 1):
        clear_canvas()
        img.clip_draw(frame * frame_width, top_img - line * frame_height, frame_width, frame_height, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.1)


def character_run():
    draw_frame(0,2)


def character_slide():
    draw_frame(0,4)


def character_jump():
    draw_frame(0,5)


def character_attack():
    draw_frame(0,8)


while(1):
    character_run()

    delay(1)
    character_slide()
    delay(1)
    character_jump()
    delay(1)
    character_attack()
    delay(1)