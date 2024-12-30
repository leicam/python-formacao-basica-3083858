from collections import defaultdict

#exercicios sets e tuplas

herois_conjunto = {"sniper", "wind-ranger", "troll-warlord", "dragon-knight", "sniper"}
print("heróis conjunto: ", herois_conjunto)

herois_lista = ["drow-ranger", "bristle-back", "faceless-void", "drow-ranger"]
print("heróis lista: ", herois_lista)

herois_conjunto_convertido = set(herois_lista)
print("heróis conjunto convertido: ", herois_conjunto_convertido)

herois_conjunto_convertido.add("crystal-maiden")
print("heróis conjunto registro adicionado: ", herois_conjunto_convertido)

herois_conjunto_convertido.discard("faceless-void")
print("heróis conjunto registro descartado: ", herois_conjunto_convertido)

herois_conjunto_filtrado = [item for item in herois_conjunto_convertido if item == "drow-ranger"] 
print("heróis conjunto registro filtrado: ", herois_conjunto_filtrado)

herois_tupla = ("enchantress", "shadow-shaman", "jakiro")
print("heróis tupla: ", herois_tupla)

print("imprimindo o elemnto do indice 2 da tupla: ", herois_tupla[2])


def heroisDeInteligencia() :
    return ["keep-of-the-light", "lina", "zeus", "witch-doctor"]

print("invocando metodo heroisDeInteligencia() -> ", heroisDeInteligencia())

kotl, lina, zeus, macaco = heroisDeInteligencia()
print(kotl)
print(lina)
print(zeus)
print(macaco)

#exercicios lista

meu_range = range(14)
meu_range_convertido_para_lista = list(meu_range)

print("Imprimindo os três primeiros elementos do range convertido em lista: ", meu_range_convertido_para_lista[0:3])
meu_range_convertido_para_lista.append(23)
print("Item inserido no final do range convertido em lista: ", meu_range_convertido_para_lista)

meu_range_convertido_para_lista.remove(11)
print("Removido elemento 11 do range convertido em lista: ", meu_range_convertido_para_lista)

lista_copia = meu_range_convertido_para_lista.copy()
print("meu_range_convertido_para_lista -> ", meu_range_convertido_para_lista)
print("lista_copia -> ", lista_copia)

#exercicios lista comprehension
minha_lista_numerica = [20, 14, 27, 13, 25]
print("minha_lista_numerica  = ", minha_lista_numerica)

minha_lista_numerica_multiplicada = [item * 2 for item in minha_lista_numerica]
print("minha_lista_numerica_multiplicada = ", minha_lista_numerica_multiplicada)

minha_lista_items_divisiveis_por_vinte = [item for item in  range(0, 100) if item % 20 == 0]
print("minha_lista_items_divisiveis_por_vinte = ", minha_lista_items_divisiveis_por_vinte)

minha_string = '''
    Matar à distância é a especialidade do Sniper.
    Ele mantém os seus inimigos sempre em alerta com
    uma constante chuva de tiros, para então, no momento
    certo, finalizá-los com um disparo mortal.
'''

def formatarString(valor) :
    return valor.replace(',', '').replace('.', '').replace('-', '').lower()

lista_palavras_normalizadas = [formatarString(item) for item in minha_string.split()]
print("palavras normalizadas -> ", lista_palavras_normalizadas)

#exercicios dicionarios
meu_dicionario = {"herois": ["medusa", "alchemist", "lion", "bane"],
                  "atributo": ["força", "agilidade", "inteligência", "universal"]}
print("meu_dicionario -> ", meu_dicionario)

chaves_dicionario = meu_dicionario.keys()
print("chaves do dicionário -> ", chaves_dicionario)
print(type(chaves_dicionario))

lista_valores_dicionario = meu_dicionario.values()
print("dados do dicionário -> ", lista_valores_dicionario)
print(type(lista_valores_dicionario))

print("localizando valores correspondentes a chave atributo -> ", meu_dicionario["atributo"])

meu_dicionario["complexidade"] = ["I", "II", "III"]

print("inserido novo par de chave-valor no dicionário -> ", meu_dicionario)

novo_dicionario = defaultdict(list);
print("type novo_dicionario", type(novo_dicionario))

novo_dicionario["items"].extend(["consumiveis", "atributo", "equipamento", "diversos", "loja-secreta"])
print("novo_dicionario utilizando o módulo collections -> ", novo_dicionario)
print("localizando registro 1 da chave items -> ", novo_dicionario["items"][1])

#exercicios dicionario comprehension

minha_lista = ["tango", "sentinela-observadora", "sentinela-reveladora", "garrafa"]
novo_dicionario_comprehension_v1 = {len(item):item for item in minha_lista}
print("novo_dicionario_comprehension_v1 -> ", novo_dicionario_comprehension_v1)

minha_tupla = ("areia-da-revelação", "fragmento-de-aghanim", "fumaça-da-enganação")
novo_dicionario_comprehension_v2 = {item.split('-')[0]:item for item in minha_tupla}
print("novo_dicionario_comprehension_v2 -> ", novo_dicionario_comprehension_v2)

minha_lista_tuplas = [("consumiveis", "mango"), ("atributo", "machado-do-ogro"), ("equipamento", "claymore"), ("arcanos", "botas-de-velocidade")]
novo_dicionario_comprehension_v3 = {chave:valor for (chave, valor) in minha_lista_tuplas}
print("novo_dicionario_comprehension_v3 -> ", novo_dicionario_comprehension_v3)

novo_dicionario_comprehension_v4 = {chave*2: valor for (chave, valor) in novo_dicionario_comprehension_v3.items()}
print("novo_dicionario_comprehension_v4 -> ", novo_dicionario_comprehension_v4)

novo_dicionario_comprehension_v5 = {chave: valor for (chave, valor) in novo_dicionario_comprehension_v3.items() if len(chave) <= 3}
print("novo_dicionario_comprehension_v5 -> ", novo_dicionario_comprehension_v5)

novo_dicionario_comprehension_v6 = {chave: valor for (chave, valor) in novo_dicionario_comprehension_v3.items() if len(chave) <= 8}
print("novo_dicionario_comprehension_v6 -> ", novo_dicionario_comprehension_v6)

