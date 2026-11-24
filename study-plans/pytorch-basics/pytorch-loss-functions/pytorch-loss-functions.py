import torch

def compute_loss(pred: torch.Tensor, target: torch.Tensor, method: str, delta: float = 1.0) -> float:
    """
    Returns the mean loss as a Python float.
    """
    if method == "mse":
        return ((pred - target)**2).mean().item()
    elif method == "cross_entropy":
        d, C = pred.shape
        shifted = pred - pred.max(dim=1, keepdim=True).values
        log_paritiion = shifted.exp().sum(dim=1).log()
        target_logits = shifted[torch.arange(d), target]
        return (log_paritiion - target_logits).mean().item()
    else: 
        a = (pred - target).abs()
        return (torch.where(a <= delta, 0.5*a**2, delta*(a - 0.5*delta))).mean().item()
