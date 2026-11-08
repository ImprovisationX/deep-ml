import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix = np.array(matrix)
	axis = 0
	if mode == 'row':
		axis = 1
	means = np.mean(matrix, axis=axis)
	
	return means.tolist()