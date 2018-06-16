# -*- coding: utf-8 -*-
#teste01.py
from colore_main import *
#Teste 1
menu_cores()
regiao1 = [[1,0,0,2,2], [0,2,2,1,2],[2,1,1,1,2], [2,1,2,1,2],[2,2,1,2,2] ]
print("região: \n")
for linha in regiao1:
	print(linha)

ponto1 = [2,2]
nova_cor1= 2
print("\nponto:" , ponto1, "\nNova Cor: ", nova_cor1)

if avalia_cor(nova_cor1):
  resultado_esperado1 = [[1,0,0,2,2], [0,2,2,2,2],[2,2,2,2,2], [2,2,2,2,2],[2,2,1,2,2] ]
  print("\nResultado Esperado: \n")
  for linha in resultado_esperado1:
    print(linha)
  resultado1 = colorir_regiao(regiao1,ponto1,nova_cor1)
  print("\nResultado Final: ", resultado1 == resultado_esperado1)#deve ser True
  for linha in resultado1:
    print(linha)
else: print("\nCor Inválida!")