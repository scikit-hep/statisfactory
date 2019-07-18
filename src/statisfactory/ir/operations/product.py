from ..operation import operation


class product(operation):
    def __init__(self, multiplicands: list):
        desc = {}
        super(product, self).__init__(multiplicands, desc)
