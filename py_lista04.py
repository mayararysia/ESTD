# -*- coding: utf-8 -*-
#Lista04 - Pilha - Respostas:
#Mayara Rysia

"""
1º

p.push(5) - p[5]
p.push(3) - p[5,3]
p.push(8) - p[5,3,8]
p.pop() - p[5,3]
p.pop() - p[5]
p.push(9) - p[5, 9]
p.push(1) - p[5, 9, 1]
p.pop() - p[5, 9]
p.push(7) - p[5,9,7]
p.push(6) - p[5,9,7,6]
p.pop() - p[5,9,7]
p.pop() - p[5,9]
p.push(4) - p[5,9,4]
p.pop() - p[5,9]
p.pop() - p[5]

"""

"""
2º

1- 25 valores na pilha
2- 12 vezes apontou para o topo da pilha
3- remove 10 elementos da pilha : restando 15 elementos
4- 15 elementos
"""
"""
3º
Desenvolva um método/função recursiva para remover todos os elementos de uma pilha.
"""

def push(p, e):
  return p.append(e)
  
print("--- 3º ---\n")
def apagar(p):
  print(p)
  if not p:
    return Exception('Todos Removidos!')
  p.pop()
  return apagar(p)

pilha = [5,4,3,2,1]
print(apagar(pilha))

"""
4º
Desenvolva uma função que inverte uma lista de elementos colocando-os todos em uma pilha, e colocando-os novamente
na lista de forma invertida.

Lista - FIFO
Pilha - LIFO
"""
print("\n--- 4º ---\n")
lista = [1,2,3,4,5]
def inverte(lista):
  pilha = []
  tam = len(lista)
  
  for i in range(tam):
    pilha.append(lista[i])
    
  del lista[0:tam]
  
  while(len(pilha) != 0):
    lista.append(pilha.pop())
 
  return lista
 
print(inverte(lista))
  
"""
6. Crie uma função que copia todos os elementos de pilha p para outra pilha q, de forma que os elementos mantenham a
mesma ordem, ou seja, o elemento no topo da pilha p permanecerá no topo da pilha q.
"""
print("\n--- 6º ---\n")
pilha = [5,4,3,2,1]
def copy(p):
  q = []
  tam = len(p)
  for value in p:
    push(q, value)
  
  return q
print("q: ", copy(pilha))
   
  
  
  
  
  
  
  
  
  
