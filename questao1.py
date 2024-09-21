def calcula_fibonacci(numero_input):
    #inicializa as listas com os primeiros termos
    lista_fibonacci = [0, 1, 1]

    #deve-se limitar minha sequencia ao numero digitado pelo usuario
    while lista_fibonacci[-1] <= numero_input:
        #se nao tiver ultrapassado o numero adiciona-se o proximo item a lista
        lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2])

    return lista_fibonacci

def verifica_pertencimento(numero_input, lista_pronta):
    #verifica se o numero digitado esta ou nao na sequencia de fibonacci criada
    if numero_input in lista_pronta:
        return f"O número {numero_input} pertence a sequência de Fibonacci"
    else:
        return f"O número {numero_input} não pertence à sequência de Fibonacci"

#cada vez que o usuario rodar o codigo a lista é resetada
lista_pronta = []
#input dado pelo usuario
numero_input = int(input("Digite um numero para chegar se ele pertence a lista de Fibonacci: "))
lista_pronta = calcula_fibonacci(numero_input)
mensagem_gerada = verifica_pertencimento(numero_input, lista_pronta)

#print final para resposta ao usuario
print(lista_pronta)
print(mensagem_gerada)


