import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a_norm = np.linalg.norm(a, ord=2)
    b_norm = np.linalg.norm(b, ord=2)
    if a_norm == 0 or b_norm == 0:
        return float(0)
    return (np.dot(a,b)/(a_norm * b_norm)).item()