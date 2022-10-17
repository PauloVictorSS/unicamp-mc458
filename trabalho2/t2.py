def merge(A, esquerda, meio, direita):

  totalTrocas = 0
  aux = [0] * len(A)
  for i in range(esquerda, direita + 1):
    aux[i] = A[i]

  i = esquerda
  j = meio + 1

  for k in range(esquerda, direita + 1):
    if(j > direita):
      A[k] = aux[i]
      i += 1
    else:
      if(i > meio):
        totalTrocas += j - k
        A[k] = aux[j]
        j += 1
      elif(aux[i] <= aux[j]):
        A[k] = aux[i]
        i += 1
      else:
        totalTrocas += j - k
        A[k] = aux[j]
        j += 1

  return totalTrocas


def mergesort(A, esquerda, direita, totalTrocas):
  if esquerda < direita:
    meio = (esquerda + direita) // 2

    totalTrocas1 = mergesort(A, esquerda, meio, totalTrocas)
    totalTrocas2 = mergesort(A, meio + 1, direita, totalTrocas)
    totalTrocas3 = merge(A, esquerda, meio, direita)

    totalTrocas += totalTrocas1 + totalTrocas2 + totalTrocas3
  
  return totalTrocas


def main():

  numTotalContainers = int(input())
  containers = list(map(int, input().split()))

  totalTrocas = mergesort(containers, 0, numTotalContainers - 1, 0)
  print(totalTrocas)


main()