try:
    from . import module_b
    from . import module_a
except (SystemError or ImportError):
    # for local call teseting, usage
    import module_b
    import module_a
import numpy as np

def print():
    module_b.b.b()
    module_a.a1(np.array([0,0,0,0,0,1]))
