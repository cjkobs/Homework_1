from scipy.optimize import minimize
import numpy as np

# We want to minimize ||f(x)-xinit|| subject to f(x) = 0
fun = lambda x: (x[0]-x[1])**2 + (x[1]+x[2]-2)**2 + (x[3]-1)**2+(x[4]-1)**2

# initial guess
xinit = [10, 10, 10, 10, 10]
# the euclidean norm of f-xinit
# constraint f(x) = 0:
constr = ({"type": "ineq", "fun": lambda x: x[0] + 3*x[2]},
          {"type": "ineq", "fun": lambda x: x[2] + x[3] - 2*x[4]},
          {"type": "ineq", "fun": lambda x: x[1] - x[4]})
bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))
res = minimize(fun, xinit, method='SLSQP', bounds=bnds, constraints=constr)
print(res.x)
