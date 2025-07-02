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
    angry = Angry()  # Create an instance of Angry smiley
    angry.show()  # Show the angry smiley
    time.sleep(1)
    angry.blink()  # Blink the angry smiley
    time.sleep(1)
    angry.turn_sick()  # Transition to sick complexion
    time.sleep(1)
    angry.turn_angry()  # Transition back to angry complexion
    time.sleep(1)


if __name__ == "__main__":
    # from multiprocessing import freeze_support
    # freeze_support()
    main()
