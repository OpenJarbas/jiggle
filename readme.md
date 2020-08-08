# Jiggle

simple python mouse jiggler

A Mouse Jiggler prevents your computer from going to sleep while you work or play. 

Jiggle alloes you to create constant mouse activity so your computer won't go idle and trigger screen savers or sleep mode—eliminating the need to log in repeatedly.
 

## Usage

```python
from jiggle import MouseJiggler

j = MouseJiggler()
j.run()
```

Event / Thread based

```python
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

sleep(30)

j.stop()
```