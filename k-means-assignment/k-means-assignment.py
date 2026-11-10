import numpy as np
def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    
    points = np.asarray(points, dtype=float)
    centroids = np.asarray(centroids, dtype=float)
    sums = [np.sum((points - i)**2, axis=1, keepdims=True) for i in centroids]
    return np.argmin(np.hstack(sums),axis=1).tolist()
        