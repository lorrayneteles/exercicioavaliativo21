#diferença entre dois numeros

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
if num1 > num2:
    diferenca = num1 - num2
else:
    diferenca = num2 - num1 
print(f'A diferenca entre os dois numeros é {diferenca}')