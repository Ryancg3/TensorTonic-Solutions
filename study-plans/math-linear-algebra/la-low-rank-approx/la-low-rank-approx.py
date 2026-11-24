import numpy as np

def low_rank_approximation(A: list, r: int) -> np.ndarray:
    """
    Returns the best rank-r float64 approximation.
    """
    A = np.asarray(A, dtype=float)
    U, s, V = np.linalg.svd(A)

    return U[:, :r] @ np.diag(s[:r]) @ V.T[:r,:]