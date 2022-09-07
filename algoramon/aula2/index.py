from ctypes.wintypes import HCOLORSPACE
from string import octdigits


print ("EX1")
A = 2
B = 5
C = 10
resposta1 = A+B*C/A
resposta2 = (A+B)*C/A
resposta3 = (A+B*C)/A
print(f"resposta letra A é {resposta1}")
print(f"resposta letra B é {resposta2}")
print(f"resposta letra C é {resposta3}")

print ("EX2")
numero1 = float(input("digite um numero/n"))
numero2 = float(input("digite outro numero/n"))
resposta4 = (numero1+numero2)/2
print(f"a soma desses numeros é {numero1+numero2}")
print(f"a media desses numeros é {resposta4}")

print ("EX3")
numero3 = float(input("digite um numero/n"))
resposta5 = numero3-1
resposta6 = numero3+1
print(f"antecessor {resposta5}")
print(f"sucessor {resposta6}")

print ("EX4")
numero4 = float(input("digite um numero/n"))
numero5 = float(input("digite um numero/n"))
numero6 = float(input("digite um numero/n"))
resposta7 = (numero4+numero5+numero6)/3
print(f"a média aritimetica é {resposta7}")

print ("EX5")
numerofun = float(input("digite o numero do funcionario/n"))
horas = float(input("digite as horas trabalhadas por mes/n"))
valorhora = float(input("digite o valor da hora/n"))
salario = horas*valorhora
print(f"o salário é {salario}")

print ("EX6")
numero7 = float(input("digite um numero/n"))
numero8 = float(input("digite outro numero/n"))
adicao = numero7+numero8
subtracao = numero7-numero8
multiplicacao = numero7*numero8
divisao = numero7/numero8
print(f"resultado1 {adicao}")
print(f"resultado2 {subtracao}")
print(f"resultado3 {multiplicacao}")
print(f"resultado4 {divisao}")

print ("EX7")
numero9 = float(input("digite a base/n"))
numero10 = float(input("digite a altura/n"))
area = (numero9*numero10)/2
print (f"a area do triangulo é {area}")

print ("EX8")
numerocoelhos = float(input("digite o numero de coelhos/n"))
custo = (numerocoelhos*0.7)/18+10
print (f"O custo para a criação de {numerocoelhos} coelhos, é de {custo}")
 
print ("EX9")
custo2 = float(input("digite o valor de custo/n"))
venda2 = float(input("digite o valor de venda"))
lucro = venda2-custo2
print (f"lucro R${lucro}")
 
print ("EX10")
valor = float(input("digite o valor do produto/n"))
quantidade = float(input("digite a quantidade de produtos/n"))
pagamento = valor*quantidade
print (f"o total da compra é de R${pagamento}")

print ("EX11")
numero11 = float(input("digite um numero/n"))
numero12 = float(input("digite outro numero/n"))
resto = numero11%numero12
print (f"o resto da divisão é {resto}")

print ("EX12")
numero13 = float(input("digite um numero/n"))
numero14 = float(input("digite outro numero/n"))
inteiro = numero14//numero13
print (f"o resultado inteiro é {inteiro}")