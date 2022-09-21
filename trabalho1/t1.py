def achaTrechoMaisAgradavel(n, x):
    if(n == 1):
        if(x[0] < 0):
            i = j = k = 0
            maxSeq = maxSuf = 0
        else:
            i = j = k = 1
            maxSeq = maxSuf = x[0]
    else:
        i, j, k, maxSeq, maxSuf = achaTrechoMaisAgradavel(n-1, x)

        if(k == 0):
            k = n
        maxSuf += x[n-1]

        if(maxSuf > maxSeq):
            i = k
            j = n
            maxSeq = maxSuf
        elif(maxSuf < 0):
            maxSeq = 0
            k = 0

    return i, j, k, maxSeq, maxSuf


def main():
    
    numTotalParadas = int(input())
    agradabTrechos = list(map(int, input().split()))

    print(numTotalParadas)
    print(agradabTrechos)

    indParadaInicial, indParadaFinal, indSufMax, maxSeq, maxSuf = achaTrechoMaisAgradavel(numTotalParadas - 1, agradabTrechos)

    print(f"{indParadaInicial} {indParadaFinal}")


main()