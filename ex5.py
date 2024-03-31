#Inverter uma palavra
def inversor_texto(texto):
    texto_reverso = ''
    for i in range(len(texto) -1, -1, -1):
        texto_reverso += texto[i]
    return texto_reverso

texto = input("Digite algo: ")
texto_reverso = inversor_texto(texto)
print("A palavra digitada foi {} e ela invertida é {}".format(texto, texto_reverso))