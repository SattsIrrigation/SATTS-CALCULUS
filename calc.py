from defi import calcular_umidade_exponencial, classificar_status
import matplotlib.pyplot as plt


umidade_inicial = 90.0
taxa_evaporacao = 0.15
limite_critico = 30.0  

tempos = list(range(0, 25))
umidades = []

for t in tempos:
    umidade = calcular_umidade_exponencial(umidade_inicial, taxa_evaporacao, t)
    umidades.append(umidade)

print("=== SATTS IRRIGATION: MODELO EXPONENCIAL ===")
for t in [0, 6, 12, 18, 24]:
    status = classificar_status(umidades[t], limite_critico)
    print(f"Hora {t}h | Umidade: {umidades[t]:.2f}% | Status: {status}")

plt.figure(figsize=(10, 6))
plt.plot(tempos, umidades, label='Curva de Secagem do Solo (Exponencial)', color='blue', linewidth=2)

plt.axhline(y=limite_critico, color='red', linestyle='--', label='Limite Crítico (Irrigação Necessária)')

plt.title("Modelo Matemático de Evaporação do Solo - SATTS")
plt.xlabel("Tempo (Horas)")
plt.ylabel("Umidade do Solo (%)")
plt.legend()
plt.grid(True)
plt.show()