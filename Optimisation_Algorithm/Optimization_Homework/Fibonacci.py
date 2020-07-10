# import math

def Value(x):
    f = x**2+2*x
    return f

def Fibonacci(fn):
    f1 = 1;f2 = 1;f3 = 1;n = 2
    f = [1,1]
    while f3 <= fn:
        n += 1;f1 = f2;f2 = f3;f3 = f1 + f2
        f.append(f3)
    return f3, n, f

def FibonacciSearch(ak, bk, sita):
    fn = (bk-ak)/sita
    k = 1
    fnn, n, f= Fibonacci(fn)
    
    for i in range(2, n-1):
        landa = ak
        miu = bk
        miu = ak + (f[n-i]/f[n-i+1])*(bk-ak)
        landa = ak + (f[n-i-1]/f[n-i+1])*(bk-ak)
        if Value(landa)>Value(miu):
            ak = landa
#             landa = miu
            k+=1
        else:
            bk = miu
#             miu = landa
            k+=1
    ck = (ak + bk)/2
    return ck, n

if __name__ == "__main__":
    ak = int(input("最小值："))
    bk = int(input("最大值："))
    sita = float(input("精度："))
    
    ck, k = FibonacciSearch(ak, bk, sita)
    print(ck, k-2)