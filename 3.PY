import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=[10, 8])
Inicial=(1371,3266,1587,4350,2162)
Primaria=(3774,8623,3824,8675,6100)
Secundaria=(2975,8679,3651,8985,5725)
Especial=(990,1055,1800,2170,989)
X = np.arange(len(Inicial))
plt.bar(X, Inicial, color = 'black',edgecolor='black',linewidth=2, width = 0.2)
plt.bar(X + 0.2, Primaria, color = 'g',edgecolor='black',linewidth=2, width = 0.2)
plt.bar(X + 0.4, Secundaria, color = 'b',edgecolor='black',linewidth=2, width = 0.2)
plt.bar(X + 0.6, Especial, color='r',edgecolor='black',linewidth=2, width=0.2)
plt.legend(['inicial', 'primaria', 'secundaria','Especial'])
plt.xticks([i + 0.25 for i in range(5)], ['Amazonas', 'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho'])
plt.title("Profesores por regiones")
plt.xlabel('Regiones')
plt.ylabel('Profesores')
plt.savefig('proyecto3.png')
plt.show()





