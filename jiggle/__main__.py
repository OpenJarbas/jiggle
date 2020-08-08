from jiggle import MouseJiggler

j = MouseJiggler()
try:
    j.start()
except KeyboardInterrupt:
    j.stop()