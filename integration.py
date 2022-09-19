import scipy.integrate as integrate
import scipy.special as special

def func(x,a,c):
    return(a*x**2+c)

a = 1
c = 2
result = integrate.quad(func, 0, 4.5, args=(a,c))
print(result)
