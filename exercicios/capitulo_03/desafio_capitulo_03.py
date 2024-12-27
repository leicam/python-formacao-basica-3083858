from decimal import Decimal

#exercicios booleano
lista_um = ["pera", "uva", "maca", None, "salada-mista"]

for item in lista_um :
    if item :
        print(f"{item} e uma fruta valida!")
    else:
        print(f"{item} NAO e uma fruta valida!")

#exercicios numerico
valor_um = 234521
valor_dois = 932481

print(type(valor_um + valor_dois))

valor_tres = 3.3333333
valor_quatro = 932481

print(type(valor_tres + valor_quatro))

valor_cinco = "3.14159265358979323846"

print(f"a variavel valor_cinco e do tipo {type(valor_cinco)}")

valor_cinco = Decimal(valor_cinco)

print(f"agora a variavel valor_cinco e do tipo {type(valor_cinco)}")

#exercicios string

string_um = "Juliano Maciel"

print("Imprima apenas os primeiros 3 caracteres da sua string", string_um[:3])
print("Converta toda a string para letras minúsculas", string_um.lower())
print("Converta toda a string para letras maiúsculas", string_um.upper())
print("Formate a string para que tenha apenas a primeira letra maiúscula", string_um.capitalize())
print("ormate a string para que a primeira letra de cada palavra seja maiúscula", string_um.title())
print("Inverta o case de todas as letras da string", string_um.swapcase()) #inverte o case das palavras da string
print("Formate uma string usando string format", f"Ola {string_um}!")