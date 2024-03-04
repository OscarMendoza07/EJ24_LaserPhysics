import numpy as np
import matplotlib.pyplot as plt

def indice_refraccion_real(omega, omega_p, omega_0, gamma):
    return 1 + (omega_p**2) / (omega_0**2 - omega**2 - 1j * gamma * omega)

def indice_refraccion_imaginario(omega, omega_p, omega_0, gamma):
    return (gamma * omega_p**2) / ((omega_0**2 - omega**2)**2 + (gamma * omega)**2)

# Definir parámetros
omega_p = 1.0  # Frecuencia de plasma
omega_0 = 2.0  # Frecuencia resonante
gamma = 0.1    # Ancho de banda

# Crear un rango de frecuencias angulares
omega_range = np.linspace(0, 5, 1000)

# Calcular los índices de refracción real e imaginario
n_real = np.real(indice_refraccion_real(omega_range, omega_p, omega_0, gamma))
k_imag = indice_refraccion_imaginario(omega_range, omega_p, omega_0, gamma)

# Graficar la parte real del índice de refracción
plt.figure(figsize=(10, 5))
plt.plot(omega_range, n_real, label='Parte Real', color='blue')
plt.plot(omega_range, k_imag, label='Parte Imaginaria', color='red')
plt.xlabel('Frecuencia Angular')
plt.ylabel('Índice de Refracción Real e imaginario')
plt.title('Índice de Refracción Real e Imaginario para un Medio Dieléctrico')
plt.legend()
plt.show()
