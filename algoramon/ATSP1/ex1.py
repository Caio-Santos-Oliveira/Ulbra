altura = float(input("digite a sua altura/ "))
sexo = str(input("digite seu sexo/ "))
if sexo=="homem" or sexo=="masculino":
    peso = (72.7*altura)-58
    print(f"seu peso ideal é de {peso} kilos")
elif sexo=="mulher" or sexo=="feminino":
    peso = (62.1*altura)-44.7
    print(f"seu peso ideal é de {peso} kilos")

        