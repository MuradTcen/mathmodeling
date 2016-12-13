import math
import scipy.integrate as spint 
import numpy as np
from numpy import polynomial as pn 
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
A=0.3 
B=0.75
C=2
R=((3*A*B*C)/(4*math.pi))**(1/3)
V=A*B*C
RO=1000
G=9.8


def simpson_i(f,a,b,n):
    k=(b-a)/2
    return k * (sum(2 * f(a + x * k) if x % 2 == 0 else 4 * f(a + x*k) for x in range(1, n)) + f(a) + f(b)) / 3
    
    
    
def trapeze_i(f,a,b,n):
    k=(b-a)/2
    return ((f(a) + f(b)) / 2 + sum(f(x) for x in np.arange(a + k, b, k))) * k
    
    
def gausse_i(f,a,b,n):
    t_list, a_list = pn.legendre.leggauss(n)
    return sum(a_i * f((b + a) / 2 + t_i * (b - a) / 2) for a_i, t_i in zip(a_list, t_list)) * (b - a)/2
 
#-------------------- INTEGRALS \/
def integr_trap(a,b,n,f):
    total=0
    for i in range(1,n-1):
        total+=f
    #total=get_h(a,b,n)*(total+)
    return total

#-------------------- INTEGRALS /\
#print (integr_trap(0,1,10,math.sin()))

#-------------------- 4 CUBE \/
n=100
def f_a(c):
    return RO*G*c*B*c
    
    
def f_b(с):
    return RO*G*A*с*с


def calc_pressure_cub_a_side(c):
    return spint.quad(f_a,0,c)
    
    
def calc_pressure_cub_a_side_s_i(c):
    return simpson_i(f_a,0,c,n) 
    
    
def calc_pressure_cub_a_side_t_i(c):
    return trapeze_i(f_a,0,c,n) 


def calc_pressure_cub_a_side_g_i(c):
    return gausse_i(f_a,0,c,n) 
       
    
def calc_pressure_cub_b_side(c):
    return spint.quad(f_b,0,c)
    
    
def calc_pressure_cub_bottom(c):

    return RO*G*c
#-------------------- 4 CUBE /\

#-------------------- 4 SPHERE \/
get_rad=(lambda h: math.pi*(2*h*R-h*h)*RO*G)
get_df=(lambda x: math.pi*RO*G*((2*R*x-x*x)**0.5)*(2*R-x)*2)
 
 
def calc_pressure_sphere_sides(R):
    #return spint.quad(get_rad,0,2*R)
    return spint.quad(get_df,0,2*R)

def calc_pressure_sphere_bottom(R):
    return RO*G*R
    

get_h=(lambda a,b,n: (b-a)/n)

#-------------------- 4 SPHERE /\    
print ('bottom:',calc_pressure_cub_bottom(C)) 
print ('a-side:',calc_pressure_cub_a_side(C)) 
print ('a-side simpson :',calc_pressure_cub_a_side_s_i(C))  
print ('a-side trapeeze',calc_pressure_cub_a_side_t_i(C))  
print ('a-side gausse',calc_pressure_cub_a_side_g_i(C))  
print ('b-side',calc_pressure_cub_b_side(C))   
print ('sphere pressure',calc_pressure_sphere_sides(R))

    
