nomedofuncionario=input("digite seu nome")
salario=float(input("digite seu salário"))
novosalario=0.0
if salario <=400:
    novosalario=salario*1.15
    print("ganhou 15% de aumento")
elif salario>400 and salario<=700:
    novosalario=salario*1.12
    print("ganhou 12% de aumento")
elif salario >700 and salario<=1000:
    novosalario=salario*1.1
    print("ganhou 10% de aumento")
elif salario>1000 and salario<=1800:
    novosalario=salario*1.07
    print("ganhou 7% de aumento")
elif salario>1800 and salario<=2500:
    novosalario=salario*1.04
    print("ganhou 4% de aumento")
else:
    print("sem aumento")
print(f"Parabéns {nomedofuncionario} seu novo salário é de R${novosalario}")