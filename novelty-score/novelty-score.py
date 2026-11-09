import numpy as np
def novelty_score(recommendations: list, item_counts: list, n_users: int) -> float:
    """
    Returns the average self-information of the recommended items.
    """
    item_counts = np.asarray(item_counts, dtype=float)
    if len(recommendations) == 0:
        return 0.0
    return np.mean(-np.log2(item_counts/n_users))