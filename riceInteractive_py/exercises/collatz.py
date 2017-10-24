# Mystery computation in Python
# Takes input n and computes output named result

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print("Input is", n)

def get_next(current):
    if current == 1:
        timer.stop()
        print("Collatz Sequence Complete")
    elif (current % 2) == 1:
        return (current * 3) +1
    elif (current % 2) == 0:
        return current // 2

# timer callback

def update():
    global n
    n = get_next(n)
    print(n)

# register event handlers
init(2202300000)

timer = simplegui.create_timer(50, update)

# start program

timer.start()
