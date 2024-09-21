def verifica_str(palavra_input):
    #como a letra pode ser maiscula ou minuscula, vamos pegar a string recebida e deixar todos seus caracteres recebidos em minusculo
    palavra_minuscula = palavra_input.lower()
    #registro do numero de vezes que a letra a, aparece na string
    numero_acontecimentos = palavra_minuscula.count("a")

    if numero_acontecimentos > 0:
        return f"A letra 'a' aparece na palavra digitada {numero_acontecimentos} vezes."
    else:
        return f"A letra 'a' nao tem nenhuma ocorrencia na palavra digitada."


palavra_digitada = str(input("Digite uma palavra para verificar o numero de ocorrencias da letra 'a' nela: "))
mensagem_resultado = verifica_str(palavra_digitada)

print(mensagem_resultado)