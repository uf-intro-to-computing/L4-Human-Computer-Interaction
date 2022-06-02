import time
import random
from random import randint
import displayio
from adafruit_display_shapes import circle
from unigui import UniGui, TextWidget
from unigui.pygamedisplay import PygameDisplay
from unigui.colorscheme import Solarized, VSCode

RANDOM_SEED = 1
random.seed(RANDOM_SEED)

WIDTH  = 500
HEIGHT = 500
SF     = 2
CS     = Solarized.dark
gui = UniGui(WIDTH, HEIGHT, scale=SF, colorscheme=CS)
display = PygameDisplay(WIDTH*SF, HEIGHT*SF)

BUTTON_WIDTH  = 50
BUTTON_HEIGHT = 50
(x, y) = (0, 0)
button = TextWidget("button", x, y, BUTTON_WIDTH, BUTTON_HEIGHT, colorscheme=CS)
button.set_value("click\nme")
button.border_on()
gui.add_widget(button)

display.show(gui)

start_time = time.time()
end_time = 0
n = 0
# Get the next random location for the box as a tuple
def button_clicked(_click):
    # TODO: increment n, exiting if needed and printing elapsed time;
    #       get a new random coordinate;
    #       and set the location of the button
    
button.set_click_action(button_clicked)

while True:
    display.refresh()
    click = display.get_mouse_clicks()
    if click is not None:
        gui.process_click(click)
    time.sleep(0.1)