import time

from blinkable import Blinkable
from smiley import Smiley
from transition import Transition


class Angry(Smiley, Blinkable):
    """Provides a Smiley with an angry expression."""

    def __init__(self) -> None:
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.transition = Transition()

    def draw_mouth(self) -> None:
        """Renders an angry mouth (straight line) by blanking the pixels."""
        mouth = [42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open: bool = True) -> None:
        """Draws angry eyes (open or closed) on the standard smiley."""
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = (
                self.BLANK if wide_open else self.my_complexion
            )

    def blink(self, delay: float = 0.25) -> None:
        """Blinks the angry smiley's eyes once."""
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()

    def turn_sick(self) -> None:
        """Transitions the complexion to green using the Transition object."""
        sick_complexion = self.GREEN
        # Prepare current and ending LED matrices
        current_state = self.pixels.copy()
        ending_state = [
            sick_complexion if px != self.BLANK else self.BLANK
            for px in self.pixels
        ]
        frames = self.transition.slide_effect_transition(
            current_state,
            ending_state,  # type: ignore # LEDMatrix is a list of RGBTuple
        )
        for frame in frames:
            self.pixels = frame.copy()
            self.show()

    def turn_angry(self) -> None:
        """Transitions the complexion to red using the Transition object."""
        angry_complexion = self.RED
        current_state = self.pixels.copy()
        ending_state = [
            angry_complexion if px != self.BLANK else self.BLANK
            for px in self.pixels
        ]
        frames = self.transition.slide_effect_transition_slow(
            current_state,
            ending_state,  # type: ignore # LEDMatrix is a list of RGBTuple
        )
        for frame in frames:
            self.pixels = frame.copy()
            self.show()
