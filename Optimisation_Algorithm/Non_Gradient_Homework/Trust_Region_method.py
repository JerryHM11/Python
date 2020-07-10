import time
import numpy as np
import scipy.optimize as opt
def objfun(x):
    return (x[0,0]-2)**4 + (x[0,0]-2*x[1,0])**2
def gradobjfun(x):
    return np.array([[4*(x[0,0]-2)**3+2*(x[0,0]-2*x[1,0])],[8*x[1,0]-4*x[0,0]]])
def Hessen(x):
    return np.array( [[12*(x[0,0]-2)**2+2,-4],[-4,8]])
def mk(x,dk):
    return objfun(x) + np.dot(gk.T,dk) + 0.5*np.dot(np.dot(dk.T,Gk),dk)
def Trust_Region(x,epsilon):
    eta1 = 0.1;eta2 = 0.75
    gama1 = 0.5;gama2 = 2
    derta_ba = 3;derta0 = 1
    k = 0;xk = x
    global gk,dk,Gk
    dertak = derta0
    while True:
        gk = gradobjfun(xk)
        Gk = Hessen(xk)
        if np.linalg.norm(gk) <= epsilon:
            x_min = xk
            f_min =objfun(xk)
            return x_min,f_min,k
        if np.dot(np.dot(gk.T,Gk),gk) <= 0:
            dk = -(dertak/np.linalg.norm(gk))*gk
        else:
            dk = -min(np.linalg.norm (gk)**2/np.dot(np.dot(gk.T,Gk),gk),dertak/np.linalg.norm (gk))*gk
        rhok = (objfun(xk)-objfun(xk+dk))/(mk(xk,np.zeros((2,1)))-mk(xk,dk))
        if rhok <= eta1:
            dertak = gama1*dertak
        elif rhok >= eta2 and (np.linalg.norm(dk) <= dertak+epsilon and np.linalg.norm(dk) <= dertak-epsilon):
            dertak = min(gama2*dertak,derta_ba)
        if rhok > eta1:
            xk = xk+dk
        k+=1

if __name__ == '__main__':
    x = np.random.randint(0,10,(2,1))
    epsilon = float(input("Epsilon:"))
    start = time.time()
    x_min,f_min,k = Trust_Region(x,epsilon)
    end = time.time()
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)
    print("Time(/s):",end-start)