import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A, dtype=float)
    splits = np.split(A,indices_or_sections=A.shape[0], axis=0)
    # Write code here
    splits_reshape = [i.reshape(-1,1) for i in splits]  
    return np.hstack(splits_reshape)
