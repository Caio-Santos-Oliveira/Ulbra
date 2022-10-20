from cmath import pi


codaluno=int(input("digite o codigo do aluno"))
nota1=float(input("digite a nota 1"))
nota2=float(input("digite a nota 2"))
nota3=float(input("digite a nota 3"))
mediaponderada=(nota1*4+nota2*3+nota3*3)/10
print(codaluno)
print(nota1)
print(nota2)
print(nota3)
if mediaponderada>=7:
    print(f"o aluno {codaluno} foi aprovado")
else:
    print(f"o aluno {codaluno} foi reprovado")
print(mediaponderada)