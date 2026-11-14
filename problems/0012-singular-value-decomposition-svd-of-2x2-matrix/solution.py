import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    U, S, Vt = np.linalg.svd(A)
    return U, S, Vt
    pass