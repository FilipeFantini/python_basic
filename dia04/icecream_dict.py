#%%
icecream_type = input("Entre com o tipo do sorvete: [casquinha/cascão/cestinha] ").lower()
flavor = input("Entre com o sabor do sorvete: [morango/creme/chocolate] ").lower()
topping_type = input("Entre com a cobertura que você quer: [caramelo/morango/chocolate] ").lower()

icecreams = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00
}

price = 0

if icecream_type in icecreams:
    price += icecreams[icecream_type]
else:
    print("Tipo de sorvete não disponível")

toppings = {
    "caramelo": 1.5,
    "morango": 1.6,
    "chocolate": 1.0,
    "": 0
}

if topping_type in toppings:
    price += toppings[topping_type]
else:
    print("Tipo de cobertura não disponível")

print("Seu sorvete ", icecream_type, " de ", flavor, " cobertura ", topping_type, " custará: $", price)
# %%
