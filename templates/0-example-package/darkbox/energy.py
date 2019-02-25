import numpy as np


def square(x):
    """Calculate the sum-of-squares energy of the input.

    Parameters
    ----------
    x : ndarray
        Input signal.

    Returns
    -------
    e : float
        Energy of the signal `x`.
    """
    return np.sum(x**2)
