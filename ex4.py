#Verifica qual interruptor liga cada lampada
def liga_interruptores():

    interruptores = [False, False, False]
    
    configuracao = [True, False, True]
    
    for i in range(len(interruptores)):
        interruptores[i] = configuracao[i]
    
    return interruptores

modo_inicial = liga_interruptores()

l1_inicial = modo_inicial[0]
l2_inicial = modo_inicial[1]
l3_inicial = modo_inicial[2]

modo_inicial = [False, False, False]

interruptor_selecionado = 0
modo_inicial[interruptor_selecionado] = True

l1 = modo_inicial[0]
l2 = modo_inicial[1]
l3 = modo_inicial[2]

if l1 == l1_inicial:
    if l2 == l2_inicial:
        interruptor1 = (interruptor_selecionado + 1) % 3
        interruptor2 = interruptor_selecionado
        interruptor3 = (interruptor_selecionado + 2) % 3
    else:
        interruptor1 = interruptor_selecionado
        interruptor2 = (interruptor_selecionado + 1) % 3
        interruptor3 = (interruptor_selecionado + 2) % 3
else:
    if l2 == l2_inicial:
        interruptor1 = (interruptor_selecionado + 2) % 3
        interruptor2 = (interruptor_selecionado + 1) % 3
        interruptor3 = interruptor_selecionado
    else:
        interruptor1 = (interruptor_selecionado + 1) % 3
        interruptor2 = (interruptor_selecionado + 2) % 3
        interruptor3 = interruptor_selecionado

print("O interruptor 1 controla a lâmpada", interruptor1)
print("O interruptor 2 controla a lâmpada", interruptor2)
print("O interruptor 3 controla a lâmpada", interruptor3)
