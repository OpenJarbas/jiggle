from jiggle import MouseJiggler
from time import sleep

j = MouseJiggler(ignore_idle=True, jiggle=2, daemonic=True)


def on_mouse_move(mouse_position):
    print(mouse_position)


def on_jiggle():
    print("jiggle")


def on_idle():
    print("idle")


def on_active():
    print("active")


def on_stop():
    print("Stopped")


j.on_mouse_move = on_mouse_move
j.on_jiggle = on_jiggle
j.on_idle = on_idle
j.on_active = on_active
j.on_stop = on_stop

j.start()

sleep(10)

j.stop()

sleep(1)
