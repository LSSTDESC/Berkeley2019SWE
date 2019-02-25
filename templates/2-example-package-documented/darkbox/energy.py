import numpy as np


def square(x):
    r"""Calculate the sum-of-squares energy of the input.

    We use the following definition for energy:

    .. math::
 
       E_{s} = \left< x(t),x(t) \right> = \int_{-\infty}^{\infty}{|x(t)|^{2}}dt

    Parameters
    ----------
    x : ndarray
        Input signal.

    Returns
    -------
    e : float
        Energy of the signal `x`.

    Notes
    -----
    Mathematics can also be used inline, :math:`\int_0^\infty f(x)
    dx`.  In the source code, note the ``r`` before the docstring
    start.  This means Python interprets the docstring literally,
    without escaping, otherwise we need quite a few more back-slashes
    in there.

    References
    ----------
    .. [0] numpydoc docstring guide, https://numpydoc.readthedocs.io/en/latest/format.html

    """
    return np.sum(x**2)
