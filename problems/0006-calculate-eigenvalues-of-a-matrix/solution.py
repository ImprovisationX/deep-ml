import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix = np.array(matrix, dtype=float)
    eigenvalues = np.linalg.eigvals(matrix)

    return eigenvalues.tolist()