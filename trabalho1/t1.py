def achaTrechoMaisAgradavel(numTotalTrechos, agradabTrechos):

    inicio = -1
    fim = -1
    k = 0
  
    somaAtual = 0
    somaMaximaAtual = 0

    for i in range(0,numTotalTrechos): 
  
        somaAtual += agradabTrechos[i] 
  
        if somaMaximaAtual < somaAtual:
            inicio = k 
            fim = i  
            somaMaximaAtual = somaAtual 
  
        if somaAtual < 0:
            k = i+1 
            somaAtual = 0    

    return inicio + 1, fim + 1


def main():
    
    numTotalParadas = int(input())
    agradabTrechos = list(map(int, input().split()))

    indParadaInicial, indParadaFinal = achaTrechoMaisAgradavel(numTotalParadas - 1, agradabTrechos)

    print(f"{indParadaInicial} {indParadaFinal}")


main()