p=[0.1,5,10,15,20,25,30,35]
T=[275,300,325,350,375,400,425,450,500]
z=[24.2,26.7,30.2,34.4,38.3,42.4,46.7,50.9,
   26.2,28.4,31.4,34.9,38.5,42.0,45.6,49.3,
   28.0,30.1,32.6,35.6,38.8,41.9,44.8,48.1,
   30.0,31.8,34.1,36.7,39.5,42.3,45.1,47.8,
   31.9,33.6,35.6,38.1,40.5,43.1,45.6,48.0,
   33.8,35.4,37.3,39.4,41.8,44.1,46.4,48.6,
   35.5,37.0,38.8,40.7,42.9,45.1,47.2,49.2,
   37.3,38.7,40.3,42.0,44.0,46.2,48.0,49.9,
   40.7,42.0,43.3,44.9,46.5,48.3,50.1,51.8]


def interp(x1,x2,y1,y2,q11,q12,q21,q22,x,y):
    delim=(lambda x1,x2,y1,y2: (x2-x1)*(y2-y1))
    dlm=delim(x1,x2,y1,y2)
    return (q11*(x2-x)*(y2-y))/dlm+ \
           (q21*(x-x1)*(y2-y))/dlm+ \
           (q12*(x2-x)*(y-y1))/dlm+ \
           (q22*(x-x1)*(y-y1))/dlm


def in_out_interp(p,T,z):
    def left_right_nei(x,lst):
        tmp=lst[:]
        tmp.append(x)
        tmp.sort()
        return tmp[tmp.index(x)-1],tmp[tmp.index(x)+1]
   
    print("Enter X:")
    x=float(input())
    print("Enter Y:")
    y=float(input())
    x1,x2=left_right_nei(x,p)
    y1,y2=left_right_nei(y,T)
    q11=z[p.index(x1)+T.index(y1)*len(p)]
    q12=z[p.index(x1)+T.index(y2)*len(p)]
    q21=z[p.index(x2)+T.index(y1)*len(p)]
    q22=z[p.index(x2)+T.index(y2)*len(p)]
    #print (q11,q12,q21,q22)
    print (interp(x1,x2,y1,y2,q11,q12,q21,q22,x,y))
     
in_out_interp(p,T,z)           
#print (interp(30,35,275,300,46.7,45.6,50.9,49.3,32,280))