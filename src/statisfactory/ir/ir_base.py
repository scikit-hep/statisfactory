import pprint


class ir_base(object):
    def __init__(self, dependencies, description):
        self._dependencies = dependencies
        self._description = description

    @property
    def dependencies(self):
        return self._dependencies

    @property
    def description(self):
        return self._description

    def __repr__(self):
        out = str(type(self)) + ':\n'
        out += '\tdependencies: ' + pprint.pformat(self._dependencies)
        out += '\n'
        out += '\tdescription : ' + pprint.pformat(self._description)
        return out
