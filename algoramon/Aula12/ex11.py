for x in range (10):
    matricula = int(input("Digite a matrícula do aluno "))
    nome = str(input("Digite o nome do aluno "))
    nota1 = float(input("digite a nota 1 do aluno "))
    nota2 = float(input("digite a nota 2 do aluno "))
    nota3 = float(input("digite a nota 3 do aluno "))
    media = (nota1+nota2+nota3)/3
    if media >=7:
        print(f"O aluno {nome} está aprovado com nota {media}")
    else:
        print(f"O aluno {nome} está reprovado com nota {media}")
