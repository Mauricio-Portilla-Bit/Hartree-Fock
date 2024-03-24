import numpy as np
import Polarplots as p
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from statistic.pdf import pdf_generation
from polynomial.laguerre import *


#p.Polarplots(4,1)


n = 3
l = 2
r = np.linspace(0,10,200)
psi = -1*Radial_Function(n,l,r)
f = 100*psi**2
plt.plot(r, f*10)
#plt.plot(r/a,(a**(2.9))*psi**2)
#plt.xlim([0,18])
#plt.ylim([-0.3,0.8])
#plt.show()



Y = pdf_generation(r,f, 1, 10000)
print(Y)
plt.hist(Y)
plt.show()