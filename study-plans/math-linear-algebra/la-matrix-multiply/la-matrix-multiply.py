import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    
    return np.asarray(A, dtype=float) @ np.asarray(B, dtype=float)