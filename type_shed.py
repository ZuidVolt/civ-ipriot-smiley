from typing import TypeGuard

type RGBTuple = tuple[int, int, int]
type LEDMatrix = list[RGBTuple]
type NullableLEDMatrix = list[RGBTuple | None]


def check_led_matrix_size(led_matrix: LEDMatrix) -> TypeGuard[LEDMatrix]:
    """Check if the LED matrix is 8x8 RGB pixels."""
    eight_by_eight_matrix = 64
    return len(led_matrix) == eight_by_eight_matrix
