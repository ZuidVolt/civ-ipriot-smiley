import time

from blinkable import Blinkable
from smiley import Smiley


class Happy(Smiley, Blinkable):
    """Provides a Smiley with a happy expression."""

    def __init__(self) -> None:
        # Calls super().__init__() which now uses the default YELLOW complexion
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self) -> None:
        """Renders a mouth by blanking the pixels that form that object."""
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open: bool = True) -> None:
        """Draws the eyes (open or closed) on the standard smiley.

        :param wide_open (bool): eyes open or closed.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            # Use the smiley's own complexion color when eyes are closed
            self.pixels[pixel] = (
                self.BLANK if wide_open else self.my_complexion
            )

    def blink(self, delay: float = 0.25) -> None:
        """Blinks the smiley's eyes once.

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
