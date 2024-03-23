import numpy as np
import matplotlib.pyplot as plt
import bisect


def pdf_generation(X_, function, resolution: float, size: int):

    bins_count = int(len(function) / resolution)
    bins = [round(function[i*resolution]) for i in np.arange(bins_count)]
    cdf = np.cumsum(bins)
    N = cdf[-1]
    RandInt = np.random.randint(0, N, size)

    # Generate the distribution
    domain_min = min(X_)
    domain_max = max(X_)
    function_size = len(function)
    Y = [bisect.bisect_left(cdf, RandInt[i]) / function_size * domain_max - domain_min for i in RandInt]
    return Y


"""

Implementation Example

X = np.linspace(0, 1, 1000)
f = -X**2 + 2*X
Y = pdf_generation(X, f, 1, 10000)

plt.hist(Y)
plt.show()

"""
