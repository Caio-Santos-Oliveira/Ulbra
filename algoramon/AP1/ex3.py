cigarros_dia = int(input("digite o numero de cigarros médio que você fuma ao dia\n"))
tempo_fumo = int(input("faz quantos meses que você fuma?\n"))
if tempo_fumo <= 3:
    print("seus dentes já estão amarelos\n ")
elif tempo_fumo >3 and tempo_fumo <= 12:
    print("alem dos dentes amarelos, seu paladar e sua respiração estão comprometidas\n ")
else:
    print("alem dos dentes amarelos, seu paladar e sua respiração comprometidas, seu pulmão também está comprometido\n ")
cigarros_fumados = (tempo_fumo*30)*cigarros_dia
cigarros_ano = cigarros_dia*365
minutos_perdida = cigarros_fumados*15
minutos_perdida_ano = cigarros_ano*15
dias_perdidos = int(minutos_perdida/1440)
dias_perdidos_ano = int(minutos_perdida_ano/1440)
print(f"voce ja perdeu {minutos_perdida} minutos de vida com os cigarros que já fumou, ou seja, você morrerá {dias_perdidos} dias mais cedo\n ")
print(f"se continuar fumando vai perder mais {minutos_perdida_ano} minutos de vida a cada ano que passar, ou seja, menos {dias_perdidos_ano} dias por ano\n ")