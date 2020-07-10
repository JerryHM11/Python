import time
import numpy as np
import scipy.optimize as opt
def objfun(D,x):
    y = 0
    for i in range(0,D-1):
        y = y + 100*(x[i,0]**2-x[i+1,0])**2+(x[i,0]-1)**2
    return y
def phi_ADM(alpha):
    return objfun(D,zk + alpha*(E[i].reshape(D,1)))
def phi_HJM(alpha):
    return objfun(D,x + alpha*dk)
def Hooke_Jeeves_method(D,x0,epsilon):
    global zk,dk,x,i,E
    E = np.eye(D)
    xk = x0;y = xk;k = 0
    value_number = 0
    find_number = 0
    while True:
        zk = y
        for i in range(D):
            di = E[i].reshape(D,1)
            alpha = opt.minimize_scalar(phi_ADM).x
            zk = zk + alpha*di
            value_number += 1
            find_number += 1
        x = zk
        if np.linalg.norm(x-xk)<epsilon and abs(objfun(D,x)-objfun(D,xk))<epsilon:
            x_min = x
            f_min = objfun(D,x_min)
            return x_min,f_min,k,value_number,find_number
        else:
            value_number += 1
        dk = x-xk
        landa = opt.minimize_scalar(phi_HJM).x
        value_number += 1
        find_number += 1
        y = x+landa*dk
        xk = x
        k += 1
        
if __name__ == "__main__":
    D = int(input("Dimension:"))
    epsilon = float(input("Epsilon:"))
    start = time.time()
    x0 = np.zeros((D,1))
    x_min,f_min,k,vnum,fnum = Hooke_Jeeves_method(D,x0,epsilon)
    end = time.time()
    print("x_min:",x_min.reshape(1,D)[0])
    print("f_min:",f_min)
    print("迭代数:",k)
    print("调用目标函数次数:",vnum)
    print("一维搜索次数:",fnum)
    print("Time(/s):",end-start)