from scipy.optimize import minimize
import numpy as np
# function, fun, that we want to minimize
fun = lambda x: (x[0]-x[1])**2 + (x[1]+x[2]-2)**2 + (x[3]-1)**2 + (x[4]-1)**2
# initial guess for [x[0], x[1], ..., x[4])
xinit = [1, 1, 1, 1, 1]
# constraints for fun from the problem
constr = ({"type": "eq", "fun": lambda x: x[0] + 3*x[2]},
          {"type": "eq", "fun": lambda x: x[2] + x[3] - 2*x[4]},
          {"type": "eq", "fun": lambda x: x[1] - x[4]})
# bounds for the possible values of x[i]
bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))
# performing the minimizing of fun subject to the contrainst and bounds that were defined with the initial guess
res = minimize(fun, xinit, method='SLSQP', bounds=bnds, constraints=constr)
# printing the answer so it is easy to see
print(res.x)
