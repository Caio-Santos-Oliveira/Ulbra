num_fun = int(input("digite o numero do funcionário "))
hora_fun = float(input("digite as horas trabalhadas por mês "))
valor_hora = float(input("digite o valor da hora trabalhada "))
num_filhos = int(input("digite o numero de filhos menores de 14 anos "))
idade_fun = int(input("digite a idade do funcionário "))
tempo_servico = float(input("digite o tempo de serviço "))
sala_familia = float(input("digite o salário família por filho "))
sala_mensal = valor_hora*hora_fun
sala_bruto = sala_mensal + num_filhos*sala_familia
if sala_bruto>1500:
    ir = 0.15
elif sala_bruto>500 and sala_bruto<=1.500:
    ir = 0.08
else:
    ir = 0
ir_valor = ir*sala_bruto
inss_valor = sala_bruto*0.085
sala_liquido = sala_bruto - inss_valor - ir_valor
print(f" o funcionário de numero {num_fun}")
print(f" tem seu salário bruto de R${sala_bruto}")
print(f" possui descontos de R${ir_valor} de IR, e R${inss_valor}")
print(f" seu salário liquído é de R${sala_liquido}")
