n = float(input("digite um numero "))
n2 = 1
soma = 0
if n>0:
    while n2 != n:
        n2 = n2+1
        soma = soma+n2
    print(soma)
elif n==0:
    print("zero")
else:
    print("numeros positivos, por favor")
    
n2 = 1
nn = int(input("digite um numero "))   
soma = 0
for x in range (nn-1):
    n2 = n2+1
    soma = soma+n2
print(soma)