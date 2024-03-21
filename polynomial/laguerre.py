import numpy as np 
import math 


# Laguerre Function (n) 
def Laguerre(n: int, x):
    
    # Series representation 
    l= 0
    for k in range(n + 1):
        l = l +  (math.comb(n, k)*((-x)**(k)) / math.factorial(k)) 

    return l


# Associated Functions (n, m) 
def Laguerre_Generalized(n: int, m: int, x):
    
    # Series representation 
    l= 0
    for k in range(n + 1):
        l = l +  (-1)**(k) * (math.comb(n + m, n - k)*((x)**(k)) / math.factorial(k)) 

    return l


# Radial Function (n, l)
def Radial_Function(n: int, l: int, r):
    
    if n - 1 < l:
        print("Error: n - 1 < l")
        return 0
    
    a = 0.529 * 10 ** (-10)
    Z = 1
    c = - np.sqrt(( (2*Z)/(n*a))**3 * (math.factorial(n - l - 1)/(2*n*(math.factorial(n + l))**3)))
    rho = 2*Z*r/(n*a)
    
    return c * np.multiply(np.multiply(np.exp(-rho/2), rho**(l)), Laguerre_Generalized(n + l, 2*l + 1, rho))


