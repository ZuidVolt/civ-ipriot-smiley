def create_eight_by_eight_matrix_with_index_elements() -> list[int]:
    matrix: list[int] = []
    count = 0
    for _ in range(64):
        matrix.append(count)
        count += 1
    return matrix


def display_matrix(matrix: list[int]) -> None:
    for i in range(8):
        for j in range(8):
            print(f"{matrix[i * 8 + j]:2}", end=" ")  # from stack overflow
        print()
    print()


if __name__ == "__main__":
    matrix = create_eight_by_eight_matrix_with_index_elements()
    display_matrix(matrix)

    # will produce 8 lists
    for i in range(8):
        column = matrix[i::8]
        match i + 1:
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"
        print(f"Every element in the {i + 1}{suffix} column: {column}")

    # will produce 64 lists
    for i in range(8):
        for j in range(8):
            element = matrix[i * 8 + j]
            match (i + 1, j + 1):
                case (1, 1):
                    suffix = "st"
                case (2, 2):
                    suffix = "nd"
                case (3, 3):
                    suffix = "rd"
                case _:
                    suffix = "th"
            print(
                f"The element at the {i + 1}{suffix} row and {j + 1}{suffix} column: {element}",
            )
