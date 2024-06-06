def check_input():
    """Essa funcao valida se o tipo de dado passado é de fato um valor do tipo inteiro"""
    try:
        return int(input("Entre com um número de 1 a 15: "))
    
    except ValueError as err:
        return print("Isso não é um número!")
    
def check_interval(numero):
    """Checa se o numero passado esta entre o intervalo de 1 e 15, considerando ambos.
    numero: int
    """
    return 1<= numero <=15

def valida_entrada():
    """Essa funcao valida a entrada do usuario para garantir a integridade do codigo."""
    while True:
        
        numero = check_input()

        if type(numero) != int:
            print(numero)
            continue

        if check_interval(numero):
            return numero


numero_sorte = 7

for i in range(3):
    
    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!!!")
        break
    
    elif numero > numero_sorte:
        print ("Você errou! Tente um número menor!")

    else:
        print("Você errou! Tente um número maior!")