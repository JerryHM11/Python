import time
import scipy
import numpy as np
import scipy.optimize as opt
def objfun(D,x):
    y = 0
    for i in range(0,D-1):
        y = y + 100*(x[i,0]**2-x[i+1,0])**2+(x[i,0]-1)**2
    return y
def phi(alpha):
    return objfun(D,zk + alpha*dk)
def Rosenbrock_method(D,x,epsilon):
    global zk,dk
    E = np.eye(D)
    xk = x;k = 0
    value_number = 0
    find_number = 0
    x_value = np.eye(D)
    while True:
        alpha_value = []
        zk = xk
        for i in range(D):
            dk = E[:,i:i+1]
            alpha = opt.minimize_scalar(phi).x
            zk = zk + alpha*dk
            alpha_value.append(alpha)
            x_value[:,i:i+1] = zk
            value_number += 1
            find_number += 1
        x = zk
        if np.linalg.norm(x-xk)<epsilon and abs(objfun(D,x)-objfun(D,xk))<epsilon:
            x_min = x
            f_min = objfun(D,x_min)
            return x_min,f_min,k,value_number,find_number
        else:
            value_number += 1
        xk = x
        k += 1
        for i in range(D):
            if alpha_value[i] != 0:
                e = np.zeros((D,1))
                for j in range(i,D):
                    e = e + alpha_value[j]*E[:,j:j+1]
                E[:,i:i+1] = e
        E = scipy.linalg.orth(E)

if __name__ == "__main__":
    D = int(input("Dimension:"))
    epsilon = float(input("Epsilon:"))
    start = time.time()
    x = np.zeros((D,1))
    x_min,f_min,k,vnum,fnum = Rosenbrock_method(D,x,epsilon)
    end = time.time()
    print("x_min:",x_min.reshape(1,D)[0])
    print("f_min:",f_min)
    print("迭代数:",k)
    print("调用目标函数次数:",vnum)
    print("一维搜索次数:",fnum)
    print("Time(/s):",end-start)