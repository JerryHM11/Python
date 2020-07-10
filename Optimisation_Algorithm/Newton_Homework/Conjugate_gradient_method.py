import time
import numpy as np
def objfun(x):
    return (x[1,0]-x[0,0]**2)**2+(1-x[0,0])**2
def gradobjfun(x):
    return np.array([[4*x[0,0]**3-4*x[0,0]*x[1,0]+2*x[0,0]-2],[2*x[1,0]-2*x[0,0]**2]])
def phi(alpha):
    dk = -gradobjfun(x)
    return objfun(x+alpha*dk)
def GoldenSearch(x):
    sita = 1e-10
    tua = 0.618;ak = 0;bk = 2
    while True:
        if bk - ak < sita:
            alpha = (ak+bk)/2
            return alpha
        else:
            landa = ak + (1-tua)*(bk - ak)
            miu = ak + tua*(bk - ak)
            flanda = phi(landa)
            fmiu = phi(miu)
            if flanda>fmiu:
                ak = landa
            else:
                bk = miu
def Conjugate_gradient_method(x,epsilon):
    k = 0
    while True:

        gk = gradobjfun(x)
        if np.linalg.norm(gk) < epsilon:
            return np.hstack((x[0],x[1])), objfun(x), k
        if k == 0:
            dk = -gk
        else:    #beta选择了Fletcher-Reever(FR)公式
            beta = 1.0*(np.dot(gk.T,gk)[0,0])/(np.dot(g0.T,g0)[0,0])
            dk = -gk+beta*d0
            gd = np.dot(gk.T,dk)
            if gd >= 0:
                dk = -gk
        alpha = GoldenSearch(x)
        x = x+alpha*dk
        g0 = gk
        d0 = dk
        k+=1
        
if __name__ == '__main__':
    epsilon = float(input("阀值："))
    start = time.time()
    x = np.array([[3],[2]])
    x_min, f_min, k = Conjugate_gradient_method(x,epsilon)
    end = time.time()
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)
    print("Time(/s):",end-start)
