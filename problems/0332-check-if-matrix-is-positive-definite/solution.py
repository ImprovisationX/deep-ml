import numpy as np

def check_positive_definite(matrix: list) -> dict:
    A = np.array(matrix, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1] or A.shape[0] == 0:
        return -1

    if not np.all(np.isfinite(A)):
        return -1

    eigenvalues = np.linalg.eigvals(A).real

    eigenvalues = np.sort(eigenvalues)
    eigenvalues = np.round(eigenvalues, 4)

    is_symmetric = np.allclose(A, A.T)
    is_pd = is_symmetric and np.all(eigenvalues > 1e-10)

    return {
        'is_positive_definite': bool(is_pd),
        'eigenvalues': eigenvalues.tolist()
    }