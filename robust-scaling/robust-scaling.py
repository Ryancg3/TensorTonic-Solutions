import math
def robust_scaling(values: list) -> list:
    """
    Returns values centered by the median and scaled by the interquartile range.
    """
    values_sorted = sorted(values)
    if len(values) == 1:
        return [0.0]
    def median(values):
        if len(values) % 2 == 1:
            median_ind = [len(values)//2]
            median = values[min(median_ind)]
        else:
            median_ind = [len(values)//2 -1, len(values)//2]
            median = sum([values[i] for i in median_ind])/len(median_ind)
        
        return median, median_ind
    # Write code here
    median_val, median_ind = median(values_sorted)

    low_q_bound = max(median_ind)
    upper_q_bound = min(median_ind) +1
    print(low_q_bound)
    low_q_slice = values_sorted[:low_q_bound]
    upper_q_slice = values_sorted[upper_q_bound:]
    low_median, _  = median(low_q_slice)
    upper_median, _ = median(upper_q_slice)
    inter_q = upper_median - low_median
    print(inter_q)
    print(median_val)
    print(values)
    if inter_q == 0.0:
        return  [(i-median_val) for i in values]
    return [(i-median_val)/inter_q for i in values]
    
    