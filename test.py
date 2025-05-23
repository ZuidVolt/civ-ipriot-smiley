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
