import numpy as np
def calibrate_isotonic(cal_labels: list, cal_probs: list, new_probs: list) -> list:
    """
    Returns a list of calibrated probabilities.
    """
    #arrays
    cal_labels = np.asarray(cal_labels, dtype=float)
    cal_probs = np.asarray(cal_probs, dtype=float)
    new_probs = np.asarray(new_probs, dtype=float)
    #sorting
    cal_probs_order = np.argsort(cal_probs) 
    cal_labels = cal_labels[cal_probs_order]

    blocks = [[i] for i in range(len(cal_labels))]

    i = 0
    while i < len(blocks) - 1:
        if np.mean(cal_labels[blocks[i]]) > np.mean(cal_labels[blocks[i+1]]):
            blocks[i:i+2] = [blocks[i] + blocks[i+1]]   # merge i and i+1
            if i > 0:
                i -= 1      # merged block may now be smaller than the one before it
        else:
            i += 1

    for i in blocks:
        if len(blocks) > 1:
            cal_labels[i] = np.mean(cal_labels[i])
    
    cal_labels = np.clip(cal_labels, 0,1)
    
    neigh = np.interp(new_probs, cal_probs, cal_labels)

    return neigh.tolist()