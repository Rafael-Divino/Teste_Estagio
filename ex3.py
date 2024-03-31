"""
A) sequencia de numeros impares
    1,3,5,7,9,...
B) sequencia de numeros multiplicados por 2
    2,4,6,8,16,32,64,128,...
C) Sequencia de numeros naturais elevado ao quadrado
    0,1,4,9,16,25,36,49,...
D) Sequencia de numeros pares elevado ao quadrado
    4,16,36,64,100,...
E) Sequencia dos numeros de Finonacci
    1,1,2,3,5,8,13,...
F) Sequencia de numeros que começam com a letra D
    2,10,12,16,17,18,19,200,...
"""
def sequencia_impar(n):
    i = 1
    seq = []
    while len(seq) < n:
        seq.append(i)
        i += 2
    return seq

print(sequencia_impar(5)) #A)
print("////////////////////////////")

def sequencia_par_mult_dois(n):
    i = 1
    seq = []
    while len(seq) < n:
        seq.append(i*2)
        i *= 2
    return seq
print(sequencia_par_mult_dois(7)) #B)
print("////////////////////////////")

def sequencia_naturais_quadrado(n):
    numeros = [i**2 for i in range(n)]
    return numeros
print(sequencia_naturais_quadrado(8)) #C)
print("////////////////////////////")

def sequencia_pares_quadrado(n):
    i = 2
    seq = []
    while len(seq) < n:
        seq.append(i**2)
        i += 2
    return seq
print(sequencia_pares_quadrado(5)) #D)
print("////////////////////////////")


def fibonecci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonecci(numero-1) + fibonecci(numero-2)
fibo = [fibonecci(i) for i in range(1,8)]
print(fibo) #E)
print("////////////////////////////")



def numero_por_extenso(numero):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
                 17: "dezessete", 18: "dezoito", 19: "dezenove"}
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    if numero in especiais:
        return especiais[numero]
    elif numero < 100:
        dezena = numero // 10
        unidade = numero % 10
        return dezenas[dezena] + (" e " if dezena > 1 and unidade != 0 else "") + unidades[unidade]
    elif numero == 100:
        return "cem"
    else:
        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = (numero % 100) % 10
        return centenas[centena] + (" e " if (dezena > 0 or unidade > 0) else "") + numero_por_extenso(numero % 100)

def sequencia_com_d():
    numeros_com_d = []
    for numero in range(2, 201):
        numero_extenso = numero_por_extenso(numero)
        if numero_extenso.startswith('d'):
            numeros_com_d.append(numero)
    return numeros_com_d

lista_com_d = sequencia_com_d()
print(lista_com_d)#F)




