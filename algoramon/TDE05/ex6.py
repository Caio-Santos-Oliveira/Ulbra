nota1=float(input("digite a nota 1"))
nota2=float(input("digite a nota 2"))
nota3=float(input("digite a nota 3"))
media=(nota1+nota2+nota3)/3
if media>=9:
    conceito= "A"
elif media>=7.5 and media<9:
    conceito="B"
elif media >=6 and media<7.5:
    conceito="C"
elif media <=4 and media <6:
    conceito="D"
else:
    conceito="E"
if conceito=="A" or conceito=="B":
    print("aluno aprovado")
else:
    print("reprovado")
print(media)
print(conceito)
