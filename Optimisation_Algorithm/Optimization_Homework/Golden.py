
def Value(x):
    f = x**2+2*x
    return f

def GoldenSearch(ak, bk, sita):
    k = 1
    landa = ak+0.382*(bk-ak)
    miu = ak+0.618*(bk-ak)

    while True:
        if Value(landa)>Value(miu):
            if bk-landa<=sita:
                return miu, k
            else:
                ak = landa
                landa = miu
                miu = ak+0.618*(bk-ak)
                k+=1
        else:
            if miu-ak<=sita:
                return landa, k
            else:
                bk = miu
                miu = landa
                landa = ak+0.382*(bk-ak)
                k+=1

if __name__ == "__main__":
    ak = int(input("最小值："))
    bk = int(input("最大值："))
    sita = float(input("精度："))
    
    ck, k = GoldenSearch(ak, bk, sita)
    print(ck, k)