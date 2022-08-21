import random
import string


class Funcionario:
  cod: int # 4 bytes
  nome: str # 50 bytes
  cpf: str # 15 bytes
  data_nascimento: str # 11 bytes
  salario: float # 4 bytes


class KeyId:
  id: int
  RRN: int

def generateRandomValues(f: Funcionario, id: int):
  f.cod = id
  f.nome = "".join(random.choice(string.ascii_lowercase) for _ in range(50))
  f.cpf = formatCpf("".join(str(random.randint(0, 9)) for _ in range(15)))
  f.data_nascimento = formatBirthdayDate("".join(str(random.randint(0, 9)) for _ in range(11)))
  f.salario = round(random.uniform(1, 10000), 2)

def formatBirthdayDate(date: str):
  formattedDate = date[0:2] + "/" + date[3:5] + "/" + date[6:10]
  return formattedDate

def formatCpf(cpf: str):
  formattedCpf = cpf[0:3] + "." + cpf[4:7] + "." + cpf[7:10] + "-" + cpf[11:13]
  return formattedCpf
