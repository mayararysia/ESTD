from lista_nao_ordenada import *

def test1_lista(l):
		
	print(l.isEmpty())  
	try:
		l.insert(0, 56) #posição 0, elemento: 56
	except Exception:
		print("Lista vazia!")
	l.append(2)
	l.append(3)
	l.append(4)
	l.append(30)
	l.append(41)
	print(l.isEmpty())
	print("\nLista: ")
	l.print_()
	print("Size: ", l.size())

def test2_lista(l):
	print("\nLista: ")
	try:
		l.insert(6, 100) #posição 3, elemento: 6
	except Exception:
		print("Erro!")
	l.print_()
	print("Size: ", l.size())
	try:
		l.pop()
	except Exception:
		print("Lista Vazia!")
	print("\nLista: ")
	l.print_()

if __name__ == '__main__':

	l = ListaEncadeada()
	test1_lista(l)
	test2_lista(l)

