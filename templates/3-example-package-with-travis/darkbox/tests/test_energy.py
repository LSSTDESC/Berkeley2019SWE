from darkbox import energy

import numpy as np
from numpy.testing import assert_equal


def test_square():
    x = np.array([1, 2, 3, 4])
    assert_equal(energy.square(x), 30)
