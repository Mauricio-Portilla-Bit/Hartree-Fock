import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from polynomial import legendre as le

def Polarplots(l,m):
    #This is a polar representation of the spherical harmonics, so far, so good
    th = np.linspace(0,np.pi,512)
    ph = np.linspace(0,np.pi*2,512)
    [TH,PH] = np.meshgrid(th,ph)
    X = np.multiply(np.cos(PH),np.sin(TH))
    Y = np.multiply(np.sin(PH),np.sin(TH))
    Z = np.cos(TH)
    f = np.real(le.SH(l,m,TH,PH))
    Xf = np.multiply(X,f)
    Yf = np.multiply(Y,f)
    Zf = np.multiply(Z,f)
    #Create figure
    fig = plt.figure(figsize =(9, 9))
    ax = plt.axes(projection ='3d')
    # Creating plot
    ax.plot_surface(Xf, Yf, Zf)
    ax.set_aspect('equal', 'box')
    # show plot
    plt.show()
