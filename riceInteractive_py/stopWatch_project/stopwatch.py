# http://www.codeskulptor.org/docs.html
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

template = "Lets Begin!"
message = template
second_count = 0

#format time function
def format(time):
    #we get an integer that needs logic to become A:BC.D
    #Idea: divide by 600 if === int: save counter of this for mins
    #Make counter that moves with secs and retarts after 60 secs and use that for secs
    #splice last number in time for the dotsec
    #
    sec_time = 0
    time = str(time)
    dotsec = time[-1]
    sec = time[-3:-1]
    mins = time[0: -3]

    return mins + ":" + sec + "." + dotsec

# Handler for mouse click
def click_on():
    timer.start()
def click_off():
    timer.stop()

#Handler for the timer
def display_time():
    global message
    global second_count
    second_count += 1
    message = format(second_count)

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [200,200], 48, "Red")


# Create a frame and assign callbacks to event handlers
try:
    frame = simplegui.create_frame("Home", 600, 400)
    timer = simplegui.create_timer(100 , display_time)
    frame.add_button("Timer On", click_on)
    frame.add_button("Timer Off", click_off)
    frame.set_draw_handler(draw)
    # Start the frame animation
    frame.start()
except:
    print('error somewhere in the frame')
