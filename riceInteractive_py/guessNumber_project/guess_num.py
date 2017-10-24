try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# Initial Game Stats, assume 100 range game
message = "Welcome!"
secret_number = random.randrange(1, 101)
check = 100
guess_counter = 7
counter_display = 'Guesses left: ' + str(guess_counter)

# Handler for buttons & extra fcn for game reset
def range_1000():
    global secret_number, check, guess_counter
    guess_counter = 10
    check = 1000
    secret_number = random.randrange(1, 1001)
def range_100():
    global secret_number, check, guess_counter
    guess_counter = 7
    check = 100
    secret_number = random.randrange(1, 101)
def reset():
    global secret_number, guess_counter
    if check == 1000:
        secret_number = random.randrange(1, 1001)
        guess_counter = 10
    elif check == 100:
        secret_number = random.randrange(1, 101)
        guess_counter = 7
def guess_minus():
    global guess_counter, counter_display, message
    guess_counter -= 1
    counter_display = 'Guesses left: ' + str(guess_counter)
    if guess_counter == 0:
        message = "Out of Guesses, Game Reset"
        reset()

#input that tells you too high or too low.
def input_handler(guess):
    try:
        global message
        guess = int(guess)
        if guess > secret_number:
            message = 'Guess was ' + str(guess) + ', Too High!'
            guess_minus()
        elif guess < secret_number:
            message = 'Guess was ' + str(guess) + ', Too Low!'
            guess_minus()
        elif guess == secret_number:
            message = 'Guess was ' + str(guess) + ', CORRECT! New Game Started'
            reset()

    except:
        message = 'This is not a number. Please input again.'

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [150,112], 30, "White")
    canvas.draw_text(counter_display, [20,190], 30, "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 200)
frame.add_input('Number Here', input_handler, 120)
frame.add_button("Range up to 1000", range_1000,120)
frame.add_button("Range up to 100", range_100, 120)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
