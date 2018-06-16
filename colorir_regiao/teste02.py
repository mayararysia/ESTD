# -*- coding: utf-8 -*-
#teste02.py
from colore_main import *
#Teste 2
menu_cores()
regiao2 = [[1,1,1,2,2,1], [1,2,2,1,2,1],[1,1,1,1,2,1], [1,1,2,1,1,1],[1,2,1,2,2,1] ]
print("região2: \n")
for linha in regiao2:
  print(linha)
ponto2 = [0,0]
nova_cor2 = 0
print("\nponto:" , ponto2, "\nNova Cor: ", nova_cor2)
if avalia_cor(nova_cor2):
  resultado_esperado2 = [[0,0,0,2,2,0], [0,2,2,0,2,0],[0,0,0,0,2,0], [0,0,2,0,0,0],[0,2,0,2,2,0] ]
  print("\nResultado Esperado: \n")
  for linha in resultado_esperado2:
    print(linha)
  resultado2 = colorir_regiao(regiao2,ponto2,nova_cor2)
  print("\nResultado Final: ", resultado2 == resultado_esperado2)#deve ser True
else: print("\nCor Inválida!")