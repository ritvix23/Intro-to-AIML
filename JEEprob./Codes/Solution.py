#Problem - Locus of centroid of the triangle whose vertices are (a cos t, a sin t), (b sin t, − b cos t) and (1, 0), where t is a parameter, is
# The code plots the required locus
import matplotlib.pyplot as plt
import numpy as np
import math
t = np.linspace(0,2*np.pi,100)
A = np.zeros((2,100))
B = np.zeros((2,100))
C = np.zeros((2,100))
G = np.zeros((2,100))
a,b=1,2 #We took a=1 and b=2 for our code


for i in range(100):
    A[0,i] = math.cos(t[i]) 
    B[0,i] = 2*math.sin(t[i]) 
    C[0,i] = 1
    A[1,i] = math.sin(t[i])
    B[1,i] = 2*-math.cos(t[i])
    C[1,i] = 0
def mid_pt(B,C):
    D = (B+C)/2
    return D

def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def line_intersect(AD,CF):
    n1 = norm_vec(AD)
    n2=norm_vec(CF)
    N=np.vstack((n1,n2))
    
    p=np.zeros(2)
    p[0] = np.matmul(n1,AD[:,0])
    p[1] = np.matmul(n2,CF[:,0])
    if np.linalg.det(N) !=0:
        return np.matmul(np.linalg.inv(N),p) 
    else:
        return (t1+t2+t3)/3 #To complete the locus we use direct formula of centroid but in reality no triangle is possible if det(N)=0
    
    

for i in range(100):
    t1 = np.array([A[0,i],A[1,i]])
    t2 = np.array([B[0,i],B[1,i]])
    t3 = np.array([1,0])



    D = mid_pt(t2,t3)
    F = mid_pt(t1,t2)
    E = mid_pt(t1,t3)

    AD = np.vstack((t1,D)).T
    CF = np.vstack((t3,F)).T
    BE = np.vstack((t2,E)).T
    dvec = np.array([-1,1])
    omat= np.array([[0,1],[-1,0]])
    res = line_intersect(AD,BE)
   
    G[0,i] = res[0]
    G[1,i] = res[1]
    

plt.xlim(-1,1.2)
plt.ylim(-1, 1.2)    
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(G[0,:],G[1,:],label='$locus$')
plt.savefig('plot.png')
    