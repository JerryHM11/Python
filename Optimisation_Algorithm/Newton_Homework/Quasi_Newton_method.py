import sympy
import numpy as np
def Hessen(x):
    f = "(x2-x1**2)**2+(1-x1)**2"
    vars = sympy.symbols('x1 x2')
    x1= sympy.symbols('x1')
    x2= sympy.symbols('x2')
    f = sympy.sympify([f])
    H = sympy.zeros(len(vars),len(vars))
    for i ,fi in enumerate(f):
        for j,r in enumerate(vars):
            for k,s in enumerate(vars):
                H[j,k] = sympy.diff(sympy.diff(fi,r), s)
    H = H.subs({x1:x[0],x2:x[1]})
    return np.array(H)
def objfun(x):
    return (x[1,0]-x[0,0]**2)**2+(1-x[0,0])**2
def gradobjfun(x):
    return np.array([[4*x[0,0]**3-4*x[0,0]*x[1,0]+2*x[0,0]-2],[2*x[1,0]-2*x[0,0]**2]])
def phi(alpha):
    Dk = np.linalg.inv(Hessen(x))
    gk = gradobjfun(x)
    dk = -1.0*np.dot(Dk,gk)
    return objfun(x+alpha*dk)
def GoldenSearch(x):
    epsilon = 1e-5
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
def Quasi_Newton_methods(x,epsilon):
    k = 0
    Dk = np.linalg.inv(Hessen(x))
    x0 = x
    rho = 0.5
    while True:
        gk = gradobjfun(x0)
        if np.linalg.norm(gk) < epsilon:
            return np.hstack((x0[0],x0[1])),objfun(x0),k
        dk = -1.0*np.dot(Dk,gk)
        alpha = GoldenSearch(x0)
        x = x0 + alpha*dk
        sk = x - x0
        yk = gradobjfun(x) - gk
        if np.dot(sk.T,yk)[0,0] > 0:
            ak = np.dot(sk,sk.T)
            bk = np.dot(sk.T,yk)[0,0]
            ck = np.dot(np.dot(np.dot(Dk,yk),yk.T),Dk)
            dk = np.dot(np.dot(yk.T,Dk),yk)[0,0]
            Dk = Dk + ak/bk - ck/dk
        x0 = x
        k += 1
        
if __name__ == "__main__":
    epsilon = float(input("阀值："))
    x = np.array([[3],[2]])
    x_min, f_min, k = Quasi_Newton_methods(x,epsilon)
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)