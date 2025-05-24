from smiley import Smiley


class Sad(Smiley):
    def __init__(self) -> None:
        super().__init__()

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
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.YELLOW
            self.pixels[pixel] = eyes
