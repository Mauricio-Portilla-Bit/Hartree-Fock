import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from mpl_toolkits import mplot3d

def Pl(n):      #Coeficients of a legendre polynomial
    c = np.zeros([n+1,n+1])   
    c[0,0] = 1
    if n > 0:
        c[1,0] = 0
        c[1,1] = 1
    if n > 1:
        for i in range(1,n):
            cpre = np.insert(c[i,:],0,0)
            cpre = np.delete(cpre,-1)
            c[i+1,:] =  ((2*i +1)*cpre-i*c[i-1][:])/(i+1)
    return c[n,:]
#For every higher order polynomial lower order have to computed, carried out in this manner complexity bearly increases
#cpre is the equivalent of multiplying Pn+1 by x, just carried out in coeficient notation

def Polyval(c,x): #Evaluates a "Polynomial vector" in a given domain
    v = np.zeros(len(x))
    for i in range(len(c)):
        print(c[i])
        v = v + c[i] * x**(i)
    return v
#A little explanantion of what i mean with Polynomial vector : (function) f(x) = 1+x+x^2 -----> (asociated vector) [1,1,1]
#In this notation, derivatives, integrals,sums and multiplication by a a given power of x are computationally friendly
# I know, loops are not that optimal but to be fair, the value of c will rarely exceed 10
 
def legendrep(n,x):   #ELegendre polynomials in a domain c---> coefficient vector, x--->Domain
    c = Pl(n) 
    y = Polyval(c, x)
    return y
#Its just the evalutation using the other two functions

def FAL(l,m,x): #It returns the associated legendre functions evaluated in the specified domain
 if m > l:
     print("error")
     return 1
 y = ((-1)**m)*((1-x**2)**(m/2))*Polyval(Polydiff(Pl(l),m),x)
 return y

def Polydiff(c,m):   #It calculates the mth order derivative of a given polynomial vector
    print(len(c))
    for i in range(m):
        c = np.delete(c,0)
        print(type(c))
        t = len(c)
        c = c*(np.arange(t)+1)
    return c
#Again, i know, loops, but seriously, when in the world will you take something higher than a 5th order 
#dervative??



def SH(l,m,th,ph):  #It returns the spherical harmonics, evaluated in the corresponding domain
    Nf = (((2*l+1)/(4*np.pi))*(np.math.factorial(l-np.abs(m))/np.math.factorial(l + np.abs(m))))**0.5 #Normalization constant 
    Y = Nf*np.multiply(FAL(l,np.abs(m),np.cos(th)),np.exp(1j*m*ph)) #Actual calculation of the spherical harmonics
    return Y
#Important to note, theta is the angle with respect to the z axis ph is the azimuthal axis with respect to the x axis   

#This is a polar representation of the spherical harmonics, so far, so good
th = np.linspace(0,np.pi,100)
ph = np.linspace(0,np.pi*2,100)
[TH,PH] = np.meshgrid(th,ph)
X = np.multiply(np.cos(PH),np.sin(TH))
Y = np.multiply(np.sin(PH),np.sin(TH))
Z = np.cos(TH)
f = np.real(SH(2,2,TH,PH))
Xf = np.multiply(X,f)
Yf = np.multiply(Y,f)
Zf = np.multiply(Z,f)


#Create figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_surface(Xf, Yf, Zf)
 
# show plot
plt.show()






