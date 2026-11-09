import numpy as np

def rnn_step_backward(dh: list, cache: list) -> dict:
    """
    Returns a dictionary with dx_t, dh_prev, dW, dU, and db.
    """
    dh = np.asarray(dh, dtype=float)
    cache = [np.asarray(i, dtype=float) for i in cache]
    x_t, h_prev, h_t, W, U, b = cache
    dz = dh * (1- h_t**2)
    dx_t = W.T @ dz
    dh_prev = U.T @ dz
    dW = np.tensordot(dz,x_t, axes=0)
    dU = np.tensordot(dz,h_prev, axes=0)
    return {"dx_t": dx_t, 
            "dh_prev": dh_prev, 
            "dW": dW, 
            "dU": dU, 
            "db": dz}