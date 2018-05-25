#Fila Simples
class Fila:
  def __init__(self):
    self._dados = []
	
  def enqueue(self, e): #insere
    self._dados.append(e)
	
  def dequeue(self): #remove
    if not self.is_empty():
      result = self._dados[0]
      del self._dados[0]
      return result
    raise Exception('A Fila está vazia')

  def __len__(self): #retorna tamanho
    return len(self._dados)

  def is_empty(self): #vazia
    return self.__len__() == 0
  
  def first(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    return self._dados[0]
  
  def get(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    return self._dados
	
if __name__ == '__main__':  
  #Teste
  f = Fila()
  print(f.is_empty())
  f.enqueue(8)
  f.enqueue(10)
  f.enqueue(60)
  print("---")
  print("First: ", f.first())
  print("Fila: ", f.get())
  print("tamanho: ", f.__len__())
  print("Dequeue: ", f.dequeue())
  print("---")
  print("First: ", f.first())
  print("tamanho: ", f.__len__())
  print("Fila: ", f.get())
  print("Dequeue: ", f.dequeue())
  print("---")
  print("First: ", f.first())
  print("tamanho: ", f.__len__())
  print("Fila: ", f.get())
  print("Dequeue: ", f.dequeue())
  print("---")
  try:    
    print("First: ", f.first())
    print("tamanho: ", f.__len__())
    print("Fila: ", f.get())
    print("Dequeue: ", f.dequeue())
  except Exception:
    print("Fila vazia!")
  print("---") 
  n=100
  for i in range(5):
    f.enqueue(n)
    n+=1  
  try:    
    print("First: ", f.first())
    print("tamanho: ", f.__len__())
    print("Fila: ", f.get())
    print("Dequeue: ", f.dequeue())
  except Exception: print("Fila vazia!")
