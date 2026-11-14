import numpy as np

def low_rank_approximation(delta_W: np.ndarray, r: int) -> list:
    U, S, Vt = np.linalg.svd(delta_W, full_matrices=False)

    U_r = U[:, :r]
    S_r = S[:r]
    Vt_r = Vt[:r, :]

    approx = U_r @ np.diag(S_r) @ Vt_r
    return approx.tolist()
    pass