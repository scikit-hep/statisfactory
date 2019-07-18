import pytest


def test_simple_construct():
    from statisfactory.ir import (poisson, gaussian, product)
    
    expected = b"<class 'statisfactory.ir.product.product'> :\t\n\toperands     : [\n <class 'statisfactory.ir.poisson.poisson'> :\t\n\tobservables : {'x': 'x'}\n\tparameters  : {'mean': 'mean'}\n\texpression  : '(mean**x)*exp(mean)/factorial(x)'\n <class 'statisfactory.ir.gaussian.gaussian'> :\t\n\tobservables : {'x': 'x'}\n\tparameters  : {'mean': 'mean', 'sigma': 'sigma'}\n\texpression  : 'exp(-0.5*((x-mean)/sigma)**2'\n ]"

    a = poisson('x','mean')
    b = gaussian('x','mean','sigma')
    p = product([a,b])
    print(p.__repr__() == expected.decode())
