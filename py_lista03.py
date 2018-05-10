# -*- coding: utf-8 -*-
from unicodedata import normalize
#Lista de Exercícios 03 - Recursividade
#Aluna: Mayara Rysia

def removeEspacosAMais(nome):
  tam = len(nome)
  i=0; final = tam-1
  nomeFormatado = ""
  while i <= final:
    if nome[i] != " ":
      nomeFormatado+=nome[i]
    i+=1
  return nomeFormatado
  
def removerCaracteresEspeciais(string):
  stri = removeEspacosAMais(string)
  return normalize('NFKD', stri).encode('ASCII', 'ignore').decode('ASCII').lower()
  
#questão 01
def fat(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * fat(n-1)
    
#questão 02
def inverte(palavra):
  if len(palavra) == 1:
    return palavra
  return inverte(palavra[1:]) + palavra[0]
  
#questão 03
def repetida(P, k, qtd, i):
  if P[i] == k: qtd += 1
  if i == 0: return qtd
  return repetida(P, k, qtd, i-1)
  
#questão 04
def crescente(N, n):
  i = n-N
  if N != 0: print(i)
  else: return print(i)
  return crescente(N-1, n)
    
#questão 05
def decrescente(N):
  if N == 0: return print(N)
  print(N)
  return decrescente(N-1)
  
#questão 06
def Fibonacci(num):
  if(num==1 or num==2):
    return 1
  else:
    return Fibonacci(num-1) + Fibonacci(num-2)
    
#questão 07
def fatDuplo(n):
  if n == 1 or n == 0:
    return 1
  if n%2!=0:
    return n * fatDuplo(n-1)
  return fatDuplo(n-1)
  
#questão 08
def palindroma(palavra, cont, tam, i):
  if palavra[i] == palavra[tam]: cont+=1
  if tam == 0:
    if cont == len(palavra):
      return "É Palíndroma!"
    return "Não é Palíndroma!"
  return palindroma(palavra, cont, tam-1, i+1)

#questão 09
def _MDC(a, b):
  if b == 0 : return a
  r = a % b
  a = b
  b = r
  return _MDC(a, b)

def main():
  #1
  num = int(input('Insira Um Número: '))
  print("Fatorial: ", fat(num))
  print("---")
  
  #02
  palavra = input('Insira Uma Palavra: ')
  print(P, "-->> ", inverte(palavra))
  
  #3
  k = input('Insira uma Letra: ')
  print("A letra ", k, "aparece ",repetida(palavra, k, 0, tam), "vezes em ", palavra)

  #4
  print("Número: ", num)
  print("Ordem Crescente: ")
  crescente(num, num)
  #5
  print("Ordem Decrescente: ")
  decrescente(num)
  print("---")
  
  #6
  print("Termo: ", 10)
  print("->> ", Fibonacci(10-1))
  print("---")

  #7
  print("Número: ", num)
  print("Fatorial Duplo: ", fatDuplo(num))
  print("---")

  #8
  string = input("Insira uma String: ")
  s = removerCaracteresEspeciais(string)
  print(palindroma(s, 0, len(s)-1, 0))
  
  #9
  print("\n---Cálculo do MDC---")
  a = int(input('Insira o Primeiro Número: '))
  b = int(input('Insira o Segundo Número: '))
  if (a >0 and b>0):
    print("MDC( ", a,", ", b, ") = ", _MDC(a, b))
  else: print("Insira Números Positivos!")

if __name__ == "__main__":
   main()
