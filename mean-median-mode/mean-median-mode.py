from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    median = np.median(x)
    values = Counter(x)
    mode = min([k for k, v in values.items() if v == max(values.values())])
    return {"mean": mean.item(), "median": median.item(), "mode": mode.item()}
    