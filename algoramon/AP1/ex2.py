idade = int(input("quantos anos você tem?\n"))
if idade>=10 and idade<=20:
    ponto1 = 1
elif idade>=21 and idade<=30:
    ponto1 = 2
elif idade>=31 and idade<=40:
    ponto1 = 3
elif idade>=41 and idade<=50:
    ponto1 = 4
elif idade>=51 and idade<=60:
    ponto1 = 6
elif idade>60:
    ponto1 = 8
else:
    ponto1 = 0   
heranca_familiar = int(input("quantos parentes com cardio patia você possui?\n"))
if heranca_familiar == 0:
    ponto2 = 1
elif heranca_familiar == 1:
    ponto2 = 2    
elif heranca_familiar == 2:
    ponto2 = 3
elif heranca_familiar>=3:
    ponto2 = 7
else:
    print("numeros negativos não pode")
sexo = str(input("digite seu sexo\n"))
percent_gordura = float(input("digite seu percentual de gordura corporal\n"))
if sexo == "homem" or sexo == "masculino":
    if percent_gordura<12:
        ponto3 = 0
    elif percent_gordura>=12 and percent_gordura<16:
        ponto3 = 1
    elif percent_gordura>=16 and percent_gordura<20:
        ponto3 = 2
    elif percent_gordura>=20 and percent_gordura<22:
        ponto3 = 3
    elif percent_gordura>=22 and percent_gordura<30:
        ponto3 = 5
    else:
        ponto3 = 7
elif sexo == "mulher" or sexo == "feminino":
    if percent_gordura<16:
        ponto3 = 0
    elif percent_gordura>=16 and percent_gordura<20:
        ponto3 = 1
    elif percent_gordura>=20 and percent_gordura<25:
        ponto3 = 2
    elif percent_gordura>=25 and percent_gordura<32:
        ponto3 = 3
    elif percent_gordura>=32 and percent_gordura<40:
        ponto3 = 5
    else:
        ponto3 = 7
else:
    print("digite um sexo válido")
tabagismo = int(input("digite o numero de cigarros que voce fuma por dia\n"))
if tabagismo < 1:
    ponto4 = 0
elif tabagismo >= 1 and tabagismo < 11:
    ponto4 = 1
elif tabagismo >= 11 and tabagismo <21:
    ponto4 = 2
elif tabagismo >= 21 and tabagismo <31:
    ponto4 = 4
elif tabagismo >= 31 and tabagismo <41:
    ponto4 = 6
elif tabagismo > 40:
    ponto4 = 10
exe_min_semana = int(input("quantos minutos de exercicio você pratica por semana?\n"))
if exe_min_semana > 240:
    ponto5 = 0
elif exe_min_semana >= 120 and exe_min_semana <241:
    ponto5 = 1
elif exe_min_semana >= 80 and exe_min_semana <120:
    ponto5 = 2
elif exe_min_semana >= 60 and exe_min_semana <80:
    ponto5 = 3
elif exe_min_semana >= 31 and exe_min_semana <60:
    ponto5 = 6
else:
    ponto5 = 8
colesterol = int(input("qual sua pontuação de colesterol?\n"))
if colesterol < 180:
    ponto6 = 1
elif colesterol >= 181 and colesterol <206:
    ponto6 = 2
elif colesterol >= 206 and colesterol <231:
    ponto6 = 3
elif colesterol >= 231 and colesterol <256:
    ponto6 = 4
elif colesterol >= 256 and colesterol <281:
    ponto6 = 5
else:
    ponto6 = 7
pres_art_sis = int(input("digite sua pressão arterial sistólica em mmHg\n"))
if pres_art_sis < 120:
    ponto7 = 1
elif pres_art_sis >= 120 and pres_art_sis <140:
    ponto7 = 2
elif pres_art_sis >= 140 and pres_art_sis <260:
    ponto7 = 3
elif pres_art_sis >= 160 and pres_art_sis <180:
    ponto7 = 4
elif pres_art_sis >= 180 and pres_art_sis <200:
    ponto7 = 6
else:
    ponto7 = 8
pres_art_dia = int(input("digite sua pressão arterial diastólica em mmHg\n"))
if pres_art_dia < 70:
    ponto8 = 1
elif pres_art_dia >= 70 and pres_art_dia <77:
    ponto8 = 2
elif pres_art_dia >= 77 and pres_art_dia <83:
    ponto8 = 3
elif pres_art_dia >= 83 and pres_art_dia <94:
    ponto8 = 4
elif pres_art_dia >= 94 and pres_art_dia <106:
    ponto8 = 6
else:
    ponto8 = 8
    
pontuacao_total = ponto1+ponto2+ponto3+ponto4+ponto5+ponto6+ponto7+ponto8
print(f"sua pontuação de risco cardiovascular é de {pontuacao_total} pontos")
if pontuacao_total >= 5 and pontuacao_total <12:
    print("isso significa que seu risco é bem abaixo da média")
elif pontuacao_total >= 12 and pontuacao_total <18:
    print("isso significa que seu risco é abaixo da média")
elif pontuacao_total >= 18 and pontuacao_total <25:
    print("isso significa que seu risco é médio habitual")
elif pontuacao_total >= 25 and pontuacao_total <32:
    print("isso significa que seu risco é moderado")
elif pontuacao_total >= 32 and pontuacao_total <41:
    print("isso significa que seu risco é perigoso")
elif pontuacao_total >= 41 and pontuacao_total <64:
    print("isso significa que você está em perigo urgente, procure um médico agora")
else:
    print("repita o processo")
