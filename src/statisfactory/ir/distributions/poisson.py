from ..distribution import distribution


class poisson(distribution):
    def __init__(self, x, mean):
        obs = {'x': x}
        params = {'mean': mean}
        desc = {'expression': '(mean**x)*exp(mean)/factorial(x)'}
        super(poisson, self).__init__(obs, params, desc)
