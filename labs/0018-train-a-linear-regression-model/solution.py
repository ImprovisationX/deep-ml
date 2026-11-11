# --- cell 1 ---
import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    alpha = 0.01
    eps = 1e-6
    n = len(X)
    W = np.asarray(W, dtype=float).copy()
    b = np.asarray(b, dtype=float).copy()
    for _ in range(10000):
        y_pred = X@W + b
        error = y_pred - y
        
        dW = (X.T@error)/n
        db = np.mean(error)
        
        grad_norm = np.sqrt(np.sum(dW**2) + db**2)

        if grad_norm < eps:
            break
        W -= alpha*dW
        b -= alpha*db
        
    return W, b
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    pass