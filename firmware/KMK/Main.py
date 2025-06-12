print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()


keyboard.row_pins = (board.GP3, board.GP4, board.GP2)
keyboard.col_pins = (board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()

keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(TapDance())

encoder_handler.pins = ((board.GP0, board.GP1, None),)

#RGB
rgb = RGB(pixel_pin=board.GP26, 
          num_pixels=9, 
          rgb_order=(1,0,2),
          
          )

keyboard.extensions.append(rgb)

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(i2c=i2c_bus)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=1, # initial screen brightness level
)


display.entries = [
    ImageEntry(image="me.bmp", x=0, y=0, layer=0),
    ImageEntry(image="kevin.bmp", x=0, y=0, layer=1), 
    ImageEntry(image="oneil.bmp", x=0, y=0, layer=2), 
    ImageEntry(image="hc.bmp", x=0, y=0, layer=3), 
    TextEntry(text="Layer 0", x_anchor="T", y_anchor="R", layer=0),
    TextEntry(text="Layer 1", x_anchor="T", y_anchor="R", inverted=True, layer=1),
    TextEntry(text="Layer 2", x_anchor="T", y_anchor="R", inverted=True, layer=2),
    TextEntry(text="Layer 3", x_anchor="T", y_anchor="R", inverted=True, layer=3),
]
keyboard.extensions.append(display)

TRANS = KC.TRNS
RAISE =   KC.LT(1, KC.TD(KC.B, KC.A), prefer_hold=True, tap_interrupted=False, tap_time=1000)
MIDDLE =  KC.LT(2, KC.TD(KC.B, KC.A), prefer_hold=True, tap_interrupted=False, tap_time=1000)
MIDDLER = KC.LT(3, KC.TD(KC.B, KC.A), prefer_hold=True, tap_interrupted=False, tap_time=1000)
BASE =    KC.LT(0, KC.TD(KC.B, KC.A), prefer_hold=True, tap_interrupted=False, tap_time=1000)
keyboard.keymap = [
 
    [ #LAYER 0: NUMPAD
     KC.N7, KC.N8, KC.N9, RAISE,
     
     KC.N4, KC.N5, KC.N6,

     KC.N1, KC.N2, KC.N3
    ],
    
    [ #LAYER 1: Media Keys
     KC.NO, KC.BRIU, KC.NO, MIDDLE,

     KC.MPRV, KC.MPLY, KC.MNXT,

     KC.NO, KC.BRID, KC.NO
    ],

    [ #LAYER 2: DAILY [TBD, will think of it when i have it in-person!]
     KC.N7, KC.N8, KC.N9, MIDDLER ,

     KC.N4, KC.N5, KC.N6,

     KC.N1, KC.N2, KC.N3
    ],
    
    [ #LAYER 3: LEDs animation 
     KC.RGB_MODE_KNIGHT, KC.RGB_MODE_SWIRL, KC.RGB_MODE_BREATHE, BASE,
     
     KC.RGB_HUD, KC.RGB_ANI, KC.RGB_HUI,
     
     KC.N1, KC.RGB_AND, KC.RGB_TOG
    ],
]


encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), # any layer
]

if __name__ == '__main__':
    keyboard.go()