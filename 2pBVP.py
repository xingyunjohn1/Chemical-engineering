# 2pBVP.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp
# scale
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# fontset
mpl.rcParams["font.family"] = ["serif"]
mpl.rcParams["font.serif"] = ["Times New Roman"]
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["font.size"] = 20  
mpl.rcParams["font.style"] = "normal" 
mpl.rcParams["font.weight"] = "normal" 
mpl.rcParams["mathtext.rm"] = "serif"
mpl.rcParams["mathtext.it"] = "serif:italic"
mpl.rcParams["mathtext.bf"] = "serif:bold"
mpl.rcParams["mathtext.fontset"] = "custom"
font1 = {'size': '62'}


# function to be solve
def dydx(x, y):
    dy0 = y[1]
    dy1 = 0.05*(1+x**2)*y[0]+2
    return np.vstack((dy0, dy1))


# boundary condictions
def boundCond(ya, yb):
    fa = 40  # y(xa=0) = 40
    fb = 80  # y(xb=10) = 80
    return np.array([ya[0]-fa, yb[0]-fb])


xa, xb = 0, 10  # bound(xa, xb)
# initialization
xini = np.linspace(xa, xb, 11)
yini = np.zeros((2, xini.size))

res = solve_bvp(dydx, boundCond, xini, yini)  # solve BVP
# points
xSol = np.linspace(xa, xb, 100)  # x
ySol = res.sol(xSol)[0]  # y
dySol = res.sol(xSol)[1]  # dy

plt.figure(figsize=(8, 6), dpi=80)
plt.text(2.3, 82, r'$\{$', fontdict=font1)
plt.text(3, 100, r'$y\prime\prime-0.05(1+x^2)y-2=0$')
plt.text(3, 80, r'$y(0)=40,y(10)=80$')
plt.plot(xSol, ySol, label='$y$', color="red", linewidth=2.0, linestyle="-")
plt.plot(xSol, dySol, label='d$y$', color="green",
         linewidth=2.0, linestyle="--")
plt.xlim(0, 10)
plt.ylim(-20, 180)
plt.legend()
plt.grid(True)
plt.xlabel("$x$")
plt.ylabel("$y,$d$y$")
plt.title("scipy.integrate.solve_bvp")
plt.savefig(".\\2pBVP.png", dpi=72)
plt.show()
