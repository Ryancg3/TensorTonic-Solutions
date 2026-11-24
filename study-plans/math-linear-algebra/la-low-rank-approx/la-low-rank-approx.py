import numpy as np

def low_rank_approximation(A: list, r: int) -> np.ndarray:
    """
    Returns the best rank-r float64 approximation.
    """
    A = np.asarray(A, dtype=float)
    U, s, Vt = np.linalg.svd(A, full_matrices=False)

    return (U[:, :r] * s[:r]) @ Vt[:r]