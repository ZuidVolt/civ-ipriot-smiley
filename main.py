"""Demonstrates the use of the Smiley class and its subclasses.

If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle.
"""

import time

from angry import Angry
from happy import Happy
from sad import Sad


def main() -> None:
    print("Showing Happy Smiley (default yellow)...")
    smiley = Happy()
    smiley.show()
    time.sleep(1)
    smiley.blink()
    time.sleep(1)

    print("Showing Sad Smiley (blue)...")
    sad = Sad()
    sad.show()
    time.sleep(1)
    sad.blink()
    time.sleep(1)

    print("Showing Angry Smiley (red)...")
    angry = Angry()
    angry.show()
    time.sleep(1)
    angry.blink()
    time.sleep(1)
    # extra functionality to change complexion with a transitions
    angry.turn_sick()
    time.sleep(1)
    angry.turn_angry()
    time.sleep(1)


if __name__ == "__main__":
    # from multiprocessing import freeze_support
    # freeze_support()
    main()
