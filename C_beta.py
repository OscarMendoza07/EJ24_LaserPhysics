import numpy as np
import matplotlib.pyplot as plt

# Definir la fórmula del coeficiente de atenuación
def beta(w, epsilon, mu, sigma):
    part1 = np.sqrt(w**2 * epsilon * mu / 2)
    part2 = np.sqrt(np.sqrt(1 + (sigma / (w * epsilon))**2) + 1)
    return part1 * part2

# Parámetros
w_values = np.linspace(1e8, 1e11, 1000)  # Frecuencia angular en radianes por segundo
#w_values = np.linspace(6.3e15, 2.7e15, 10000)  # Frecuencia angular en radianes por segundo
epsilon_value = 8.85e-12  # Permitividad en F/m
mu_value = 4 * np.pi * 1e-7  # Permeabilidad en H/m
sigma_value = 1e6  # Conductividad en S/m

# Calcular el coeficiente de atenuación para diferentes frecuencias angulares
beta_values = beta(w_values, epsilon_value, mu_value, sigma_value)

# Graficar
plt.plot(w_values, beta_values)
plt.xlabel('Frecuencia Angular (rad/s)')
plt.ylabel('Coeficiente de Atenuación β')
plt.title('Coeficiente de Propagación en función de la Frecuencia Angular')
plt.show()
