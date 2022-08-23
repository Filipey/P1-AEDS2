import random
import string


class Employee:
  id: int # 4 bytes
  name: str # 50 bytes
  cpf: str # 15 bytes
  birthday_date: str # 11 bytes
  salary: float # 4 bytes


class KeyId:
  id: int
  RRN: int

def generateRandomValues(e: Employee, id: int):
  e.id = id
  e.name = "".join(random.choice(string.ascii_lowercase) for _ in range(50))
  e.cpf = formatCpf("".join(str(random.randint(0, 9)) for _ in range(15)))
  e.birthday_date = formatBirthdayDate("".join(str(random.randint(0, 9)) for _ in range(11)))
  e.salary = round(random.uniform(1, 10000), 2)

def formatBirthdayDate(date: str):
  formattedDate = date[0:2] + "/" + date[3:5] + "/" + date[6:10]
  return formattedDate

def formatCpf(cpf: str):
  formattedCpf = cpf[0:3] + "." + cpf[4:7] + "." + cpf[7:10] + "-" + cpf[11:13]
  return formattedCpf
