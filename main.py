import random
import time

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


def linearSearchEmployeeById(file_name):
    file = open(file_name + ".dat", "rb")
    comparisons = 0
    byte = file.read(1).decode()
    savedRegister = ""
    field = ""
    searchId = bin(int(input("\nForam gerados ids de 0 a 99. Digite um id para pesquisar: ")))[2:]
    start = time.time()
    founded = False

    while byte:
        field += byte
        savedRegister += byte
        if field == searchId + "|":
            founded = True
        if byte == "#":
            comparisons += 1
            if founded:
                totalTime = time.time() - start
                return savedRegister[:-1], comparisons, totalTime
            savedRegister = ""
            field = ""
        if byte == "|":
            field = ""

        byte = file.read(1).decode()
    return None, comparisons, time.time() - start

def readEmployee(file_name):
    file = open(file_name + ".dat", "rb")
    register = file.read().split("|")

    for field in register:
        print(field)


def binarySearchEmployeeById(file_name, id):
    searchId = input("Buscando o mesmo funcionário por busca binária: \n")
    file = open(file_name + ".dat", "rb")
    left = 0
    right = len(file)

    while left < right:
        middle = (left + right) // 2
        file.seek(middle * 84)
        readEmployee(file_name)


def formatRegister(register: str, comparisons: int, time):
    if register is None:
      print("Não foi encontrado nenhum funcionário com esse Id.")
      print(f"O total de comparações foi {comparisons}, e o tempo gasto foi {time}s")
      return

    fields = register.split("|")
    [id, name, cpf, birthday_date, salary] = fields

    print("\nFuncionário encontrado:\n")
    print(
        f"Código: {int(id, 2)}"
        f"\nNome: {name}"
        f"\nCPF: {cpf}"
        f"\nData de Aniversário: {birthday_date}"
        f"\nSalário: {salary}"
        f"\nComparações: {comparisons}"
        f"\nTempo gasto: {time}s")


if __name__ == "__main__":
    file = input("Digite o nome do arquivo binário: ")
    generateBinaryDatabase(file)
    register, comparisons, timer = linearSearchEmployeeById(file)
    formatRegister(register, comparisons, timer)
