# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:36:26 2020

@author: Paal
"""


from pylab import *

k = 10000.0  # N/m. fjærkonstant
m = 930.0  # kg. masse på bilen
g = -9.81  # m/s^2
dL = -6.0  # m. lengda på fjæra
rl = 5.0  # m. radius på loopen
vr = 30.0  # grader. vinkelen på rampen
lr = 15.0  # m. lengeden på rampen
vd = 25.0  # grader. vinkel på dosert sving
rd = 100.0  # m. radius på dosert sving
hr = sin(math.radians(vr)) * lr  # m. høgden på rampen

time = 6.0  # s
dt = 0.1  # tidssteg
n = int(round(time / dt))

Ek = zeros((n, 1), float)
Ek1 = zeros((n, 2), float)
Ep = zeros((n, 1), float)
x = zeros((n, 1), float)
vh1 = zeros((30, 2), float)
vh2 = zeros((30, 2), float)
vh3 = zeros((30, 2), float)
vh4 = zeros((30, 2), float)
vh5 = zeros((30, 2), float)
v = zeros((n, 1), float)
t = zeros((n, 1), float)
a = zeros((n, 1), float)
F = zeros((n, 1), float)
r1 = zeros((30, 2), float)
r2 = zeros((30, 2), float)
r3 = zeros((30, 2), float)
r4 = zeros((30, 2), float)
r5 = zeros((30, 2), float)

x[0] = 0
v[0] = 0
a[0] = 0
F[0] = 0


# formel for å rekne kva vinkel den doserte svingen må ha
def vinkelsving(v):
    alpha = math.degrees(
        math.atan((v) ** 2 / (rd * (-g)))
    )  # for å finne kva vinkel som må
    # til for å klare svingen
    return alpha


# detter er ikkje hooks lov. for lat til å endre det
# formelen for potensiel energi
def hooksL(x):
    E = 1 / 2 * k * x ** 2
    return E


# formelen for kinetisk energi
def kinetiskE(v):
    K = 1 / 2 * m * v ** 2
    return K


# newtons 2. lov plus hooks lov: -xk = ma
def fartE(x):
    v = sqrt((k / m) * x ** 2)
    return v


# formelen for potensiel energi
def potensielE(h):
    P = g * m * h
    return P


# loop for å kunne plote forholdet mellom potensiel og kinetisk energi ved start
def spring(dL, Ek):
    Etot = hooksL(dL)
    V = fartE(dL)  # farten i det den forlatter fjæra

    # lager ein loop for å rekne energi, fart og akselerasjon per metersteg
    for i in range(n):
        Ep[i] = hooksL(dL)  # energien før ein slepper fjæra
        Ek[i] = Etot - Ep[i]
        a[i] = -k / m * dL
        v[i] = sqrt(2 * Ek[i - 1] / m)
        dL = dL + dt
        t[i] = t[i - 1] + dt

    # plot for fart og akselerasjon kvar 0.1 meter steg
    figur = figure()
    subplot(2, 1, 1)
    plot(t, a)
    xlabel(" fjør distanse")
    ylabel("m/s^2")
    subplot(2, 1, 2)
    plot(t, v)
    xlabel("fjør distanse")
    ylabel("m/s")
    show()

    # plot for energi i fjæra i kvar 0.1 meter steg
    figur1 = figure()
    subplot(2, 1, 1)
    plot(t, Ep, "green")
    plot(t, Ek, "red")
    xlabel("fjør distanse")
    ylabel("energi")
    figur1.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/Spring-energi.png", bbox_inches="tight"
    )
    figur.savefig("C:/Users/Paal/UiA/Fys129/Bilder/Spring.png", bbox_inches="tight")
    return V


def hoppet(V):

    hr1 = sin(math.radians(10)) * lr  # m. høgden på rampen
    hr2 = sin(math.radians(20)) * lr  # m. høgden på rampen
    hr3 = sin(math.radians(30)) * lr  # m. høgden på rampen
    hr4 = sin(math.radians(40)) * lr  # m. høgden på rampen
    hr5 = sin(math.radians(50)) * lr  # m. høgden på rampen

    Veh1 = sqrt(2 * g * hr1 + V ** 2)  # farten bilen har i det den forlatter hoppet
    Veh2 = sqrt(2 * g * hr2 + V ** 2)
    Veh3 = sqrt(2 * g * hr3 + V ** 2)
    Veh4 = sqrt(2 * g * hr4 + V ** 2)
    Veh5 = sqrt(2 * g * hr5 + V ** 2)

    r0x = 0  # m. Start posisjonene i x rettning
    r0y1 = hr1  # m. Start posisjonene i y rettning
    r0y2 = hr2
    r0y3 = hr3
    r0y4 = hr4
    r0y5 = hr5

    v0x1 = Veh1 * cos(math.radians(10))  # m/s. for å rekne farten bilen har i x retning
    v0y1 = Veh1 * sin(math.radians(10))  # m/s. for å rekne farten bilen har i y retning
    v0x2 = Veh2 * cos(math.radians(20))
    v0y2 = Veh2 * sin(math.radians(20))
    v0x3 = Veh3 * cos(math.radians(30))
    v0y3 = Veh3 * sin(math.radians(30))
    v0x4 = Veh4 * cos(math.radians(40))
    v0y4 = Veh4 * sin(math.radians(40))
    v0x5 = Veh5 * cos(math.radians(50))
    v0y5 = Veh5 * sin(math.radians(50))

    t1 = zeros(30, float)
    # intitalverdier
    r01 = array([r0x, r0y1])
    v01 = array([v0x1, v0y1])
    r02 = array([r0x, r0y2])
    v02 = array([v0x2, v0y2])
    r03 = array([r0x, r0y3])
    v03 = array([v0x3, v0y3])
    r04 = array([r0x, r0y4])
    v04 = array([v0x4, v0y4])
    r05 = array([r0x, r0y5])
    v05 = array([v0x5, v0y5])

    vh1[0, :] = v01
    r1[0, :] = r01
    vh2[0, :] = v02
    r2[0, :] = r02
    vh3[0, :] = v03
    r3[0, :] = r03
    vh4[0, :] = v04
    r4[0, :] = r04
    vh5[0, :] = v05
    r5[0, :] = r05

    for i in range(29):
        a = g * array([0, 1])
        vh1[i + 1, :] = vh1[i, :] + a * dt
        r1[i + 1, :] = r1[i, :] + vh1[i + 1, :] * dt
        vh2[i + 1, :] = vh2[i, :] + a * dt
        r2[i + 1, :] = r2[i, :] + vh2[i + 1, :] * dt
        vh3[i + 1, :] = vh3[i, :] + a * dt
        r3[i + 1, :] = r3[i, :] + vh3[i + 1, :] * dt
        vh4[i + 1, :] = vh4[i, :] + a * dt
        r4[i + 1, :] = r4[i, :] + vh4[i + 1, :] * dt
        vh5[i + 1, :] = vh5[i, :] + a * dt
        r5[i + 1, :] = r5[i, :] + vh5[i + 1, :] * dt
        t1[i + 1] = t[i] + dt

    # finner total energi i systemet og bruker det til å rekne ut potensiel
    Etot = hooksL(dL)
    Ek1 = kinetiskE(vh3)
    Ekr = Ek1.sum(axis=1)  # for å lage eit plot for kinetisk energi over tid
    Ep = Etot - Ekr

    # plot for lenge og høgde i hoppet
    figur1 = figure()
    grid()
    plot(r1[:, 0], r1[:, 1], "green")
    plot(r2[:, 0], r2[:, 1], "blue")
    plot(r3[:, 0], r3[:, 1], "red")
    plot(r4[:, 0], r4[:, 1], "yellow")
    plot(r5[:, 0], r5[:, 1], "purple")
    xlabel("x [m]")
    ylabel("y [m]")
    show()

    # plot for energi i hoppet
    figur2 = figure()
    plot(t1, Ep)
    plot(t1, Ekr)
    ylabel("Energi")
    xlabel("Time")
    show()

    figur1.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/Hopp-lenge.png", bbox_inches="tight"
    )
    figur2.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/Hopp-energi.png", bbox_inches="tight"
    )


def loopen():

    # minimums gjennomsnitts fart bilen må ha for å klare loopen
    v = sqrt(5 * (-g) * rl)

    # for å finne høgden i loopen
    grader = range(0, 359)

    # nye arrayes så kan lagre 360 verdier
    Ep2 = zeros(360, float)
    Ek2 = zeros(360, float)
    deg = zeros(360, float)
    v2 = zeros(360, float)
    a2 = zeros(360, float)
    a_t = zeros(360, float)

    # total energi i systemet
    Etot = hooksL(dL)

    # veit at kinetisk = total energi rett før loopen
    Ep2[0] = 0
    Ek2[0] = Etot
    # loop for å rekne den potensiele energien og akselerasjonen kvar gradsteg
    for i in grader:
        Ep2[i + 1] = (rl - rl * cos(math.radians(i))) * -g * m
        Ek2[i + 1] = Etot - Ep2[i + 1]
        deg[i + 1] = i
        v2[i + 1] = sqrt((2 * Ek2[i + 1]) / m)
        # radiell akselerasjon
        a2[i] = v2[i + 1] ** 2 / rl
        # tangentiell akselerasjon
        a_t[i + 1] = g * sin(math.radians(i))

    # ploter energien i systemet i kvar einaste grad
    figur = figure()
    plot(deg, Ep2, "green")
    plot(deg, Ek2, "red")
    xlabel("grader")
    ylabel("Energi")
    show()

    # ploter akselerasjonen i systemet i kvar einaste grad
    figur2 = figure()
    plot(deg, a2)
    xlabel("grader")
    ylabel("m/s^2")
    show()

    figur3 = figure()
    plot(deg, a_t)
    xlabel("grader")
    ylabel("m/s^2")
    show()

    figur.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/loop-energi.png", bbox_inches="tight"
    )
    figur2.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/loop-akselerasjon.png", bbox_inches="tight"
    )
    figur3.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/loop-akselerasjon-t.png", bbox_inches="tight"
    )


def svingen(v):
    # veit at energien ikkje forandrer seg grunna at farten ikkje endrer seg.
    # Derfor er Ek = Etot
    # einaste krafta som påvirker bilen er sentrifugalkrafta som drar bilen,
    # inn mot sentrum av sirkelen

    Ek1 = zeros(180, float)
    Ep1 = zeros(180, float)
    v_s = zeros(180, float)
    a_r = zeros(180, float)

    Etot = hooksL(dL)
    Ek = kinetiskE(v)
    Ek1[0] = kinetiskE(v)
    Ep1[0] = Etot - Ek
    grader = range(0, 180)
    for i in grader:
        Ek1[i] = Etot
        Ep1[i] = Etot - Ek
        # rekner farten til bilen gjennom heile svingen
        v_s[i] = sqrt(2 * Ek1[i] / m)
        # rekner den radielle akselerasjonen gjennom heile svingen
        a_r[i] = v_s[i] ** 2 / rd

    figur = figure()
    plot(grader, Ek1, "red")
    plot(grader, Ep1, "blue")
    xlabel("grader")
    ylabel("Energi")
    show()

    figur1 = figure()
    plot(grader, a_r)
    xlabel("grader")
    ylabel("sentrifugal akselerasjon")
    show()

    figur.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/sving-energi.png", bbox_inches="tight"
    )
    figur1.savefig(
        "C:/Users/Paal/UiA/Fys129/Bilder/sving-akselerasjon.png", bbox_inches="tight"
    )


# for å kjøre funksjonene eg har laga
V = spring(dL, Ek)
hoppet(V)
svingen(V)
loopen()
