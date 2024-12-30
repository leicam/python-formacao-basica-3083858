#exercicios if elif else

minha_lista = range(1, 31)

for valor in minha_lista:
    if valor > 20 :
        print("Esse número maior do que 20. valor = ", valor)
    elif valor == 20:
        print("Esse número é igual à ", valor)

ate_12 = []
entre_13_e_20 = []
maior_21 = []

for valor in minha_lista:
    if valor <= 12:
        ate_12.append(valor)
    elif valor >= 13 and valor <= 20:
        entre_13_e_20.append(valor)
    else:
        maior_21.append(valor)

print("ate_12 -> ", ate_12)
print("entre_13_e_20 -> ", entre_13_e_20)
print("maior_21 -> ", maior_21)

#exercicios operador ternario
[print("Esse número maior do que 20. valor = ", idade) if (idade > 20) else print("Esse número é igual à ", idade) if (idade == 20) else print("Esse número menor do que 20. valor = ", idade) for idade in minha_lista]

ate_12 = []
entre_13_e_20 = []
maior_21 = []

[ate_12.append(idade) if (idade <= 12) else entre_13_e_20.append(idade) if (idade >= 13 and idade <= 20) else maior_21.append(idade) for idade in minha_lista]

print("ate_12 -> ", ate_12)
print("entre_13_e_20 -> ", entre_13_e_20)
print("maior_21 -> ", maior_21)

#exercicios for loop
lista_for_loop = range(100, 1100, 100)

for valor in lista_for_loop:
    print("valor = ", valor)

for valor in lista_for_loop:
    if (valor % 3 == 0):
        print (f"valor {valor} é divisível por {3}!")
        continue
    else:
        print (f"valor {valor} não é divisível por {3}!")
    
    print("retornando para o inicio do loop-for")

for valor in lista_for_loop:
    if (valor % 3 == 0):
        print (f"Encontrado o primeiro valor {valor} divisível por {3} da lista!")
        break
    else:
        print (f"valor {valor} não é divisível por {3}!")
    
    print("retornando para o inicio do loop-for")

valores_for_loop = range(1, 101)

for valor in valores_for_loop:
    if (valor % 2 == 0):
        print(f"valor: {valor} é um número par!")
    else:
        print(f"valor: {valor} é um número impar!")

#exercicio while loop

contador = 0

while contador <= 5 :
    print(f"contador = {contador}")
    contador += 1

contador = 0

while contador <= 10 :
    if contador % 2 != 0:
        print(f"contador = {contador} é um número impar!")
    contador += 1
else:
    print("fim do exercicio while loop")
    
#exercicios fizz fizbuzz

items_fizz_buzz = range(1, 101)

for valor in items_fizz_buzz:
    if valor % 3 == 0 and valor % 5 == 0:
        print("FizBuzz")
    elif valor % 3 == 0:
        print("Fizz")
    elif valor % 5 == 0:
        print("Buzz")
    else:
        print(f"valor = {valor}")

print("programa encerrado!")