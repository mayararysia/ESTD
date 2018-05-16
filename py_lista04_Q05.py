# -*- coding: utf-8 -*-
#Lista 04 - Mayara Rysia
"""
5º
Mofique a implementação PilhaArray para que a capacidade da pilha seja limitada a uma quantidade MAX de elementos,
onde MAX será um parâmetro opcional do construtor (init). Se push for chamado quando a pilha estiver cheia, uma
exceção deve ser lançada. Crie também a função is_full().
"""
class PilhaVazia(Exception):
  pass

class PilhaArray:

  def __init__(self, MAX):
    self.MAX = MAX
    self._pilha = []

  def __len__(self):
    return len(self._pilha)

  def size(self):
    return self.__len__()

  def is_empty(self):
    return len(self._pilha) == 0
  
  def is_full(self):
    return len(self._pilha) == self.MAX
    
  def push(self, e):
    if not self.is_full(): self._pilha.append(e)
    else: print(Exception('A pilha está Cheia'))

  def top(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha[-1]

  def pop(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha.pop()
    
  def get(self):
    return self._pilha

if __name__ == '__main__':
  p = PilhaArray(5)     # conteúdo [ ]
  p.push(5)            # conteúdo [5]
  p.push(3)            # conteúdo [5, 3]
  print(len(p))        # conteúdo [5, 3];    retorna 2
  print(p.pop())       # conteúdo [5];       retorna 3
  print(p.is_empty())  # conteúdo [5];       retorna False
  print(p.pop())       # conteúdo [ ];       retorna 5
  print(p.is_empty())  # conteúdo [ ];       retorna True
  p.push(7)            # conteúdo [7]
  p.push(9)            # conteúdo [7, 9]
  print(p.top())       # conteúdo [7, 9];    retorna 9
  p.push(4)            # conteúdo [7, 9, 4]
  print(p.size())      # conteúdo [7, 9, 4]; retorna 3
  print(p.pop())       # conteúdo [7, 9];    retorna 4
  p.push(6)            # conteúdo [7, 9, 6]
  p.push(8)            # conteúdo [7, 9, 6, 8]
  print(p.pop())       # conteúdo [7, 9, 6]; retorna 8
  #5ª
  p.push(100)
  p.push(200)
  p.push(300)
  p.push(400)
  print("PILHA: ", p.get())
