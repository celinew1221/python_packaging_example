# relative path only work for packaging but if you call this within the package it won't work
# so if you want to call main, and print to test this package, try
# python3 -m python_packaging_example.main
# python3 -m python_packaging_example.print

from . import module_b
from . import module_a
import numpy as np

def print():
    module_b.b.b()
    module_a.a1(np.array([0,0,0,0,0,1]))

if __name__=="__main__":
    print()
