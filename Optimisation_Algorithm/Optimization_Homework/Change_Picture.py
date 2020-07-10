from matplotlib import pyplot as plt
import Fibonacci
import Golden
import Binary

ak = int(input("最小值："))
bk = int(input("最大值："))

L = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
B = [];B_Value = []
G = [];G_Value = []
F = [];F_Value = []

for i in L:
    b_value, b = Binary.BinarySearch(ak, bk,i)
    g_value, g = Golden.GoldenSearch(ak, bk, i)
    f_value, f = Fibonacci.FibonacciSearch(ak, bk, i)
    
    B.append(b)
    B_Value.append(b_value)
    G.append(g)
    G_Value.append(g_value)
    F.append(f)
    F_Value.append(f_value)

plt.figure(figsize=(12,8),dpi=80)
plt.figure(1)
ax1 = plt.subplot(321)
plt.plot(L, B, "or")#color='#FF0000'
ax2 = plt.subplot(322)
plt.plot(L, B_Value, "oy")
ax3 = plt.subplot(323)
plt.plot(L, G, "^b")
ax4 = plt.subplot(324)
plt.plot(L, G_Value, "^c")
ax5 = plt.subplot(325)
plt.plot(L, F, "sk")
ax6 = plt.subplot(326)
plt.plot(L, F_Value, "sm")
plt.show()

print(B)
print(B_Value)
print(G)
print(G_Value)
print(F)
print(F_Value)