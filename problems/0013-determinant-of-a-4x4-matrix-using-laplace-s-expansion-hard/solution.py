def determinant_4x4(matrix: list[list[int|float]]) -> float:
	n = len(matrix)
	if n == 1:
		return maxtrix[0][0]

	if n == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	det = 0.0
	for col in range(n):
		submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
		sign = (-1)**col
		det += sign*matrix[0][col]*determinant_4x4(submatrix)
	return det