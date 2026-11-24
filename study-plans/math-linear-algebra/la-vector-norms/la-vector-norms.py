import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    v = np.asarray(v, dtype=float)
    l_1 = np.sum(np.abs(v))
    l_2 = np.sqrt(np.sum(v**2))
    l_inf = np.max(np.abs(v))
    return np.array([l_1,l_2,l_inf])