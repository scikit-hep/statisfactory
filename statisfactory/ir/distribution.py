from .ir_base import ir_base
import pprint as pp


class distribution(ir_base):
    def __init__(self, observables: dict, parameters: dict, description: dict):
        self._observables = observables
        self._parameters = parameters
        deps = {}
        deps.update(observables)
        for k, p in parameters.items():
            if k in deps:
                raise ValueError('key %s already in dependencies' % k)
            else:
                deps[k] = p
        if 'expression' not in description:
            raise ValueError('Distributions must have an expression in their description')
        super(distribution, self).__init__(deps, description)

    def __repr__(self):
        out = str(type(self)) + ' :\t\n'
        out += '\tobservables : ' + pp.pformat(self._observables) + '\n'
        out += '\tparameters  : ' + pp.pformat(self._parameters) + '\n'
        out += '\texpression  : ' + pp.pformat(self._description['expression'])
        return out
