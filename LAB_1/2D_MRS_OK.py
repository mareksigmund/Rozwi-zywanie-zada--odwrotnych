import numpy as np
import matplotlib.pyplot as plt

# Parametry siatki
nx, ny = 50, 50  # Liczba węzłów w x i y
Lx, Ly = 1.0, 1.0  # Wymiary obszaru w x i y
dx, dy = Lx / (nx - 1), Ly / (ny - 1)  # Odległość między węzłami

# Inicjalizacja siatki
temperature = np.zeros((ny, nx))

# Warunki brzegowe
temperature[0, :] = 0  # Górny brzeg
temperature[-1, :] = 100  # Dolny brzeg
temperature[:, 0] = 75  # Lewy brzeg
temperature[:, -1] = 50  # Prawy brzeg

# Iteracja do osiągnięcia stanu stacjonarnego
for iteration in range(10000):
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            temperature[j, i] = (temperature[j+1, i] + temperature[j-1, i] + temperature[j, i+1] + temperature[j, i-1]) / 4.0

# Rysowanie rozkładu temperatury - mapa ciepła
plt.figure(figsize=(10, 8))
plt.imshow(temperature, cmap='hot', interpolation='nearest', origin='lower')
plt.colorbar(label='Temperatura')
plt.title('Mapa ciepła rozkładu temperatury')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Rysowanie rozkładu temperatury - kontury
plt.figure(figsize=(10, 8))
plt.contourf(np.linspace(0, Lx, nx), np.linspace(0, Ly, ny), temperature, 20, cmap='hot')
plt.colorbar(label='Temperatura')
plt.title('Konturowy rozkład temperatury')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
