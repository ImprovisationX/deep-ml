import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	
	rows, cols = A.shape
	if x_ini == None:
		x = np.zeros_like(b)
	else: 
		x = np.array(x_ini, dtype=float)

	for _ in range(n):
		for r in range(rows):
			sum_ = np.dot(A[r], x) - A[r][r]*x[r]
			x[r] = (b[r] - sum_)/A[r][r]
	
	return x
