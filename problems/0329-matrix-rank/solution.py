import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    mat = np.array(A, dtype=float).copy()

    if mat.ndim == 1:
        mat = mat.reshape(1, -1)
    if mat.size == 0:
        return 0

    m, n = mat.shape
    pivot_row = 0

    for col in range(n):
        if pivot_row >= m:
            break

        max_row = pivot_row + np.argmax(np.abs(mat[pivot_row:, col]))


        if np.abs(mat[max_row, col]) <= tol:
            continue


        if max_row != pivot_row:
            mat[[pivot_row, max_row]] = mat[[max_row, pivot_row]]

        pivot_val = mat[pivot_row, col]
        factors = mat[pivot_row + 1 :, col] / pivot_val
        mat[pivot_row + 1 :, col:] -= np.outer(factors, mat[pivot_row, col:])
        pivot_row += 1

    return pivot_row
    pass