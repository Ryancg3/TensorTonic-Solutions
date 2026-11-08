import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X = np.asarray(X, dtype=float)
    min = np.min(X, axis=axis, keepdims=True)
    max = np.max(X, axis=axis, keepdims=True)

    data_range = max -min 
    safe_range = np.where(data_range > eps, data_range, 1.0)
    output = (X - min)/safe_range
    return output#np.where((output < eps) | np.isnan(output), 0.0, output)
    
    