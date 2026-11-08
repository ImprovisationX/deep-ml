import numpy as np

def make_diagonal(x):
	dia_matrix = np.eye(len(x))
	for i in range(len(x)):
		dia_matrix[i][i] = x[i]
	return dia_matrix
	pass