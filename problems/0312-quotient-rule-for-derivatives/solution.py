import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g = np.array(g_coeffs, dtype=float)
    h = np.array(h_coeffs, dtype=float)
    gx = np.polyval(g, x)
    hx = np.polyval(h, x)

    g_prime = np.polyder(g)
    h_prime = np.polyder(h)

    gx_prime = np.polyval(g_prime, x)
    hx_prime = np.polyval(h_prime, x)

    result = (gx_prime * hx - gx * hx_prime) / (hx ** 2)

    return float(result)
    pass