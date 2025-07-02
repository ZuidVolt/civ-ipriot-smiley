import time

from blinkable import Blinkable
from smiley import Smiley


class Sad(Smiley, Blinkable):
    def __init__(self) -> None:
        super().__init__(complexion=self.BLUE)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self) -> None:
        """Draws the mouth feature on a smiley."""
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open: bool = True) -> None:
        """Draws open or closed eyes on a smiley.

        :param wide_open: Render eyes wide open or shut.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = (
                self.BLANK if wide_open else self.my_complexion
            )

    def blink(self, delay: float = 0.25) -> None:
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
