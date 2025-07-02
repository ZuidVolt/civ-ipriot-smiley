import time

from blinkable import Blinkable
from smiley import Smiley



class Angry(Smiley, Blinkable):
    """Provides a Smiley with an angry expression."""

    def __init__(self) -> None:
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
  