print("sem ano bisexto")
n_pag = float(input("digite o numero que páginas que pretender ler ao dia "))
mes = (input("digite o mes "))
if mes == "janeiro":
    num_dias = 31
elif mes == "fevereiro":
    num_dias = 28
elif mes == "março":
    num_dias = 31
elif mes == "abril":
    num_dias = 30
elif mes == "maio":
    num_dias = 31
elif mes == "junho":
    num_dias = 30
elif mes == "julho":
    num_dias = 31
elif mes == "agosto":
    num_dias = 31
elif mes == "setembro":
    num_dias = 30
elif mes == "outubro":
    num_dias = 31
elif mes == "novembro":
    num_dias = 30
elif mes == "dezembro":
    num_dias = 31
else:
    print("digite o mes corretamente sem espaço e letra maiúscula")
    mes = (input("digite o mes "))
    if mes == "janeiro":
        num_dias = 31
    elif mes == "fevereiro":
        num_dias = 28
    elif mes == "março":
        num_dias = 31
    elif mes == "abril":
        num_dias = 30
    elif mes == "maio":
        num_dias = 31
    elif mes == "junho":
        num_dias = 30
    elif mes == "julho":
        num_dias = 31
    elif mes == "agosto":
        num_dias = 31
    elif mes == "setembro":
        num_dias = 30
    elif mes == "outubro":
        num_dias = 31
    elif mes == "novembro":
        num_dias = 30
    elif mes == "dezembro":
        num_dias = 31
    else:
        print("erro, tente novamente")
mes_pag = num_dias*n_pag
ano_pag = n_pag*365
print(f"no mes de {mes} voce vai ler {mes_pag} páginas!")
print(f"no ano você vai ler {ano_pag} páginas!")

