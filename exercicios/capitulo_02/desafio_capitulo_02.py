#exercicio variaveis

integer_um = 1
float_um = 1.2
complex_um = 7+2j
string_um = 'TESTE UM'
string_dois = "TESTE DOIS"
string_tres = '''TESTE
                TRES'''
boleana_verdadeira = True
boleana_falsa = False

print("integer_um", integer_um)
print("float_um", float_um)
print("complex_um", complex_um)
print("string_um", string_um)
print("string_dois", string_dois)
print("string_tres", string_tres)
print("boleana_verdadeira", boleana_verdadeira)
print("boleana_falsa", boleana_falsa)

#exercicio operadores aritmeticos
print("adicao -> 1 + 1 = ", 1 + 1)
print("multiplicacao -> 2 * 2 = ", 2 * 2)
print("concatenacao", "Meu nome e: " + "Juliano")
#print("multiplicacao com strings -> teste * teste_dois = ", "teste" * "teste_dois") erro na execucao do codigo
print("potencia -> 3 ** 3 = ", 3 ** 3)
print("subtracao -> 10 - 3 = ", 10 - 3)
print("divisao -> 10 / 3 = ", 10 / 3)
print("divisao inteira -> 10 // 3 = ", 10 // 3)
print("modulo (resto inteiro da divisao) -> 10 % 3 = ", 10 % 3)

a = 15.3
b = 1.3

print("a = ", a)
print("b = ", b)
print("operacao utilizando variaveis -> a + b = ", a + b)
print("operacao utilizando variaveis -> a - b = ", a - b)
print("operacao utilizando variaveis -> a / b = ", a / b)
print("operacao utilizando variaveis -> a // b = ", a // b)
print("operacao utilizando variaveis -> a % b = ", a % b)
print("operacao utilizando variaveis -> a * b = ", a * b)
print("operacao utilizando variaveis -> a ** b = ", a ** b)

#exercicio operadores relacionais
print(a, " > ", b, " = ", a > b)
print(a, " >= ", b, " = ", a >= b)
print(a, " < ", b, " = ", a < b)
print(a, " <= ", b, " = ", a <= b)
print(a, " == ", b, " = ", a == b)
print(a, " != ", b, " = ", a != b)

#exercicio operadores logicos
print("6 < 10 and 6 > 3", 6 < 10 and 6 > 3)
print("6 > 10 or 6 > 3", 6 > 10 or 6 > 3)
print("not 6 == 3", not 6 == 3)

#exercicios de associacao
print("teste in [1, 2, 3]", "teste" in [1, 2, 3])
print("teste not in [1, 2, 3]", "teste" not in [1, 2, 3])

#exercicios estruturas de dados
print("lista vazia: ", [])
print("lista com unico tipo de dados: ", ["A", "B", "C"])
print("lista com dados mesclados: ", [1, "A", True, ["elemento1", "elemento2"]])
print("tupla: ", ("Pera", "Uva", "Maca", "Salada-Mista"))
print("conjunto: ", {"Batman", "Robin", "Asa Noturna", "Batman"})
dicionario = {"animais": "cachorro, gato, pombo", "carros" : "porsche 911, bmw M3, ferrari F40"}
print("dicionario", dicionario)
print("dicionario -> carros: ", dicionario["carros"])
