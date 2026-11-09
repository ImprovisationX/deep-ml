import numpy as np

def gaussian_elimination(A, b):
	A = np.array(A, dtype = float)
	b = np.array(b, dtype = float)
	
	rows, cols = A.shape
	r = 0
	for c in range(cols):
		if r >= rows:
			break
		
		pivot_row = np.argmax(np.abs(A[r:, c])) + r
		
		if np.abs(A[pivot_row, c]) < 1e-10:
			continue
		if pivot_row != r:
			A[[pivot_row, r]] = A[[r, pivot_row]]
			b[[pivot_row, r]] = b[[r, pivot_row]]
		
		for i in range(r + 1, rows):
			factor = A[i, c] / A[r, c]
			A[i] -= A[r]*factor
			b[i] -= b[r]*factor
		r += 1
	x = np.zeros_like(b)
	n = len(x)
	for i in range(n - 1, -1, -1):
		if A[i][i] != 0:
			x[i] = (b[i] - np.sum(A[i] * x))/A[i][i]
	
	return x
