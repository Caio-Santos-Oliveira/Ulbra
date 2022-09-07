import math

raio = float(input("digite o raio do cilindro em metros"))
altura = float(input("digite a altura do cilindro em metros"))
arealat = 2*math.pi*raio*altura 
areabase = math.pi*raio*raio 
areatotal = areabase+arealat
qlitros = areatotal/3
qlatas = int((qlitros/5)+1)
custo = qlatas*150
print(f"serao necessarias {qlatas} latas de tinta, resultando num valor de R${custo}")
