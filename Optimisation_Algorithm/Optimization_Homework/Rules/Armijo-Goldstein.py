import numpy as np
import matplotlib.pyplot as plt

def objfun(xk):
    y = (3*xk[0,0]-4)**2 + (4*xk[1,0]**2-2)**2
    return y

def gradobjfun(xk):
    y = np.array([[6*(3*xk[0,0]-4)],[16*xk[1,0]*(4*xk[1,0]**2-2)]])
    return y

def phi(alpha, xk):
    dk = -gradobjfun(xk)
    y = objfun(xk+alpha*dk)
    return y

def gradphi(alpha, xk):
    dk = -gradobjfun(xk)
    y = gradobjfun(xk+alpha*dk).T*dk
    return y

def Armijo_Goldstein(alpha0, xk):
    a1 = 0
    a2 = float("inf")
    alpha = alpha0
    rho = 0.3
    phi0 = phi(0, xk)
    gradphi0 = gradphi(0, xk)
    while True:
        phialpha = phi(alpha, xk)
        if phialpha <= phi0+rho*gradphi0[0,0]*alpha:
            if phialpha >= phi0+(1-rho)*gradphi0[0,0]*alpha:
                alpha_star = alpha
                break
            else:
                a1 = alpha
                if a2 < float("inf"):
                    alpha = (a1 + a2)/2
                else:
                    alpha = 1.5*alpha
        else:
            a2 = alpha
            alpha = (a1 + a2)/2
    print(alpha_star)
        
if __name__ == "__main__":
    alpha0 = 6
    xk = np.array([[0],[0]])
    Armijo_Goldstein(alpha0, xk)
    