"""Demonstrates the use of the Smiley class and its subclasses.

If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle.
"""

import time

from happy import Happy
from sad import Sad


def main() -> None:
    smiley = Happy()

    smiley.show()

    time.sleep(1)

    smiley.blink()

    sad = Sad()

    sad.show()

    time.sleep(1)

    sad.blink()


if __name__ == "__main__":
    # from multiprocessing import freeze_support
    # freeze_support()
    main()
