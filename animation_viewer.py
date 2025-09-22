from pico2d import *

open_canvas()
img = load_image('skeleton.png')

def character_walk():

    print("walk")
    pass


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
    character_walk()
    delay(1)
    character_attack_1()
    delay(1)
    character_attack_2()
    delay(1)
    character_die()
    delay(1)