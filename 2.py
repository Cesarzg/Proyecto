import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=[10, 8])
inicial = [64, 164, 85, 139, 106]
primaria = [294, 504, 281, 336, 341]
secundaria = [66, 146, 103, 132, 94]
X = np.arange(len(primaria))
plt.bar(X, inicial, color = 'black', width = 0.25)
plt.bar(X + 0.25, primaria, color = 'g', width = 0.25)
plt.bar(X + 0.5, secundaria, color = 'b', width = 0.25)
plt.legend(["Inicial","Primaria","Secundaria"])
plt.xticks([i + 0.25 for i in range(5)], ['Amazonas', 'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho'])
plt.title("Instituciones por regiones")
plt.xlabel('Regiones')
plt.ylabel('Instituciones')
plt.savefig('proyecto.png')
plt.show()