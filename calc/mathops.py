import numpy as np
import sys

def get_randn(n=10):
    randints = np.random.randint(100, size=n)
    return ":".join(["%02d" % i for i in randints])
