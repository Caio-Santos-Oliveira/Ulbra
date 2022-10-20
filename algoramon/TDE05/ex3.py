indice = float(input("Qual o índice de poluição média no mundo?"))
if indice>0.3 and indice<0.4:
    print("As empresas do primeiro grupo devem suspender suas atividades")
elif indice>0.4 and indice<0.5:
    print("As empresas do primeiro e segundo grupo devem suspender suas atividades")
elif indice>0.5:
    print("Todas as empresas devem suspender suas atividades")
else:
    print("tudo sobre controle")