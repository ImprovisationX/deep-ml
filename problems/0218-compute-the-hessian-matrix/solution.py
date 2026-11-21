from typing import Callable
import numpy as np
def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
    x = np.array(point, dtype=float)
    n = len(x)
    H = np.zeros((n, n), dtype=float)
    f_x = f(x.tolist())

    for i in range(n):
        e_i = np.zeros(n)
        e_i[i] = h

        H[i, i] = (f((x + e_i).tolist()) - 2 * f_x + f((x - e_i).tolist())) / (
            h**2
        )

        for j in range(i + 1, n):
            e_j = np.zeros(n)
            e_j[j] = h

            val = (
                f((x + e_i + e_j).tolist())
                - f((x + e_i - e_j).tolist())
                - f((x - e_i + e_j).tolist())
                + f((x - e_i - e_j).tolist())
            ) / (4 * (h**2))

            H[i, j] = val
            H[j, i] = val

    return H.tolist()
    pass