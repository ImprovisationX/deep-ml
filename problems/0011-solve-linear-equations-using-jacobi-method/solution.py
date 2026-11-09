import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	A = A.astype(float)
	b = b.astype(float)
	rows, cols = A.shape

	x = np.zeros_like(b)

	for _ in range(n):
		x_tmp = np.zeros_like(x)
		for i in range(rows):
			sum_ = np.dot(A[i], x) - A[i][i]*x[i]
			x_tmp[i] = (b[i] - sum_)/A[i][i]
		x = x_tmp
	return x