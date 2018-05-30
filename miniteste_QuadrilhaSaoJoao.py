# -*- coding: utf-8 -*-
#Miniteste 03
#Mayara Rysia

class PilhaVazia(Exception):
  pass

class PilhaArray:

  def __init__(self):
    self._pilha = []

  def __len__(self):
    return len(self._pilha)

  def size(self):
    return self.__len__()

  def is_empty(self):
    return len(self._pilha) == 0
    
  def push(self, e):
    self._pilha.append(e)

  def top(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha[-1]

  def pop(self):
    if self.is_empty():
      #raise PilhaVazia('A pilha está vazia')
      return "sem par"
    return self._pilha.pop()
    
  def get(self):
    return self._pilha

def sexo_masc(s):
 return (s == 'M' or s =='m') or (s == 'Masc' or s == 'masc') or (s == 'masculino' or s == 'Masculino')

def sexo_fem(s):
  return (s == 'F' or s == 'f') or (s == 'Fem' or s ==  'fem') or (s == 'feminino' or s == 'Feminino')

if __name__ == '__main__':
  p_mulher = PilhaArray()
  p_homem = PilhaArray()
  
  N = int(input("Insira a quantidade de pessoas: "))

  for i in range(N):
    n = input("Insira o nome da pessoa: ")
    s = input("Insira o sexo da pessoa: ")
    if sexo_fem(s):
      p_mulher.push(n)
    elif sexo_masc(s):
      p_homem.push(n)
    else:
      print("\nInválido!") 
  if p_mulher.is_empty() == False or  p_homem.is_empty() == False:
    print("\nPares (Mulher - Homem): ")
    for i in range(N-1):
      print(" ", p_mulher.pop(), "- ", p_homem.pop())
  else: print("Sem Informações!")