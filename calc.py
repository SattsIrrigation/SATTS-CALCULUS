from defi import calcular_ini
from defi import classificar_ini

import random
import matplotlib.pyplot as plt

umidade = random.randint(0, 100)
chuva = random.randint(0, 100)

ini = calcular_ini(umidade, chuva)
status = classificar_ini(ini)

print("=== SATTS IRRIGATION ===")
print(f"Umidade do Solo: {umidade}%")
print(f"Chance de Chuva: {chuva}%")
print(f"INI: {ini:.2f}")
print(f"Status: {status}")

chuva_fixa = 50

umidades = []
indices = []

for u in range(0, 101):
    umidades.append(u)
    indices.append(calcular_ini(u, chuva_fixa))

plt.figure(figsize=(8,5))
plt.plot(umidades, indices)

plt.title("Indice de Necessidade de Irrigacao")
plt.xlabel("Umidade do Solo (%)")
plt.ylabel("INI")

plt.grid(True)

plt.show()