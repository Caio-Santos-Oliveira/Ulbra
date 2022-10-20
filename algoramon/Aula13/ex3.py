sup_50 = 0
num_pessoas = 0
soma_altura = 0
cont_pessoas = 0
for x in range (25):
    idade = int(input("digite a idade "))
    altura = float(input("digite a altura "))
    peso = float(input("digite o peso em kg "))
    if idade > 50:
        sup_50 = sup_50 + 1
    if idade >= 10 and idade < 21:
        num_pessoas = num_pessoas + 1
        soma_altura = soma_altura + altura
    if peso < 40:
        cont_pessoas = cont_pessoas + 1
media = soma_altura/num_pessoas
print(f"a quantidade de pessoas com mais de 50 anos é {sup_50}")
if num_pessoas!=0:
    print(f"a media de altura das pessoas entre 10 e 20 anos é de {media}")
else:
    print("não há pessoas entre 10 e 20 anos")
print(f"{cont_pessoas*4}% das pessoas tem menos de 40 kilos")