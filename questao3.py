def calcula_soma(indice, k):
    soma = 0
    while k < indice:
        soma += k
        k += 1
    return soma

indice = 12
k = 1
resultado = calcula_soma(indice, k)
print(f"O resultado da soma foi {resultado}")
