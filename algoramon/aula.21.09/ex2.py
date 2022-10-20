print("aqui jaz um algoritimo para calcular o custe de uma viagem")
distancia = float(input("digite a distância a ser percorrida em km "))
preco_gas = float(input("digite o preço da gasolina a ser paga "))
carro = str(input("seu veículo é uma moto, carro, esportivo, caminhonete ou caminhao? "))
num_passageiros = int(input("digite o numero total de passageiros nessa viagem "))
volta = str(input("se a viajem for só de ida, digite (sim) "))
if carro == "moto":
    consumo_veiculo = 21
elif carro == "carro":
    consumo_veiculo = 17
elif carro == "esportivo":
    consumo_veiculo = 13
elif carro == "caminhonete":
    consumo_veiculo = 9
elif carro == "caminhao":
    consumo_veiculo = 6.5
else:
    consumo_veiculo = 4
if num_passageiros == 1:
    consumo=consumo_veiculo
else:
    consumo=consumo_veiculo/(1+(num_passageiros-1)/10)
litros = distancia/consumo
custo = litros*preco_gas
if volta == "sim":
    custo_final = custo
else:
    custo_final = custo*2
print(f"você irá gastar R${custo_final} nessa viajem")