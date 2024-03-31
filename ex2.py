#Função que verifica se um numero faz parte da sequancia de Fibonacci
numero = int(input("Digite o número a ser verificado:"))

def fibonacci():
    antecessor = 0
    sucessor = 1

    while (sucessor < numero):
        soma = sucessor
        sucessor += antecessor
        antecessor = soma
    if(sucessor == numero):
        print("{} faz parte da sequencia de  Fibonacci".format(numero))
    else:
        print("{} não faz parte da sequencia de Fibonacci".format(numero))
fibonacci()