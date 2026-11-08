import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    sum_sq = np.sum(x**2, axis=axis, keepdims=True)
    norm = np.sqrt(sum_sq + eps)
    normalized = x/norm
    return normalized
    pass
