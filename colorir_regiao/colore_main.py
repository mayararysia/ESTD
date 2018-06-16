# -*- coding: utf-8 -*-
#colore_main.py
#Mayara Rysia
from fila import *
"""
pontos
(x, y+1) - lado direito
(x, y-1) - lado esquerdo
(x+1, y) - abaixo
(x-1, y) - acima
"""
def menu_cores():
  print("\n--- CORES ---")
  print("0-Branco\n1-Cinza\n2-Preto\n3-Vermelho\n")

def avalia_cor(cor):
  return cor >=0 and cor<=3

def tam_matriz(regiao):
  return len(regiao)
    

def colorir_regiao(regiao1,ponto,nova_cor):
  f = Fila()
  f.enqueue(ponto)
  tam = tam_matriz(regiao1)
  
  p = f.get()[0]
  cor = regiao1[p[0]][p[1]]
  
  while not f.is_empty():
    p = f.dequeue()
    x = p[0]
    y = p[1]
    if y != tam-1 and regiao1[x][y+1] == cor:#x, y+1
      f.enqueue([x, y+1])

    if regiao1[x][y-1] == cor:#x, y-1
      f.enqueue([x, y-1])

    if x != tam-1 and regiao1[x+1][y] == cor:#x+1, y
      f.enqueue([x+1, y])

    if regiao1[x-1][y] == cor:#x-1, y
      f.enqueue([x-1, y])
          
    regiao1[x][y] = nova_cor 

  return [ [i for i in j] for j in regiao1]

if __name__ == '__main__':
  
  menu_cores()
  regiao = [[1,0,0,2,2], [0,2,2,1,2],[2,1,1,1,2], [2,1,2,1,2],[2,2,1,2,2] ]
  tam = tam_matriz(regiao)

  print("região: \n")
  for linha in regiao:
    print(linha)

  x = int(input("\nInsira o valor de x: "))
  y = int(input("\nInsira o valor de y: "))
  nova_cor = int(input("\nInsira um valor para a nova cor: "))

  if (x <= tam-1 and y<= tam-1) and avalia_cor(nova_cor):
    ponto = [x,y]
    print("\nponto:" , ponto, "\nNova Cor: ", nova_cor)    
    resultado = colorir_regiao(regiao, ponto, nova_cor)    
    print("\nResultado Final: ")
    for linha in resultado:
      print(linha)
  else:
    print("\nInválido! Tente Novamente!")