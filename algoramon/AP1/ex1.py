faturamento = float(input("digite o faturamento da empresa\n"))
despesas = float(input("digite as despesas da empresa\n"))
pis = faturamento*0.0065
cofins = faturamento*0.03
lucro = faturamento-despesas-pis-cofins
print(f"o faturamento da empresa é R${faturamento}")
print(f"o valor do PIS é R${pis}")
print(f"o valor do COFINS é R${cofins}")
print(f"o lucro da empresa é R${lucro}")
