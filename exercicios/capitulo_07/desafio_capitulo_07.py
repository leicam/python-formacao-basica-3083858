#exercicio tratamento de exceção

try:
    print(10/0)
except ZeroDivisionError:
    print("Divisão por zero inválida!")
except TypeError:
    print("Erro de sintaxe contate o suporte!")
except:
    print("Erro genérico detectado!")
finally:
    print("Programa encerrado!")

#exercicio customizacao de excecao
class HttpException(Exception):
    status_code = None
    message = None

    def __init__(self):
        super().__init__(f"Código de Status: {self.status_code}. Mensagem: {self.message}")

class BadRequest(HttpException):
    status_code = 400
    message = "O servidor não pode ou não processará a solicitação devido a algo que é percebido como um erro do cliente."

class ContentTooLarge(HttpException):
    status_code = 413
    message = "O corpo da solicitação é maior que os limites definidos pelo servidor. O servidor pode fechar a conexão ou retornar um campo de cabeçalho Retry-After."


def GerarContentTooLarge():
    raise ContentTooLarge

try:
    GerarContentTooLarge()
except HttpException as ex:
    print(ex.message)
except Exception:
    print("Erro genérico detectado!")
finally:
    print("Programa encerrado!")