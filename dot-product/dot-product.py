import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    return np.dot(np.asarray(x, dtype=float),np.asarray(y, dtype=float)).item() 