import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    m, n = A.shape
    U, s, Vh = np.linalg.svd(A, full_matrices=True)
    V = Vh.T
    rank = np.sum(s > tol)
    null_space_basis = V[:, rank:]
    return null_space_basis
    pass