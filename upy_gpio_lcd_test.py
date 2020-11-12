"""Implements a HD44780 character LCD connected via generic uPy GPIO pins.

   This has been tested only on STM32 Nucleo-64 boards using the DFR0009 LCD keypad shield.
   Note that the HAL for STM32 Nucleo devices supports both Arduino and Morpho pin names.

   Originally created by Dave Hylands: https://github.com/dhylands/python_lcd
   Modified by Y. Curtis Wang, Cal State LA for generic MicroPython
"""

from machine import Pin
from utime import sleep_ms, ticks_ms
from upy_gpio_lcd import GpioLcd

# Wiring used for this example, assuming the DFR009:
#  URL: https://wiki.dfrobot.com/LCD_KeyPad_Shield_For_Arduino_SKU__DFR0009
#
#  1 - Vss (aka Ground) - Connect to one of the ground pins on you pyboard.
#  2 - VDD - I connected to VIN which is 5 volts when your pyboard is powered via USB
#  3 - VE (Contrast voltage) - I'll discuss this below
#  4 - RS (Register Select) connect to D8 (as per call to GpioLcd)
#  5 - RW (Read/Write) - connect to ground
#  6 - EN (Enable) connect to D9 (as per call to GpioLcd)
#  7 - D0 - leave unconnected
#  8 - D1 - leave unconnected
#  9 - D2 - leave unconnected
# 10 - D3 - leave unconnected
# 11 - D4 - connect to D4 (as per call to GpioLcd)
# 12 - D5 - connect to D5 (as per call to GpioLcd)
# 13 - D6 - connect to D6 (as per call to GpioLcd)
# 14 - D7 - connect to D7 (as per call to GpioLcd)
# 15 - A (BackLight Anode) - Connect to VIN
# 16 - K (Backlight Cathode) - Connect to Ground
#
# On 14-pin LCDs, there is no backlight, so pins 15 & 16 don't exist.
#
# The Contrast line (pin 3) typically connects to the center tap of a
# 10K potentiometer, and the other 2 legs of the 10K potentiometer are
# connected to pins 1 and 2 (Ground and VDD)


def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    lcd = GpioLcd(rs_pin=Pin("D8"),
                  enable_pin=Pin("D9"),
                  d4_pin=Pin("D4"),
                  d5_pin=Pin("D5"),
                  d6_pin=Pin("D6"),
                  d7_pin=Pin("D7"))
    rotate_strs = ["Welcome to CSULA",
                   "Go Golden Eagles",
                   "Electrical",
                   "Engineering",
                   "is hype!",
                   "Join Us!!"]
    lcd.blink_cursor_on()
    while True:
        lcd.clear()
        for i, str_disp in enumerate(rotate_strs):
            for a_char in str_disp:
                lcd.putchar(a_char)
                sleep_ms(100)
            sleep_ms(750)
            if i % 2 == 1 and i > 0:
                sleep_ms(750)
                lcd.clear()
            elif len(str_disp) != 16:
                lcd.putchar("\n")
        sleep_ms(3000)
