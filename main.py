import random

from funcionario import Funcionario, generateRandomValues


def generateBinaryDatabase(file_name: str):
    try:
        i = 0
        ids = [i for i in range(100)]
        file = open(file_name + ".dat", "wb")

        while i < 100:
            f = Funcionario()
            id = random.choice(ids)
            ids.remove(id)
            generateRandomValues(f, id)
            file.write(bin(f.cod)[2:].encode())
            file.write("|".encode())
            file.write(f.nome.encode())
            file.write("|".encode())
            file.write(f.cpf.encode())
            file.write("|".encode())
            file.write(f.data_nascimento.encode())
            file.write("|".encode())
            file.write(str(f.salario).encode())
            file.write("#".encode())
            i += 1

    except IOError:
        print(IOError)
        exit(1)
    print("\nBase de dados gerada com sucesso!")
    file.close()

def LinearSearchEmployeeById(file_name):
    file = open(file_name + ".dat")
    byte = file.read(1)
    savedRegister = ""
    field = ""
    searchId = bin(int(input("\nForam gerados ids de 0 a 99. Digite um id para pesquisar: ")))[2:]
    founded = False

    while byte:
        field += byte
        savedRegister += byte
        if field == searchId + "|":
          founded = True
        if byte == "#":
          if founded:
            return savedRegister[:-1]
          savedRegister = ""
          field = ""
        if byte == "|":
          field = ""
        
        byte = file.read(1)

def formatRegister(register: str):
  fields = register.split("|")
  id = fields[0]
  name = fields[1]
  cpf = fields[2]
  birthday_date = fields[3]
  salary = fields[4]

  print("\nFuncionário encontrado:\n")
  print(f"Código: {int(id, 2)}\nNome: {name}\nCPF: {cpf}\nData de Aniversário: {birthday_date}\nSalário: {salary}")


if __name__ == "__main__":
    file = input("Digite o nome do arquivo binário: ")
    generateBinaryDatabase(file)
    register = LinearSearchEmployeeById(file)
    formatRegister(register)
