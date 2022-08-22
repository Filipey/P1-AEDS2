import os
import random
import time

from funcionario import Funcionario, KeyId, generateRandomValues


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


def getFileSize(file_name):
    file = open(file_name + ".dat", "r")
    registersCount = 0
    byte = file.read(1)

    while byte:
      if byte == '#':
        registersCount += 1
      byte = file.read(1)

    file.close()
    return registersCount   


def readRegister(file_name, seek=0):
  file = open(file_name + ".dat", "rb")
  register = ""
  file.seek(seek)
  hashSeek = 1
  byte = file.read(1).decode()

  while byte:
    if byte == "#":
      hashSeek += len(register) + seek
      return register, hashSeek
    register += byte
    byte = file.read(1).decode()

  file.close()
  return register, hashSeek


def linearSearchEmployeeById(file_name, id):
    file = open(file_name + ".dat", "rb")
    print(f"Pesquisando o funcionário {id} por busca sequencial...")
    comparisons = 0
    byte = file.read(1).decode()
    savedRegister = ""
    field = ""
    searchId = bin(id)[2:]
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
                file.close()
                return savedRegister[:-1], comparisons, totalTime
            savedRegister = ""
            field = ""
        if byte == "|":
            field = ""

        byte = file.read(1).decode()
    file.close()
    return None, comparisons, time.time() - start


def keySorting(file_name: str, sorted_file_name):
    start = time.time()
    file = open(file_name + ".dat", "r")
    size = getFileSize(file_name)
    keys = [KeyId() for _ in range(size)]
    pos = 0
    offset = 0
    register = ""

    while pos < size:
      file.seek(offset)
      register, hashSeek = readRegister(file_name, offset)
      offset = hashSeek
      keys[pos].RRN = file.tell()
      id = int(register.split("|")[0], 2)
      keys[pos].id = id
      pos += 1
    
    aux = KeyId()
    for i in range(0, size):
      for j in range(i+1, size):
        if keys[i].id > keys[j].id:
          aux = keys[i]
          keys[i] = keys[j]
          keys[j] = aux

    file.seek(0, 0)

    sort_file = open(sorted_file_name + ".dat", "wb")
    print(f"Gerando arquivo ordenado...")
    for k in range(0, size):
      seek = file.seek(keys[k].RRN)
      register, _ = readRegister(file_name, seek)
      sort_file.write(register.encode() + "#".encode())

    file.close()
    sort_file.close()
    print(f"Tempo gasto para ordenação: {time.time() - start}")


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
    # print(f"Primeiro registro ao criar db: {readRegister(file)}")
    searchId = int(input("Digite um id para buscar no arquivo: \n"))
    register, comparisons, timer = linearSearchEmployeeById(file, searchId)
    formatRegister(register, comparisons, timer)
    sortedFile = input("Digite o nome do novo arquivo ordenado: ")
    keySorting(file, sortedFile)
    # print(f"Primeiro registro após ordenar arquivo: {readRegister(sortedFile)}")
