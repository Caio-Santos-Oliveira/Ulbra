preco_terreno = float(input("digite o preço que foi pago no terreno "))
tam_terreno = float(input("digite o tamanho da planta em metros quadrados "))
mao_obra = float(input("digite o preço a ser pego pelo metro quadrado "))
condominio = str(input("digite 'sim' se a casa for ser construída dentro de um condomínio "))
num_andares = int(input("digite o numero de pisos que a casa irá possuir "))

if condominio == "sim":
    taxa = 1500
else:
    taxa = 0
num_meses = ((tam_terreno*num_andares)%15)+1
taxa_condo = taxa*num_meses
custo_obra = (tam_terreno*mao_obra)*num_andares
precofinal = preco_terreno+custo_obra+taxa_condo
print(f"o custo total dessa casa foi de {precofinal} em um prazo de {num_meses} meses")