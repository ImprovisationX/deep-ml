import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    gradient = np.array(gradient, dtype=float)
    magnitude = np.linalg.norm(gradient)

    if magnitude == 0:
        direction = 0*gradient
        descent_direction = -direction
    else:
        direction = gradient/magnitude
        descent_direction = -direction
    return {
        'magnitude': magnitude,
        'direction': direction,
        'descent_direction': descent_direction
    }
    pass