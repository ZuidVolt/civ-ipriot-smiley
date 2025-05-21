# ruff: noqa: N806 E741

from sense_hat import SenseHat
from type_shed import LEDMatrix


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        # fmt: off
        Y = self.YELLOW
        O = self.BLANK
        self.pixels: LEDMatrix = [
            O, Y, Y, Y, Y, Y, Y, O,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            O, Y, Y, Y, Y, Y, Y, O,
        ]
        # fmt: on

    def dim_display(self, dimmed: bool = True):
        """Set the SenseHat's light intensity to low (True) or high (False).

        :param dimmed: Dim the display if True, otherwise don't dim.
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """Show the smiley on the screen."""
        self.sense_hat.set_pixels(self.pixels)
