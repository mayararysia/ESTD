"""
06.
Escreva um método show() para escrever toda a lista. Exemplo: lista = ListaOrdenada();
lista.append(3); lista.append(2); lista.show() imprime: [2,3]

"""
#Implementação da Classe Noh
class Noh:
  def __init__(self,valor_inicial):
    self._dados = valor_inicial
    self._proximo = None

  def getData(self):
    return self._dados

  def getNext(self):
    return self._proximo

  def setData(self, novo_valor):
    self._dados = novo_valor

  def setNext(self, novo_proximo):
    self._proximo = novo_proximo
#Lista não ordenada:
class ListaOrdenada:
  def __init__(self): #construtor
    self.head = None
    self.final = None
  
  def isEmpty(self): #<<<<
    return self.head == None

  def append(self, item):
    temp = Noh(item)
    if self.head == None:
      temp.setNext(self.head)
      self.head = temp
    if self.final == None: 
      self.final = self.head
    else:
      self.final.setNext(temp)
      self.final = temp

  def add(self,item):
    atual = self.head
    anterior = None
    parar = False
    while atual != None and not parar:
      if atual.getData() > item:
        parar = True
      else:
        anterior = atual
        atual = atual.getNext()
    temp = Noh(item)
    if anterior == None:
      temp.setNext(self.head)
      self.head = temp
    else:
      temp.setNext(atual)
      anterior.setNext(temp)

  def size(self):
    atual = self.head
    contador = 0
    while atual != None:
      contador = contador + 1
      atual = atual.getNext()
    return contador

  def remove(self, item):
    atual = self.head
    anterior = None
    encontrou = False
    while not encontrou: #percorre a lista
      if atual.getData() == item:
        encontrou = True
      else:
        anterior = atual
        atual = atual.getNext()
    if anterior == None:
      self.head = atual.getNext()
    else:
      anterior.setNext(atual.getNext())

  def search(self,item):
    atual = self.head #atual == temp
    encontrou = False
    parar = False
    while atual != None and not encontrou and not parar:
      if atual.getData() == item:
        encontrou = True
      else:
        if atual.getData() > item:
          parar = True
        else:
          atual = atual.getNext()
    return encontrou
  
  def show(self): #show
    if self.isEmpty():
      print("Lista Vazia!")
    else:
      lista = []
      aux = self.head
      while aux.getData()!= None:
        lista.append(aux.getData())
        if aux.getNext() == None: break
        aux = aux.getNext()
      tam = len(lista)
      j=1
      for i in range(tam-1):
        if j == (tam-1): break
        if lista[i]>lista[j]:
          aux = lista[i]
          lista[i] = lista[j]
          lista[j] = aux
          j = j+1
      return lista

if __name__ == '__main__':
  minha_lista = ListaOrdenada() #exemplo de uso
  print(minha_lista.isEmpty())

  minha_lista.append(8)
  minha_lista.append(2)
  minha_lista.append(9)
  print(minha_lista.isEmpty())
  print("Size: ", minha_lista.size())
  print(minha_lista.show())

