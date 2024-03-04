import numpy as np
import matplotlib.pyplot as plt

# Función que calcula el índice de refracción según la ecuación de Cauchy
def cauchy_equation(wavelength, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result += coefficients[i] / wavelength**(2*i)
    return result

# Parámetros
wavelengths = np.linspace(300, 2000, 1000)  # Longitudes de onda en nanómetros
coefficients = [1.5, 1e-4, 1e-8]  # Coeficientes de la ecuación de Cauchy

# Calcular el índice de refracción para cada longitud de onda
refraction_indices = cauchy_equation(wavelengths, coefficients)

# Graficar
plt.plot(wavelengths, refraction_indices)
plt.xlabel('Longitud de Onda (nm)')
plt.ylabel('Índice de Refracción')
plt.title('Ecuación de Cauchy')
plt.show()
