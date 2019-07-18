from ..distribution import distribution


class gaussian(distribution):
    def __init__(self, x, mean, sigma):
        obs = {'x': x}
        params = {'mean': mean, 'sigma': sigma}
        desc = {'expression': 'exp(-0.5*((x-mean)/sigma)**2'}
        super(gaussian, self).__init__(obs, params, desc)
