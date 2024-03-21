import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def Pl(n):      #Regresa los coeficietnes del enesimo polinomio de legendre
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

def Polyval(c,x):    #Evalua los coeficietnes de un polinomio arbitrario en un vector 
    v = np.zeros(len(x))
    for i in range(len(c)):
        print(c[i])
        v = v + c[i] * x**(i)
    return v
def legendrep(n,x):
    c = Pl(n) 
    y = Polyval(c, x)
    return y


def FAL(l,m,x): #Funcion que regresa las funciones asociadas de legendre
 if m > l:
     print("error")
     return 1
 y = ((-1)**m)*((1-x**2)**(m/2))*Polyval(Polydiff(Pl(l),m),x)
 return y

def Polydiff(c,m):   #Funion que calcula la derivada de un vector de coeficientes polinomial de orden mésimo
    print(len(c))
    for i in range(m):
        c = np.delete(c,0)
        print(type(c))
        t = len(c)
        c = c*(np.arange(t)+1)
    return c

x = np.linspace(-1,1,100)
y = FAL(2,2,x)
plt.plot(x,y)
plt.show()


