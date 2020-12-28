# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *

m = 80. # kg
F = 400. # N
p = 1.293 # kg/m^3
A0 = 0.45 # m^2
Cd = 1.2
T = 10. # s
dt = 0.01
fc = 488. # N
tc = 0.67 # s
a0 = 0. # m/s^2 # oppgave i
w = 0. # m/s^2 vindhastighet
v0 = 0. # m/s start hastighet
n =  int(ceil(T/dt))
x0 = 0. # m
#a = 5 # oppgave e
fv = 25.8 # sN/m


x = zeros((n, 1), float)
v = zeros((n, 1), float)
t = zeros((n, 1), float)
A = zeros((n, 1), float)
a = zeros((n, 1), float) # oppgave i
#oppgave k
Fcc = zeros((n, 1), float)
Fvv = zeros((n, 1), float)
Dd = zeros((n, 1), float)
Ff = zeros((n,1), float)
AT = zeros((n,1),float)


x[0] = x0
v[0] = v0
A[0] = A0
a[0] = a0
Ff[0] = F
AT[0] = A0


for i in range(n):
    A[i] = A0 * (1- 0.25*exp(-(t[i-1]/tc)**(2))) # oppgave i
    D = 1/2*(A[i-1]*p*Cd*(v[i-1] - w)**2) # oppgave i
    Fc = fc*exp(-(t[i-1]/tc)**(2)) # oppgave i
    
    Fv = -fv*v[i-1] # oppgave h
    
    Fnet = F + Fc + Fv - D # oppgave i
    
    #D = (1/2)*p*Cd*A0*(v[i-1]*v[i-1] - w*w) # oppgave d og f
    #a[i] = (F-D)/m # oppgave d
    
    a[i] = Fnet/m # oppgave i
    
    Fd = F + Fv # oppgave h
    #a[i] = Fd/m # oppgave h
    
    # Eulers metode for å finne fart(t), distanse(t)
    v[i] = v[i-1] + a[i-1]*dt # oppgave d og framover
    #v[i] = v[i-1] + a*dt
    x[i] = x[i-1] + v[i]*dt    
    t[i] = t[i-1] + dt
    
    # oppgave k
    Ff[i] = norm(F)
    Dd[i] = norm(D)
    Fvv[i] = norm(Fv)
    Fcc[i] = norm(Fc)
    

figur = figure()
subplot(3,1,1)
plot(t,x)
xlabel('t [sekund]')
ylabel('x [meter]')
subplot(3,1,2)
plot(t,v)
xlabel('t [sekund]')
ylabel('v [m/s]')
subplot(3,1,3) # oppgave i
plot(t,a) # oppgave i
xlabel(' t [s]') # oppgave i
ylabel('a [m/s^2]')# oppgave i
show()

# lage en graf for oppgave k
figur1 = figure() 
subplot(4,1,1)
plot(t,Ff)
xlabel('t [sekund]')
ylabel('F [N]')
subplot(4,1,2)
plot(t,Fcc)
xlabel('t [sekund]')
ylabel('Fc [N]')
subplot(4,1,3)
plot(t,Fvv)
xlabel('t [sekund]')
ylabel('Fv [N]')
subplot(4,1,4)
plot(t,Dd)
xlabel('t [sekund]')
ylabel('D [N]')
show()

#figur.savefig("C:/Users/Paal/UiA/Fys129/Bilder/oppgaveL1.png", bbox_inches='tight')
#figur1.savefig("C:/Users/Paal/UiA/Fys129/Bilder/oppgaveK.png", bbox_inches='tight')