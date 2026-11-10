import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    xtx = X.T @ X
    xtx_inv = np.linalg.inv(xtx)
    xty = X.T @y

    
    return xtx_inv @ xty