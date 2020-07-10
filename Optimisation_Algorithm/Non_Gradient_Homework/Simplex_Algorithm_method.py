import time
import math
import numpy as np
def objfun(x):
    return 100*(x[0,0]**2-x[1,0])**2+(x[0,0]-1)**2
def Simplex_Algorithm(X,epsilon):
    k = 1
    F = np.zeros(3)
    F[0] = objfun(X[:,0:1])
    F[1] = objfun(X[:,1:2])
    F[2] = objfun(X[:,2:3])
    order= sorted(range(len(F)), key=lambda i: F[i])
    X = X[:,order]
    F = sorted(F)
    xs = X[:,0:1];fs = F[0]
    xm = X[:,1:2];fm = F[1]
    xl = X[:,2:3];fl = F[2]
    while True:
        xm_prime = (xm + xs)/2
        fm_prime = objfun(xm_prime)
        x1 = xm + xs - xl
        f1 = objfun(x1)
        if  f1 < fs:
            x2 = (5*xm + 5*xm - 6*xl)/4
            f2 = objfun(x2)
            if f1 <= f2:
                xl = xm;xm = xs;xs = x1
                fl = fm;fm = fs;fs = f1
            else:
                xl = xm;xm = xs;xs = x2
                fl = fm;fm = fs;fs = f2
        elif fs <= f1 and f1 < fm:
            xl = xm;xm = x1
            fl = fm;fm = f1
        elif fm <= f1 and f1 < fl:
            xl = x1
            fl = f1
        else:
            x3 = (3*xm + 3*xs - 2*xl)/4
            f3 = objfun(x3)
            if f3 < fs:
                xl = xm;xm = xs;xs = x3
                fl = fm;fm = fs;fs = f3
            elif fs <= f3 and f3 < fm:
                xl = xm;xm = x3
                fl = fm;fm = f3
            elif fm <= f3 and f3 < fl:
                xl = x3
                fl = f3
            else:
                xl_prime = (xl + xs)/2
                fl_prime = objfun(xl_prime)
                xm_prime = (xm + xs)/2
                X = np.hstack((np.hstack((xs,xl_prime)),xm_prime))
                F = np.array([fs,fl_prime,fm_prime])
                order = sorted(range(len(F)), key=lambda i: F[i])
                X = X[:,order]
                F= sorted(F)
                xs = X[:,0:1];fs = F[0]
                xm = X[:,1:2];fm = F[1]
                xl = X[:,2:3];fl = F[2]
        if (np.linalg.norm(xl-xs)+np.linalg.norm(xm-xs))/2 <= epsilon and math.sqrt(((fl-fs)**2+(fm-fs)**2)/2) <= epsilon:
            x_min = xs
            f_min = fs
            return x_min,f_min,k
        k += 1

if __name__ == '__main__':
    epsilon = float(input("Epsilon:"))
    start = time.time()
    X = np.random.randint(0,10,(2,3))
    print("起始矩阵：",X)
    x_min,f_min,k = Simplex_Algorithm(X,epsilon)
    end = time.time()
    x_min = x_min.reshape((1,2))[0]
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)
    print("Timer(/s):",end-start)