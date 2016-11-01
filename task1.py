import math
import scipy.integrate as spint 
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
R=((3*A*B*C)/(4*math.pi))**(3/2)
V=A*B*C
RO=1000
G=9.8

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
def f_a(c):
    return RO*G*c*B
    
    
def f_b(с):
    return RO*G*A*с


def calc_pressure_cub_a_side(c):
    return spint.quad(f_a,0,c)
    
    
def calc_pressure_cub_b_side(c):
    return spint.quad(f_b,0,c)
    
    
def calc_pressure_cub_bottom(a,b,c):
    return RO*G*a*b*c
#-------------------- 4 CUBE /\

#-------------------- 4 SPHERE \/
get_rad=(lambda h: math.pi*(2*h*R-h*h)**0.5) 

def calc_pressure_sphere_sides(R):
    return spint.quad(get_rad,0,2*R)


def calc_pressure_sphere_bottom(R):
    return RO*G*R
    

get_h=(lambda a,b,n: (b-a)/n)

#-------------------- 4 SPHERE /\    
print ('bottom:',calc_pressure_cub_bottom(A,B,C)) 
print ('a-side:',calc_pressure_cub_a_side(C))  
print ('b-side',calc_pressure_cub_b_side(C))   
print (calc_pressure_sphere_sides(R))

    
