import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	a = np.array(a)
	b = np.array(b)
	if len(a) != len(b):
		return -1
	return (a + b).tolist()
	pass