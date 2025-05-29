import numpy as np

# First base
base1 = np.array(
    [[7, 4, 1, 6],
     [2, 5, 8, 3],
     [8, 3, 2, 5],
     [1, 6, 7, 4]
     ])

# Second base
base2 = np.roll(base1, (2, 0), axis=(1, 0))

# Set up the four types of masks
mask1A = np.array(
    [[0, 1, 0, 1],
     [0, 1, 0, 1],
     [1, 0, 1, 0],
     [1, 0, 1, 0]
     ])

mask1B = np.roll(mask1A, (1, 0), axis=(1, 0))
mask2A = mask1B
mask2B = mask1A


def generate_grid(k: int, M: int, low=1) -> dict:
    """

    :param low: int
    :rtype: dict
    :param M: int
    :param k: int
    """

    if low > M / 4:
        raise IndexError("Min value cannot be > M/4.")

    if 0 < k < 5:
        grid = base1
    elif 4 < k < 9:
        grid = base2
    else:
        raise IndexError("Index out of bounds: should be 1-8.")

    if k == 1 or k == 5:
        res = {'grid': grid, 'maskA': mask1A, 'maskB': mask1B}
    elif k == 2 or k == 6:
        res = {'grid': np.fliplr(grid), 'maskA': mask2A, 'maskB': mask2B}
    elif k == 3 or k == 7:
        res = {'grid': np.fliplr(np.flipud(grid)), 'maskA': mask1A, 'maskB': mask1B}
    elif k == 4 or k == 8:
        res = {'grid': np.flipud(grid), 'maskA': mask2A, 'maskB': mask2B}
    else:
        res = {'grid': grid, 'maskA': mask1A, 'maskB': mask1B}

    m_A = res["maskA"]
    m_B = res["maskB"]

    a = grid * m_A
    b = grid * m_B

    m = M - low - 22
    res["result"] = a + b + (m_A * int(m / 2 - 1)) + (m_B * (low - 1))

    # print("base:\n", res, "\n")
    return res
