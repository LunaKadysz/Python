# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:58:06 2019

@author: Luna Kadysz
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def E(xp, yp, xf=0, yf=0, q=1):
    """Campo Eléctrico en 2 Dimensiones 
    en un punto de prueba xp, yp
    de una carga fuente en un punto xf, yf
    de valor q
    """    
    
    Dx = xp - xf
    Dy = yp - yf
    
    den = (Dx**2 + Dy**2)**1.5
    
    # Noten que la respuesta e sun vector (Ex, Ey).
    return q * Dx / den, q * Dy / den


def E2(xp, yp, a, q1, q2):
    """Campo Eléctrico en 2 Dimensiones 
    en un punto de prueba xp, yp
    de dos cargas separadas una distancia a sobre el eje y
    de valor q1 y q2
    """
    
    # Calculo el campo de cada carga ...
    E1x, E1y = E(xp, yp, 0, a/2, q1)
    E2x, E2y = E(xp, yp, 0, -a/2, q2)
    
    # y sumo porque vale superposicion.
    return E1x + E2x, E1y + E2y


rango = np.linspace(1, 10, 100)

# Campo a lo largo del Eje X para dos cargas iguales a una distancia 1
Ex, Ey = E2(rango, 0, a=1, q1=1, q2=1)

# Calculo también el campo para una carga de valor 2 en el origen
mon_Ex, mon_Ey = E(rango, 0, q=2)

plt.plot(rango, Ex, 'r', rango, mon_Ex, 'k');
plt.xlabel('x');
plt.ylabel('Ex');
plt.title('Campo sobre el eje x (y=0)');
plt.legend(['2 Cargas (q1=1, q2=1)', '1 Carga (q=2)']);

plt.plot(rango, Ey, 'r', rango, mon_Ey, 'k');
plt.xlabel('x');
plt.ylabel('Ey');
plt.title('Campo sobre el eje x (y=0)')
plt.legend(['2 Cargas (q1=1, q2=1)', '1 Carga (q=2)']);


# Ahora lo mismo sobre el eje y 
Ex, Ey = E2(0, rango, a=1, q1=1, q2=1)
mon_Ex, mon_Ey = E(0, rango, q=2)

plt.plot(rango, Ex, 'r', rango, mon_Ex, 'k');
plt.xlabel('y');
plt.ylabel('Ex');
plt.title('Campo sobre el eje y (x=0)');
plt.legend(['2 Cargas (q1=1, q2=1)', '1 Carga (q=2)']);

plt.plot(rango, Ey, 'r', rango, mon_Ey, 'k');
plt.xlabel('y');
plt.ylabel('Ey');
plt.title('Campo sobre el eje y (x=0)');
plt.legend(['2 Cargas (q1=1, q2=1)', '1 Carga (q=2)']);

# Generamos una grilla donde vamos a calcular el campo eléctrico
nx, ny = 64, 64
rangoX = np.linspace(-2, 2, nx)*1
rangoY = np.linspace(-2, 2, ny)*1
grillaX, grillaY = np.meshgrid(rangoX, rangoY)

# Y calculamos los campos
Ex, Ey = E2(grillaX, grillaY, a=1, q1=1, q2=1)

mon_Ex, mon_Ey = E(grillaX, grillaY, q=2)

fig = plt.figure(figsize=(17,17))
ax = fig.add_subplot(111)


color = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(grillaX, grillaY, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

ax.add_artist(Circle([0,0.5], 0.05, color='#aa0000'))
ax.add_artist(Circle([0,-0.5], 0.05, color='#aa0000'))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
ax.set_title('Dos cargas')
plt.show()


fig = plt.figure(figsize=(17,17))
ax = fig.add_subplot(111)


color = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(grillaX, grillaY, mon_Ex, mon_Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

ax.add_artist(Circle([0,0.0], 0.05, color='#aa0000'))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
ax.set_title('Una carga doble en el centro')
plt.show()




