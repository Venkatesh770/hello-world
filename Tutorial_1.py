# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 04:34:38 2020

@author: Venkatesh Moorthy
"""
import math        # basic mathematics
import numpy as np  
import matplotlib.pyplot as plt

N=100
m=6.631e-26
k=1.381e-23 
sigma = 0.341
epsilon = 125.7*k
x = [None] * N
y= [None]* N
v = [None] * N
abs_v = [None]*N


def init():
    f=open('config0')
    for i, line in enumerate(f):
        x[i] = [line.split()[0],line.split()[1],line.split()[2]]
        v[i] = [line.split()[3],line.split()[4],line.split()[5]] 
        
def Velocity():
    for i in range(0, N):
        abs_v[i]=[math.sqrt(float(v[i][0])*float(v[i][0])+float(v[i][1])*float(v[i][1])+float(v[i][2])*float(v[i][2]))]

def Temperature():
    ene_kin = 0.0
    for i in range(N):
        real_vel = abs_v[i]
        ene_kin = ene_kin + np.dot(real_vel,real_vel)
    
    ene_kin_aver = m*ene_kin
    temperature = (ene_kin_aver/(3*N-3))/k
    
    return temperature

def potential_energy():
    ene_pot=0.0
    for i in range(0,N):
        for j in range(i+1,N):
            dx=(float(x[i][0])-float(x[j][0]))
            dy=(float(x[i][1])-float(x[j][1]))
            dz=(float(x[i][2])-float(x[j][2]))
            r_sqr=dx*dx+dy*dy+dz*dz
            rr=sigma/r_sqr
            r_six=math.pow(rr,3)
            r_twel=math.pow(rr,6)
            ene_pot += 4 * epsilon * (r_twel - r_six)  
    return ene_pot        

init()
Velocity()
for i in range(0,N):
    y[i]=abs_v[i][0]
plt.hist(y, bins = 10)
plt.show()
t=Temperature()
print(t)
z=potential_energy()
print(z)





        
        








