import sympy
import numpy as np
def objfun(x):
    return (3*x[0,0]-4)**2+(4*x[1,0]**2-2)**2
def gradobjfun(x):
    return np.array([[18*x[0,0]-24],[64*x[1,0]**3-32*x[1,0]]])
def Hessen(f,x):
    vars = sympy.symbols('x1 x2')
    x1= sympy.symbols('x1')
    x2= sympy.symbols('x2')
    f = sympy.sympify([f])
    H = sympy.zeros(len(vars),len(vars))
    for i ,fi in enumerate(f):
        for j,r in enumerate(vars):
            for k,s in enumerate(vars):
                H[j,k] = sympy.diff(sympy.diff(fi,r), s)
    H = H.subs({x1:x[0,0],x2:x[1,0]})
    return np.array(H,dtype='float')
def phi(alpha):
    gk = gradobjfun(x)
    H = Hessen(f,x)
    H_NI = np.linalg.inv(H)
    dk = -np.dot(H_NI,gk)
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
def Damped_Newton_method(f,x,epsilon):    
    k = 0
    while True:
        if np.linalg.norm(gradobjfun(x)) < epsilon:
            return np.hstack((x[0,0],x[1,0])),objfun(x),k
        gk = gradobjfun(x)
        alpha = GoldenSearch(x)
        H = Hessen(f,x)
        H_NI = np.linalg.inv(H)
        Dkn = -np.dot(H_NI,gk)
        x = x + alpha*Dkn
        k += 1

if __name__ == "__main__":
    epsilon = float(input("阀值："))
    f = '(3*x1-4)**2+(4*x2**2-2)**2'
    x = np.array([[3],[2]])
    x_min,f_min,k = Damped_Newton_method(f,x,epsilon)
    print("x_min:",x_min)
    print("f_min:",f_min)
    print("迭代数:",k)
