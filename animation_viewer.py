from pico2d import *

open_canvas()
img = load_image('skeleton.png')
# 해당 이미지는 612*576크기


def draw_frame(frame = 0, line = 0, frame_width = 0, frame_height = 0, hight = 80, x = 450, y = 300):
    clear_canvas()
    img.clip_draw(frame, 576 - line * frame_height, frame_width, hight, x, y, 300, 300)
    update_canvas()
    frame = (frame + 1) % 9
    delay(0.1)

def character_walk():
    print("walk")
    for x in range(0, 5):
        draw_frame(0, 2, 68, 80)
        draw_frame(68, 2, 68, 80)
        draw_frame(68*2+5, 2,  68, 80)
        draw_frame(68*3+10, 2,  68, 80)
        draw_frame(68*4+15, 2,  68, 80)
        draw_frame(68*5+15, 2,  68, 80)
        draw_frame(68*6+20, 2,  68, 80)
        draw_frame(68*7+15, 2,  68, 80)




def character_attack_1():
    print("attack1")
    for x in range(0, 5):
        draw_frame(0, 3,  60, 90)
        draw_frame(60, 3,  70, 90, 80, 390)
        draw_frame(130, 3,  90, 90, 110, 390, 330)
        draw_frame(220, 3,  70, 90, 110, 390, 330)
        draw_frame(290, 3,  60, 90, 80, 380)


def character_attack_2():
    print("attack2")
    pass


def character_die():
    print("die")
    pass


while(1):
    # character_walk()
    # delay(1)
    character_attack_1()
    delay(1)
    # character_attack_2()
    # delay(1)
    # character_die()
    # delay(1)