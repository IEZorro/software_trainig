import simplegui

message = "Lets Begin!"
second_count = 0

#format time function
def format(time):
    D = time % 10
    if time == 0:
        return "." + D
    elif time // 10 != 0:
        time = time // 10
        BC = time % 60
        if len(str(BC)) == 1:
            BC = "0" + str(time % 60)
        A = time // 60
        return str(A) + ":" + str(BC) + "." + str(D)

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
    message = str(format(second_count))

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
