# ruff: noqa: N806 E741

from sense_hat import SenseHat
from type_shed import LEDMatrix, RGBTuple


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, complexion: RGBTuple = YELLOW) -> None:
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.my_complexion: RGBTuple = complexion
        # fmt: off
        O = self.BLANK
        X = self.my_complexion
        self.pixels: LEDMatrix = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]
        # fmt: on

    def dim_display(self, dimmed: bool = True) -> None:
        """Set the SenseHat's light intensity to low (True) or high (False).

        :param dimmed: Dim the display if True, otherwise don't dim.
        """
        self.sense_hat.low_light = dimmed

    def show(self) -> None:
        """Show the smiley on the screen."""
        self.sense_hat.set_pixels(self.pixels)

    def complexion(self) -> RGBTuple:
        return self.my_complexion
