import numpy as np
import matplotlib.pyplot as plt

def objfun(x):
    return 1/3*x[0,0]**2+1/2*x[1,0]**2
def gradobjfun(x):
    return np.array([[2/3*x[0,0]],[x[1,0]]])
def phi(alpha):
    dk = -gradobjfun(x)
    return objfun(x+alpha*dk)
def GoldenSearch(x):
    epsilon = 1e-8
    tua = 0.618;ak = 0;bk = 2
    while True:
        if bk - ak < epsilon:
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
def Steepest_Descent_method(x,epsilon):
    X1 = [];X2 = []
    X1.append(x[0,0])
    X2.append(x[1,0])
    k = 0
    while True:
        gk = gradobjfun(x)
        if np.linalg.norm(gk) < epsilon:
            return np.hstack((x[0],x[1])), objfun(x), k, X1, X2
        dk = -gk
        alpha = GoldenSearch(x)
        x = x+alpha*dk
        k+=1
        X1.append(x[0,0])
        X2.append(x[1,0])
    
if __name__ == "__main__":
    epsilon = float(input("阀值："))
    x = np.array([[3],[2]])
    x_min,f_min,k,X1,X2 = Steepest_Descent_method(x,epsilon)
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)
    x1 = np.arange(-1, 3.5 + 0.05, 0.05)
    x2 = np.arange(-1, 2.5 + 0.05, 0.05)
    [x1, x2] = np.meshgrid(x1, x2)
    f = 1/3*x1**2+1/2*x2**2  # 给定的函数
    plt.contour(x1, x2, f, 20)  # 画出函数的20条轮廓线
    plt.plot(X1,X2,"g*-")
    plt.show()