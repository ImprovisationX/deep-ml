import numpy as np

def pairwise_cosine_similarity(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    safe_norm = np.where(norms==0.0, 1.0, norms)
    normalized_X = X/safe_norm
    return np.dot(normalized_X, normalized_X.T)
    pass