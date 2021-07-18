import numpy as np

# Do we only want to generate a single value at a time... I guess probably
def generate_voltages(mean, std):
    """
    Generates a single value give the gaussian conditions """
    return(np.random.normal(mean,std, 1))

class signal:
    def __init__(self, mean: float,std: float):
        self.mean = mean
        self.std = std

    def