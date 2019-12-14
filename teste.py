
import numpy as np
from scipy.interpolate import lagrange

# concludentes = [10, 15, 19, 19, 5, 9, 6, 6, 10, 1, 6, 4]
# evadidos = [12, 3, 13, 6, 7, 7, 14, 20, 8, 47, 19, 16]
# semestres = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

concludentes = [12,0,2,1,6,7,6,0,2,5,6,1,0,14,6,14,8,0,46,1,18,1,16,0]
evadidos = [7,3,11,4,13,6,7,12,3,2,3,6,2,4,3,3,9,1,1,0,3,3,4,0]
semestres = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

######################################################
#############     ALUNOS EVADIDOS   ##############
######################################################

x1 = np.array(semestres)
y1 = np.array(evadidos)

poli = np.polyfit(x1, y1, 11)

print("INTERPOLAÇÃO POLINOMIAL - EVADIDOS")
print(poli)

print("\nINTERPOLAÇÃO POLINOMIAL LAGRANGE - EVADIDOS")
lagrangePoli = lagrange(x1, y1)
print(lagrangePoli)




######################################################
#############     ALUNOS CONCLUDENTES   ##############
######################################################


print("\n#####################################################################\n")

x2 = np.array(semestres)
y2 = np.array(concludentes)

poli2 = np.polyfit(x2, y2, 11)

print("INTERPOLAÇÃO POLINOMIAL - CONCLUDENTES")
print(poli2)

print("\nINTERPOLAÇÃO POLINOMIAL LAGRANGE - CONCLUDENTES")
lagrangePoli2 = lagrange(x2, y2)
print(lagrangePoli2)

