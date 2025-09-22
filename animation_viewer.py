from pico2d import *

open_canvas()
img = load_image('skeleton.png')
# 해당 이미지는 612*576크기

def draw_frame(frame = 0, line = 0):
    for x in range(0, 45, 1):
        clear_canvas()
        img.clip_draw(frame * 50, 576 - line * 91, 50, 100, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 9
        delay(0.1)

def character_walk():

    print("walk")



def character_attack_1():
    print("attack1")
    pass


def character_attack_2():
    print("attack2")
    pass


def character_die():
    print("die")
    pass


while(1):
    draw_frame(0,2)
    # character_walk()
    # delay(1)
    # character_attack_1()
    # delay(1)
    # character_attack_2()
    # delay(1)
    # character_die()
    # delay(1)