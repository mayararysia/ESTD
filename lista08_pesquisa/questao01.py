# -*- coding: utf-8 -*-
#Lista de Exercícios 08 (Pesquisa) - Questão 01
#Mayara Rysia
from time import time
from time import sleep
from random import randint
"""
1. Realize um experimento com números aleatórios para testar a diferença entre
busca sequencial e busca binária em uma lista de inteiros.
"""
#binária
def busca_binaria(uma_lista, item_pesquisado):
  inicio = 0
  fim = len(uma_lista) - 1
  encontrou = False

  while inicio <= fim and not encontrou:
    meio = (inicio + fim)//2
    if uma_lista[meio] == item_pesquisado:
      encontrou = True
    else:
      if item_pesquisado < uma_lista[meio]:
        fim = meio-1
      else:
        inicio = meio+fim
  return encontrou

#busca sequencial
def busca_sequencial(uma_lista, item_pesquisado):
  pos = 0
  encontrou = False
  parar = False

  tamanho_lista = len(uma_lista)

  while pos < tamanho_lista and not encontrou and not parar:
    if uma_lista[pos] == item_pesquisado:
      encontrou = True
    else:
      if uma_lista[pos] > item_pesquisado:
        parar = True
       pos = pos+1
  return encontrou

#lista de inteiros:
lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
qtd_b = 0
qtd_s = 0 
for i in range(5):
  num = randint(0, 42)

  print("Número Aleatório: ", num)
  print("\n<<Busca Binária>>")

  inicio = time()
  result = busca_binaria(lista_teste, num)
  fim = time()
  tempo_gasto_b = fim-inicio

  print("\n\t ", result)
  print('\ttempo gasto: ', tempo_gasto_b)

  print("\n<<Busca Sequencial>>")

  inicio = time()
  result = busca_sequencial(lista_teste, num)
  fim = time()
  tempo_gasto_s = fim-inicio

  print("\n\t ", result)
  print('\ttempo gasto: ', tempo_gasto_s)
  

  if tempo_gasto_s < tempo_gasto_b:
    qtd_s +=1
    print('\n-> Busca Sequencial levou o menor tempo')   
  else:
    qtd_b +=1
    print('\n-> Busca Binária levou o menor tempo')
   
  print("--------------------------")
  sleep(2)

print("\nCONCLUSÃO: ")
if qtd_b > qtd_s:
  print("Busca Binária tem o melhor desempenho.")
else:
  print("A Busca Sequencial tem o melhor desempenho.")

print("Quantidade Binária: ", qtd_b)
print("Quantidade Sequencial: ", qtd_s)


