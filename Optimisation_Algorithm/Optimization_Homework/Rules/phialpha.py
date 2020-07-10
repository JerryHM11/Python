import numpy as np
import matplotlib.pyplot as plt
def objfun(x):
    y = (3*x[0,0]-4)**2 + (4*x[1,0]**2-2)**2
    return y
def gradobjfun(x):
    y = np.array([[6*(3*x[0,0]-4)],[16*x[1,0]*(4*x[1,0]**2-2)]])
    return y
def phi(alpha, xk):
    dk = -gradobjfun(xk)
    y = objfun(xk+alpha*dk)
    return y
if __name__ == "__main__":
    alpha = np.arange(0,2.1,0.1)
    xk = np.array([[0],[0]])
    phialpha = [phi(i, xk) for i in alpha]
    print(phialpha)
    plt.plot(alpha, phialpha, "*")
    plt.show()