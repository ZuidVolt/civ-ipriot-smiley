from type_shed import LEDMatrix, check_led_matrix_size

type TransitionFrames = list[LEDMatrix]


class Transition:
    def __init__(self):
        self.current_state_led_matrix: LEDMatrix = []
        self.ending_state_led_matrix: LEDMatrix = []
        self.saved_led_matric_state: LEDMatrix = []

    def _check_if_valid_input_matrices(self) -> None:
        """Check if the LED matrices are valid 8x8 RGB matrices.

        Raises:
            ValueError: If the attribute ending_state or current_state LED matrix is not 8x8 pixels.
        """
        if not check_led_matrix_size(self.ending_state_led_matrix):
            raise ValueError(
                "input ending state LED matrix must be 8x8 pixels."
            )
        if not check_led_matrix_size(self.current_state_led_matrix):
            raise ValueError(
                "input current state LED matrix must be 8x8 pixels."
            )

    def slide_effect_transition(
        self, current_sate: LEDMatrix, ending_state: LEDMatrix
    ) -> TransitionFrames:  # type: ignore
        """Generates a sliding transition effect from the current state to the ending state.

        Raises:
           ValueError: If the attribute ending_state or current_state LED matrix is not 8x8 pixels.
        """
        self.current_state_led_matrix = current_sate
        self.ending_state_led_matrix = ending_state
        self._check_if_valid_input_matrices()
        print(self.ending_state_led_matrix)

    def slide_effect_transition_slow(
        self, current_sate: LEDMatrix, ending_state: LEDMatrix
    ) -> TransitionFrames:  # type: ignore
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
    current_sate = ending_state
    transition = Transition()
    transition.slide_effect_transition(current_sate, ending_state)
