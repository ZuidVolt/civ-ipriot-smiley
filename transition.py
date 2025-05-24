from type_shed import LEDMatrix, RGBTuple, check_led_matrix_size

type TransitionFrames = list[LEDMatrix]


class Transition:
    def __init__(self) -> None:
        self.current_state_led_matrix: LEDMatrix = []
        self.ending_state_led_matrix: LEDMatrix = []

    def _check_if_valid_input_matrices(self) -> None:
        """Check if the LED matrices are valid 8x8 RGB matrices.

        Raises:
            ValueError: If the attribute ending_state or current_state LED matrix is not 8x8 pixels.
        """
        if not check_led_matrix_size(self.ending_state_led_matrix):
            msg = (
                "input ending state LED matrix must be 8x8 pixels. (len == 64)"
            )
            raise ValueError(msg)
        if not check_led_matrix_size(self.current_state_led_matrix):
            msg = "input current state LED matrix must be 8x8 pixels. (len == 64)"
            raise ValueError(msg)

    def pretty_print_frames(self, frames: TransitionFrames) -> None:
        for i, frame in enumerate(frames):
            print(f"Frame {i + 1}:")
            for row in range(8):
                row_start = row * 8
                row_end = row_start + 8
                print(f"{frame[row_start:row_end]}")

    def slide_effect_transition(
        self,
        current_state: LEDMatrix,
        ending_state: LEDMatrix,
    ) -> TransitionFrames:
        """Generates a sliding transition effect from the current state to the ending state.

        Returns:
              TransitionFrames: A list of LEDMatrix frames with the length of 8.

        Raises:
           ValueError: If the attribute ending_state or current_state LED matrix is not 8x8 pixels.
        """
        self.current_state_led_matrix = current_state
        self.ending_state_led_matrix = ending_state
        self._check_if_valid_input_matrices()
        frames: TransitionFrames = []
        new_matrix_frame: LEDMatrix = self.current_state_led_matrix.copy()
        for column in range(8):
            ending_state_column = self.ending_state_led_matrix[column::8]
            for row in range(8):
                new_matrix_frame[row * 8 + column] = ending_state_column[row]
            frames.append(new_matrix_frame.copy())
        assert len(frames) == 8, "There should be 8 frames in the transition."
        return frames

    def slide_effect_transition_slow(
        self,
        current_state: LEDMatrix,
        ending_state: LEDMatrix,
    ) -> TransitionFrames:
        """Generates a sliding transition effect from the current state to the ending state.

        Returns:
                TransitionFrames: A list of LEDMatrix frames with the length of 64.

        Raises:
           ValueError: If the attribute ending_state or current_state LED matrix is not 8x8 pixels.
        """
        self.current_state_led_matrix = current_state
        self.ending_state_led_matrix = ending_state
        self._check_if_valid_input_matrices()
        frames: TransitionFrames = []
        new_matrix_frame: LEDMatrix = self.current_state_led_matrix.copy()
        for column in range(8):
            ending_state_column = self.ending_state_led_matrix[column::8]
            for row in range(8):
                new_matrix_frame[row * 8 + column] = ending_state_column[row]
                frames.append(new_matrix_frame.copy())
        assert len(frames) == 64, (
            "There should be 64 frames in the transition."
        )
        return frames


if __name__ == "__main__":
    white: RGBTuple = (255, 255, 255)
    black: RGBTuple = (0, 0, 0)
    current_state: LEDMatrix = [black] * 64
    ending_state: LEDMatrix = [white] * 64
    transition = Transition()
    slide = transition.slide_effect_transition(current_state, ending_state)
    transition.pretty_print_frames(slide)
    slide_slow = transition.slide_effect_transition_slow(
        current_state, ending_state
    )
    transition.pretty_print_frames(slide_slow)
