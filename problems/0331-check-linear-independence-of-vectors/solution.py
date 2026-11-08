import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    if not vectors:
        return True
    

    if len(vectors) > len(vectors[0]):
        return False
        
    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    
    return rank == len(vectors)
    pass