from type_shed import LEDMatrix, check_led_matrix_size

type TransitionFrames = list[LEDMatrix]


class Transition:
    """Class to gen transition frames between LED matrix states.

    Raises:
        ValueError: If the attribute ending_state LED matrix is not 8x8 pixels.
    """

    def __init__(self, ending_state: LEDMatrix):
        self.ending_state_led_matrix: LEDMatrix = ending_state
        if not check_led_matrix_size(self.ending_state_led_matrix):
            raise ValueError("LED matrix must be 8x8 pixels.")
        self.saved_led_matric_state: LEDMatrix = []

    def slide_effect_transition(self) -> TransitionFrames:  # type: ignore
        """Generates a sliding transition effect from the current state to the ending state."""
        ending_state_led_matrix = self.ending_state_led_matrix
        print(ending_state_led_matrix)

    def slide_effect_transition_slow(self) -> TransitionFrames:  # type: ignore
        pass


if __name__ == "__main__":
    # Example usage
    ending_state = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (128, 128, 128),
        (255, 255, 255),
    ] * 8
    transition = Transition(ending_state)
    transition.slide_effect_transition()
