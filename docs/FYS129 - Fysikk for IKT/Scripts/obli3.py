# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:02:33 2020

@author: Paal
"""

from pylab import *

m = 0.093  # kg. massen til snus boksen
theta = 8.6 * pi / 180
r = 0.037  # m. radius til boksen
g = 9.81  # m/s^2
h = 0.15  # m. høgden
l = 1.0  # m. lengden
dt = 0.01
T = 1.21
r_1 = 0.02
r_2 = 0.04


Ep = m * g * h
n = int(round(T / dt))

y = zeros(n, float)
v = zeros(n, float)
z = zeros(n, float)
# theta = zeros(n, float)
omega = zeros(n, float)

y[0] = 0
v[0] = 0
z[0] = 0


for i in range(n):

    alpha = (g * sin(theta)) / (
        1 + (1 / 2 * (m * (r_1 ** 2 + m * r_2 ** 2)) / m * r ** 2)
    )
    omega[i] = omega[i - 1] + alpha * dt
    y[i] = y[i - 1] + omega[i] * dt
    z[i] = z[i - 1] + dt

print(alpha)
t, x = loadtxt("C:/Users/Paal/UiA/Fys129/oppgave3.txt", usecols=[0, 1], unpack=True)
figur = figure()
plot(z, y)
plot(t, x, "o")
grid()
xlabel("tid [s]")
ylabel("x [m]")
show()
figur.savefig("C:/Users/Paal/UiA/Fys129/Bilder/obli3", bbox_inches="tight")
