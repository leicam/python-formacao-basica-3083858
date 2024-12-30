import math

#exercicios funcoes
def calcular(valorUm, valorDois, operacao) :
    if operacao == "soma" :
        return sum([valorUm, valorDois])
    elif operacao == "subtração" :
        return valorUm - valorDois
    elif operacao == "multiplicação" :
        return math.prod([valorUm, valorDois])
    elif operacao == "divisão" :
        return valorUm / valorDois
    else:
        return "Operação inválida"
    
print("soma 2 + 2 = ", calcular(2, 2, "soma"))
print("subtração 2 - 2 = ", calcular(2, 2, "subtração"))
print("multiplicação 2 * 2 = ", calcular(2, 2, "multiplicação"))
print("divisão 2 / 2 = ", calcular(2, 2, "divisão"))

def testeArgumentosNaoPrevisiveis(*args) : 
    print(args)

testeArgumentosNaoPrevisiveis(20, 13, 14, 25, 27)

somar = lambda valorUm, valorDois : print(f"soma {valorUm} + {valorDois} = {valorUm + valorDois}")
subtrair = lambda valorUm, valorDois : print(f"subtração {valorUm} - {valorDois} = {valorUm - valorDois}")
multiplicar = lambda valorUm, valorDois : print(f"multiplicação {valorUm} * {valorDois} = {valorUm * valorDois}")
dividir = lambda valorUm, valorDois : print(f"divisão {valorUm} / {valorDois} = {valorUm / valorDois}")

somar(3, 3)
subtrair(3, 3)
multiplicar(3, 3)
dividir(3, 3)

#exercicios decoradores

def descontGerente(valorBase) :
    return valorBase * 0.10

def descontoVendedor(valorBase) :
    return valorBase * 0.05

def descontoPromocaoClienteExclusivo(valorBase) :
    return valorBase * 0.20

def aplicarDesconto(valorBase, funcaoDesconto) :
    return valorBase - funcaoDesconto(valorBase)

print(f"desconto vendedor | venda de R$ 120.00 | venda com desconto R${aplicarDesconto(120.00, descontoVendedor)}")
print(f"desconto gerente | venda de R$ 120.00 | venda com desconto R${aplicarDesconto(120.00, descontGerente)}")
print(f"desconto promoção cliente exclusivo | venda de R$ 120.00 | venda com desconto R${aplicarDesconto(120.00, descontoPromocaoClienteExclusivo)}")

#region exercicios classes
class REGISTRO_I200:
    _registro = "I200"

    def __init__(self, numero_lancamento, data_lancamento, valor_lacamento) :
        self.numero_lancamento = numero_lancamento
        self.data_lancamento = data_lancamento
        self.valor_lancamento = valor_lacamento
    
    def getRegistro(self) :
        return self._registro
    
i200 = REGISTRO_I200("17903", "2022-06-30 00:00:00.0000000", 81191.24)

print("Registro:", i200.getRegistro())
print("Número lançamento:", i200.numero_lancamento)
print("Data lançamento:", i200.data_lancamento)
print("Valor lançamento: R$", i200.valor_lancamento)

#exercicios metodo classe
class REGISTRO_I250 :
    _registro = "I250"
    _codigo_conta = ""
    _valor_documento = 0.0
    _indicador = ""

    def __init__(self, codigo_conta, valor_documento, indicador) :
        self._codigo_conta = codigo_conta
        self._valor_documento = valor_documento
        self._indicador = indicador

    def getRegistro(self) :
        return self._registro
    
    def getCodigoConta(self) :
        return self._codigo_conta
    
    def setCodigoConta(self, codigo_conta) :
        self._codigo_conta = codigo_conta
    
    def getValorDocumento(self) :
        return self._valor_documento
    
    def setValorDocumento(self, valor_documento) :
        self._valor_documento = valor_documento
    
    def getIndicador(self) :
        return self._indicador
    
    def setIndicador(self, indicador) :
        self._indicador = indicador

i250 = REGISTRO_I250("2105010027", 711.18, "D")

print("Pré alterações por metodos set")
print("Registro:", i250.getRegistro())
print("Código conta:", i250.getCodigoConta())
print("Valor lançamento: R$", i250.getValorDocumento())
print("Indicador lançamento:", i250.getIndicador())

i250.setCodigoConta("1101020002")
i250.setValorDocumento("69765.41")
i250.setIndicador("C")

print("Pós alterações por metodos set")
print("Registro:", i250.getRegistro())
print("Código conta:", i250.getCodigoConta())
print("Valor lançamento: R$", i250.getValorDocumento())
print("Indicador lançamento:", i250.getIndicador())