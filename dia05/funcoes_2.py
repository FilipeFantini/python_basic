#%%

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

soma(10,20,100, 4, 500)

#%%

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i

    return total

operacao("mult",10,20,100, 4, 500)

#%%

dados = ['teo', 'calvo', 23, ['nah', 'elaine', 'claudia']]

nome, sobrenome, *_ = dados
nome, *_, ex  = dados

print(nome)
print(sobrenome)
print(ex)

#%%

a=10
b=20
print(a, b)

a,b = b,a 

print(a, b)