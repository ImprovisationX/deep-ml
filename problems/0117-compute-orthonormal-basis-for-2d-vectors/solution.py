import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    vectors = np.array(vectors, dtype=float)
    basis = []
    for v in vectors:

        for b in basis:
            v = v - np.dot(v, b)*b
        
        norm = np.linalg.norm(v)

        if norm > tol: 
            v /= norm
            basis.append(v)

    return basis
    pass