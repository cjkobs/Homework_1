from scipy.optimize import minimize
import numpy as np

# We want to minimize ||f(x)-xinit|| subject to f(x) = 0

f = (-4*x[0])**2 + (3*x[0]-x[1]-2)**2 + (x[1]-1)**2 + (x[0]-1)**2
# the euclidean norm of f-xinit
objfun = lambda x, xinit: np.sqrt(np.sum((f(x)-xinit)**2))

# initial guess
xinit = [1, 1]
# constraint f(x) = 0:
constr = {"type": "eq", "fun": f}
res= minimize(fun=objfun, args=(xinit,), x0=xinit, constraints=constr)
print(res.x)