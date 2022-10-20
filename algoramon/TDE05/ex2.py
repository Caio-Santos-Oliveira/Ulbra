from re import A


i=int(input("digite um valor inteiro entre 1 e 3"))
a=float(input("digite um valor qualquer"))
b=float(input("digite um valor qualquer"))
c=float(input("digite um valor qualquer"))
print(i)
print(a)
print(b)
print(c)
if a<b and a<c:
    valormenor = a
elif b<a and b<c:
    valormenor = b
else:
    valormenor = c
if a>b and a>c:
    valormaior = a 
elif b>c and b>a:
    valormaior = b 
else:
    valormaior = c
if a>valormenor and a<valormaior:
    valormeio = a 
elif b>valormenor and b<valormaior:
    valormeio = b 
else:
    valormeio = c
if i==1:
    print(valormenor,valormeio,valormaior)
elif i==2:
    print(valormaior,valormeio,valormenor)
else:
    print(valormenor,valormaior,valormeio)
    
