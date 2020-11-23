import math
import matplotlib.pyplot as plt
import numpy as np

def convertS(h):
    s = 3600*h
    return s

def kalkulateM(r,p):
    m = (4*math.pi/3)*p*r**3
    return m

def normal(x,mu,sigma):
    val1 = (1/(math.sqrt(2*math.pi*sigma**2)))
    val2 = (-(x-mu)**2)/(2*sigma**2)
    val3 = math.e**val2
    P = val1*val3
    return P

def acceleration(v,x,k,C):
    a = -k*x - C*v
    return a

if __name__ == '__main__':

    str = input("konverter, kalkuler, normal eller acceleration: ")

    if str == "konverter":
        h = float(input("skriv inn antall timene du vil skal bli konvertert:"))
        print(convertS(h))
    elif str == "kalkuler":
        r = float(input("gi meg ein radius(m): "))
        p = float(input("gi meg ein tetthet(kg/m^3): "))
        print(kalkulateM(r,p))
    elif str == "normal":
        muval = []
        sigmaval = []

        svar = input("gjer du b, c eller d?")

        if svar == "b":

            minx = int(input("gi meg ein minimums verdi: "))
            maxx = int(input("gi meg ein maximums verdi: "))
            mu = int(input("Gi meg ein mu verdi: "))
            sigma = int(input("Gi meg ein sigma verdi: "))
            for x in range(minx, maxx):
                print(normal(x, mu, sigma))

        elif svar == "c":
            minx = int(input("gi meg ein minimums verdi: "))
            maxx = int(input("gi meg ein maximums verdi: "))
            mu = int(input("Gi meg ein mu verdi: "))
            sigma1 = int(input("kor mange sigma verdier skal du ha? "))
            for i in range(sigma1):
                sigma = float(input("gi meg sigma verdiene dine: "))
                sigmaval.append(sigma)
            for x in range(minx, maxx):
                for z in sigmaval:
                    print(normal(x, mu, z))


        elif svar == "d":
            minx = int(input("gi meg ein minimums verdi: "))
            maxx = int(input("gi meg ein maximums verdi: "))
            sigma = float(input("gi meg ein sigma verdi: "))
            mu1 = int(input("kor mange mu verdier skal du ha?"))
            for i in range(mu1):
                mu = float(input("gi meg mu verdiene dine: "))
                muval.append(mu)
            for x in range(minx, maxx):
                for y in muval:
                    print(normal(x, y, sigma))

        else:
            exit()

    elif str == "acceleration":
        k = 10
        C = 5
        n = 100
        deltat = 0.01


        x = np.zeros(n, float)
        v = np.zeros(n, float)
        a = np.zeros(n, float)
        t = np.zeros(n, float)

        for i in range(n-1):
            a[i] = acceleration(v[i], x[i], k, C)
            v[i+1] = v[i] + a[i] * deltat
            x[i+1] = x[i] + v[i] * deltat
            t[i+1] = t[i] + deltat
        plt.subplot(3,1,1)
        plt.plot((t,a))
        plt.subplot(3,1,2)
        plt.plot((t,v))
        plt.subplot(3,1,3)
        plt.plot((t,x))
        plt.show()
    else:
        print("you are wrong")


