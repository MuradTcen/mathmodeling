import math
import scipy.integrate as sprint 
'''
вариант 9
Вычислить силу давления воды на стенки прямоугольного
аквариума заданных размеров a*b*c и сферического аква-
риума радиуса R имеющего такой же объем как и прямо-
угольный.
http://festival.1september.ru/articles/649134/

'''
#A-A width
#B-B width
#C-height
A=0.1 
B=1
C=2
R=((3*A*B*C)/(4*math.pi))**(3/2)
V=A*B*C
RO=1000
G=9.8

'''
def sum(term, a, next, b):
    if(a>b):
        return 0
    else:
        return term(a)+sum(term, next(a), next, b)

def integral(f, a, b, dx):
    def addDx(x):
        return x+dx
    return sum(f, a+dx/2, addDx, b)*dx
'''

def f(a,b):
    return RO*G*a*b

def calc_pressure_cub_bottom(a,b,c):
    return c*RO*G*a*b


def calc_pressure_cub_a_side(a,c):

    a1 = 0
    a2 = c
    return spint.quad(f,a1,a2)


def calc_pressure_cub_b_side(c):
    return c*RO*G*A*B


def calc_pressure_sphere(R):
    #horizontal   
    #vertical
    return RO*G*R
    
#print (calc_pressure_cub_bottom(a,b,c)) 
print (calc_pressure_cub_a_side(f(A,C),C))  
print()
#print integral(calc_pressure_cub_a_side(A,C),0,C,0.01)    


    
