ndias = int(input("digite o numero de diarias"))
valortotal = ndias*50
if ndias < 15:
    valortotal += 1.50 * ndias
elif ndias == 15:
    valortotal += 1 * ndias 
else:
    valortotal += 0.50 * ndias 
print(f"O valor total é R${valortotal}")
