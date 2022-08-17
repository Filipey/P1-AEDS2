import random
import string


class Funcionario:
  cod: int
  nome: str
  cpf: str
  data_nascimento: str
  salario: float

  def __init__(self, cod, nome, cpf, data_nascimento, salario):
    self.cod = cod
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
    self.salario = salario

  def setRandomValues():
    self.nome = ''.join(random.choices(string.ascii_letters) for _ in range(50))
    self.cpf= ''.join(random.choices(_ for _ in range(15)))
    

