import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	maxtrix = np.array(matrix)
	detM = np.linalg.det(matrix)
	traceM = np.trace(matrix)
	return (detM, traceM)
	pass