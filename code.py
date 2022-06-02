import time
import board
import busio
import adafruit_trellism4
import adafruit_adxl34x
import usb_hid
from adafruit_hid.mouse import Mouse

# neotrellis NeoPixel Button UI
trellis = adafruit_trellism4.TrellisM4Express()
trellis.pixels.brightness = 0.33
LEFT_BUTTON  = (0, 0)
RIGHT_BUTTON = (7, 0)
trellis.pixels[LEFT_BUTTON] = 0xFF00FF
trellis.pixels[RIGHT_BUTTON] = 0xFF00FF

# Accelerometer configuration:
# TODO
# i2c = 
# accelerometer = 

# USB HID configuration
# TODO
# mouse = 

# Convert the x and y acceleration values into left/right up/down mouse velocity values
# The mouse moves at a rate of ??
def get_mouse_deltas(x_acc, y_acc):
    # TODO
    return (round(dx), round(dy))

# Main loop TODO
# Track button states, read accelerometer, and send the proper values over USB
left_button_state = False
right_button_state = False
while True:
    (_x, _y, _z) = accelerometer.acceleration
    x_acc = round(_x) / 2
    y_acc = round(_y) / 2
    z_acc = round(_z) / 2
    # print("x: %d" % x_acc)
    # print("y: %d" % y_acc)

    (dx, dy) = get_mouse_deltas(x_acc, y_acc)
    mouse.move(x=dx)
    mouse.move(y=dy)

    # Button logic
    pressed = set(trellis.pressed_keys)
    # TODO write logic to read and debounce a button press
    