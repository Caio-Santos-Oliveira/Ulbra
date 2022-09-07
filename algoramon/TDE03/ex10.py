from traceback import print_tb


nven = int(input("digite o numero do funcionario"))
salario = float(input("digite o salario fixo"))
ncar = int(input("digite o numero de carros vendidos"))
vcar = float(input("digite a comissão por carro vendido"))
salariof = salario + ncar*vcar
print(f"o salario final do funcionario {nven} é de {salariof}")
 