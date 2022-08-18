import random
import string


class Funcionario:
  cod: int
  nome: str
  cpf: str
  data_nascimento: str
  salario: float

def generateRandomValues(f: Funcionario, idCounter: int):
  f.cod = idCounter
  f.nome = "".join(random.choice(string.ascii_lowercase) for _ in range(50))
  f.cpf = "".join(str(random.randint(0, 9)) for _ in range(15))
  f.cpf = formatCpf(f.cpf)
  f.data_nascimento = "".join(str(random.randint(0, 9)) for _ in range(11))
  f.data_nascimento = formatBirthdayDate(f.data_nascimento)
  f.salario = round(random.uniform(1, 10000), 2)

def formatBirthdayDate(date: str):
  formattedDate = date[0:2] + "/" + date[3:5] + "/" + date[6:10]
  return formattedDate

def formatCpf(cpf: str):
  formattedCpf = cpf[0:3] + "." + cpf[4:7] + "." + cpf[7:10] + "-" + cpf[11:13]
  return formattedCpf
