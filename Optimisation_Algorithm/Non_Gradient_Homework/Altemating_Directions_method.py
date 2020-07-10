import time
import numpy as np
import scipy.optimize as opt
def objfun(D,x):
    y = 0
    for i in range(0,D-1):
        y = y + 100*(x[i,0]**2-x[i+1])**2+(x[i,0]-1)**2
    return y
def phi(alpha):
    E = np.eye(D)
    return objfun(D,zk + alpha*(E[i].reshape(D,1)))
def Alternating_Directions_method(D,x0,epsilon):
    global zk,i
    E = np.eye(D)
    xk = x0;k = 0
    value_number = 0
    find_number = 0
    while True:
        zk = xk
        for i in range(D):
            di = E[i].reshape(D,1)
            alpha = opt.minimize_scalar(phi).x
            value_number += 1
            find_number += 1
            zk = zk + alpha*di
        x = zk
        if np.linalg.norm(x-xk)<epsilon and abs(objfun(D,x)-objfun(D,xk))<epsilon:
            x_min = x
            f_min = objfun(D,x_min)
            return x_min,f_min,k,value_number,find_number
        else:
            value_number += 1
        xk = x
        k += 1
        
if __name__ == "__main__":
    D = int(input("Dimension:"))
    epsilon = float(input("Epsilon:"))
    start = time.time()
    x0 = np.zeros((D,1))
    x_min,f_min,k,vnum,fnum = Alternating_Directions_method(D,x0,epsilon)
    end = time.time()
    print("x_min:",x_min.reshape(1,D)[0])
    print("f_min:",f_min)
    print("迭代数:",k)
    print("调用目标函数次数:",vnum)
    print("一维搜索次数:",fnum)
    print("Time(/s):",end-start)