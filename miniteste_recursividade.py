def superdigito(N):
  soma = N%10 + N//10
  if(soma) < 10:
    return soma
  return superdigito(soma)
print(superdigito(9875))