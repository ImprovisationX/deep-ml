import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type == 'l1':
        return float(np.sum(np.abs(arr)))
    elif norm_type == 'l2':
        return float(np.sqrt(np.sum(arr**2)))
    elif norm_type == 'linf':
        return float(np.max(np.abs(arr)))
    elif norm_type == 'frobenius' and len(arr) == 2:
        return float(np.linalg.norm(arr, 'fro'))
    else:
        raise ValueError()
    
    pass
