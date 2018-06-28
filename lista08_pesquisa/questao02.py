# -*- coding: utf-8 -*-
#Lista de Exercícios 08 (Pesquisa) - Questão 02
#Mayara Rysia
from time import time
from time import sleep
from random import randint

"""
2. Use as duas funções de busca binária apresentadas (iterativa e recursiva). Gere
uma lista de números aleatórios, ordene-os e verifique o desempenho delas. Qual
os resultados?
"""

#Busca Binária - código recursivo
def busca_binaria(uma_lista, item_procurado):
  if len(uma_lista) == 0:
    return False
  meio = len(uma_lista)//2
  if uma_lista[meio] == item_procurado:
    return True
  if item_procurado < uma_lista[meio]:
	return busca_binaria(uma_lista[:meio], item_procurado)
  else:
    return busca_binaria(uma_lista[meio+1:], item_procurado)

#Busca Binária - código iterativo
def busca_binaria_it(uma_lista, item_pesquisado):
  inicio = 0
  fim = len(uma_lista)-1
  encontrou = False

  while inicio<=fim and not encontrou:
    meio = (inicio + fim)//2
    if uma_lista[meio] == item_pesquisado:
      encontrou = True
    else:
      if item_pesquisado < uma_lista[meio]:
        fim = meio-1
      else:
        inicio = meio+1
  return encontrou

#ordena a lista
def ordena(lista):
  
  quant = tam = len(lista)
  continua = True

  while quant>=1 and continua:
    continua = False
    for i in range(tam):
      j=i+1
      
      if j != tam and lista[i] > lista[j]:
        continua = True
        ant = lista[i]
        lista[i] = lista[j]
        lista[j] = ant
      i=j    
    quant-=1

  return lista

#cria a lista
def criaLista():
  lista = []
  for i in range(9):
    num = randint(0, 42)
    lista.append(num)
  return lista

def Teste(lista, num):
  print('Procurando ', num,'na lista', lista)
  inicio = time()
  result = busca_binaria(lista, num)
  fim = time()
  tempo_gasto = fim-inicio
  print('resultado', result)

  return tempo_gasto

def Teste_it(lista, num):
  print('Procurando ', num,'na lista', lista)
  inicio = time()
  result = busca_binaria_it(lista, num)
  fim = time()
  tempo_gasto = fim-inicio
  print('resultado', result)

  return tempo_gasto

if __name__ == '__main__':

  l = criaLista()
  lista = ordena(l)
  qtd_br = qtd_bi = 0

  #Testes
  for i in range(5):

    num = randint(0, 42)

    print("<< Busca Recursiva >> \n")
    tempo_gasto_br = Teste(lista, num)
    print('\ttempo gasto: ', tempo_gasto_br)
    print('\n\n')

    sleep(2)

    print("<< Busca Iterativa >> \n")
    tempo_gasto_bi = Teste_it(lista, num)
    print('\ttempo gasto: ', tempo_gasto_bi)
    print('\n\n')

    if tempo_gasto_br < tempo_gasto_bi:
      qtd_br +=1
      print('\n-> Busca Recursiva levou o menor tempo\n')   
    else:
      qtd_bi +=1
      print('\n-> Busca Iterativa levou o menor tempo\n')
    
    print("------- ------- ------- ------- -------")

  print("\nCONCLUSÃO\n\n ")
  if qtd_br > qtd_bi:
    print("Busca Binária Recursiva teve o melhor desempenho!")
  else:
    print("Busca Binária Iterativa teve o melhor desempenho!")

  print("Quantidade Binária Recursiva: ", qtd_br)
  print("Quantidade Binária Iterativa: ", qtd_bi)












    
      

