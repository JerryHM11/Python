def Value(x):
    y = x**2 + 2*x
    return y

# def BinarySearch(ak, bk,sita):
#     k = 0
#     epsilon = 1e-12
#     while True:
#         landa = (ak + bk)/2-epsilon
#         miu = (ak + bk)/2+epsilon
#         if Value(landa)>Value(miu):
#             if bk-ak>=sita:
#                 k += 1
#                 ak = landa
#             else:
#                 return landa,k
#         else:
#             if bk-ak>=sita:
#                 k += 1
#                 bk = miu
#             else:
#                 return miu,k
#     ck = (ak+bk)/2
#     return ck, k

def BinarySearch(ak, bk,sita):
    k = 0
    epsilon = 1e-12
    while bk-ak>=sita:
        landa = (ak + bk)/2-epsilon
        miu = (ak + bk)/2+epsilon
        if Value(landa)>Value(miu):
            k += 1
            ak = landa
        else:
            k += 1
            bk = miu
    ck = (ak+bk)/2
    return ck, k

if __name__ == "__main__":
    ak = int(input("最小值："))
    bk = int(input("最大值："))
    sita = float(input("精度："))
    ck, k = BinarySearch(ak, bk, sita)
    print(ck, k)