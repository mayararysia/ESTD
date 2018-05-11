#miniteste_OddWord.py
def laterais(texto):
  final=len(texto)-1
  ini = 0
  while texto[ini] == " ":
    ini += 1
  while texto[final] == " ":
    final -= 1
  strr = " "
  while ini <= final:
    strr += texto[ini]
    ini+=1
  return strr

def inverte(palavra):
  tam = len(palavra)
  invertida = " "
  tam-=1 
  while tam!=-1:
    invertida+=palavra[tam]
    tam-=1
  return invertida
    
def formato(texto):
  strr = laterais(texto); vet = []; string = " "; vet2 = []
  tam = len(strr)
  i=0
  aux = " "
  
  while(i<tam):
    j = i
    while i<tam and strr[i] != " ":
      aux +=strr[i]
      i+=1
    if j != i:
      vet.append(aux)
    else:  i+=1
    aux = " "

  aux2 = " "
  i = 0
  
  while(i < len(vet)):
    aux = vet[i]
    if(i+1)%2 == 0:
      aux2 = inverte(aux)
      aux = aux2
    vet2.append(aux)
    i+=1
    
  i=0
  while(i<len(vet2)):
    string+= vet2[i] + " "
    i+=1
  
  return string
  
def main():
  print(formato("odd word problem"))
main()