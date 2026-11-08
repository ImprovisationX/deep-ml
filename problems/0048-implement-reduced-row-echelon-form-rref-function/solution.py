import numpy as np

def rref(matrix):
	matrix = np.array(matrix, dtype=float)
	rows, cols = matrix.shape
	r = 0
	for c in range(cols):
		if r >= rows:
			break
		
		pivot_row = np.argmax(np.abs(matrix[r:, c])) + r

		if np.abs(matrix[pivot_row, c]) < 1e-10:
			continue
		
		if pivot_row != r:
			matrix[[r, pivot_row]] = matrix[[pivot_row, r]]
		matrix[r] = matrix[r] / matrix[r, c]
		for i in range(rows):
			if i != r:
				factor = matrix[i, c]
				matrix[i] -= factor*matrix[r]
		r += 1
	return matrix.tolist()
	pass
