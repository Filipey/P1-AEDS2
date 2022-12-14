import os
import random
import time

from employee import Employee, KeyId, generateRandomValues


def generateBinaryDatabase(file_name: str):
  try:
    i = 0
    ids = [i for i in range(100)]
    file = open(file_name + ".dat", "wb")

    while i < 100:
      e = Employee()
      id = random.choice(ids)
      ids.remove(id)
      generateRandomValues(e, id)
      file.write(bin(e.id)[2:].encode())
      file.write("|".encode())
      file.write(e.name.encode())
      file.write("|".encode())
      file.write(e.cpf.encode())
      file.write("|".encode())
      file.write(e.birthday_date.encode())
      file.write("|".encode())
      file.write(str(e.salary).encode())
      file.write("#".encode())
      i += 1

  except IOError:
    print(IOError)
    exit(1)
  print("Base de dados gerada com sucesso!\n")
  print("Foram gerados registros com Ids de 0 a 99")
  file.close()


def getFileSize(file_name):
    file = open(file_name + ".dat", "r")
    registers_count = 0
    byte = file.read(1)

    while byte:
      if byte == '#':
        registers_count += 1
      byte = file.read(1)

    file.close()
    return registers_count   


def getSpecificRegister(file_name, register_number):
  file = open(file_name + ".dat", "rb")
  register_count = 0
  byte = file.read(1).decode()
  register = ""
  finded = False
  field = ""

  while register_count <= register_number:
    register += byte
    field += byte
    if field == bin(register_number)[2:] + "|":
      finded = True
    
    if byte == "#":
      register_count += 1
      if finded:
        file.close()
        return register[:-1]
      register = ""
      field = ""
    if byte == "|":
      field = ""
    byte = file.read(1).decode()
  
  file.close()
  return register


def getRegisterToMemory(file_name):
  file = open(file_name + ".dat", "rb")
  registers = []
  size = getFileSize(file_name)
  counter = 0
  byte = file.read(1).decode()
  register = ""

  while counter < size:
    if byte == "#":
      id, name, cpf, birthday_date, salary = register.split("|")
      e = Employee()
      e.id = int(id.replace("#", ""), 2)
      e.name = name
      e.cpf = cpf
      e.birthday_date = birthday_date
      e.salary = salary
      registers.append(e)
      register = ""
      counter += 1
    register += byte
    byte = file.read(1).decode()
  return registers


def readRegister(file_name, seek=0):
  file = open(file_name + ".dat", "rb")
  register = ""
  file.seek(seek)
  hash_seek = 1
  byte = file.read(1).decode()

  while byte:
    if byte == "#":
      hash_seek += len(register) + seek
      return register, hash_seek
    register += byte
    byte = file.read(1).decode()

  file.close()
  return register, hash_seek


def linearSearchEmployeeById(file_name, id):
  start = time.perf_counter()
  file = open(file_name + ".dat", "rb")
  print(f"Pesquisando o funcion??rio {id} por busca sequencial...")
  comparisons = 0
  byte = file.read(1).decode()
  saved_register = ""
  field = ""
  search_id = bin(id)[2:]
  finded = False

  while byte:
    field += byte
    saved_register += byte
    if field == search_id + "|":
      finded = True
      if byte == "#":
        comparisons += 1
        if finded:
          total_time = time.perf_counter() - start
          file.close()
          return saved_register[:-1], comparisons, total_time
        saved_register = ""
        field = ""
      if byte == "|":
        field = ""

    byte = file.read(1).decode()
  file.close()
  return None, comparisons, time.perf_counter() - start

def binarySearch(file_name, id):
  file = open(file_name + ".dat", "rb")
  comparisons = 0
  left = 0
  right = getFileSize(file_name) - 1
  file.seek(0, 0)
  register = ""
  start = time.perf_counter()
  
  while left <= right:
    middle = int((left + right) // 2)
    register = getSpecificRegister(file_name, middle)
    register_id = int(register.split("|")[0], 2)
    
    if id == register_id:
      comparisons += 1
      return register, comparisons, time.perf_counter() - start
    elif register_id < id:
      comparisons += 1
      left = middle + 1
    else:
      comparisons += 1
      right = middle - 1

  return None, comparisons, time.perf_counter() - start

def insertionSortMemory(file_name):
  try:
    os.remove(file_name + "_ordenado" + ".dat") # evitando duplicidade de arquivos
  except:
    pass
  start = time.perf_counter()
  registers = getRegisterToMemory(file_name)
  file = open(file_name + ".dat", "wb")

  registers.sort(key= lambda x: x.id)

  for register in registers:
    file.write(bin(register.id)[2:].encode())
    file.write("|".encode())
    file.write(register.name.encode())
    file.write("|".encode())
    file.write(register.cpf.encode())
    file.write("|".encode())
    file.write(register.birthday_date.encode())
    file.write("|".encode())
    file.write(str(register.salary).encode())
    file.write("#".encode())

  file.close()
  os.rename(file_name + ".dat", file_name + "_ordenado" + ".dat")
  print(f"Tempo gasto para ordena????o: {time.perf_counter() - start}s")

def keySorting(file_name: str):
  try:
    os.remove(file_name + "_ordenado" + ".dat") # evitando duplicidade de arquivos
  except:
    pass
  
  start = time.perf_counter()
  file = open(file_name + ".dat", "r")
  size = getFileSize(file_name)
  keys = [KeyId() for _ in range(size)]
  pos = 0
  offset = 0
  register = ""

  while pos < size:
    file.seek(offset)
    register, hash_seek = readRegister(file_name, offset)
    offset = hash_seek
    keys[pos].RRN = file.tell()
    id = int(register.split("|")[0], 2)
    keys[pos].id = id
    pos += 1
    
  keys.sort(key=lambda x: x.id)

  file.seek(0, 0)

  sort_file = open(file_name + "_ordenado" + ".dat", "wb")
  print("\nQuest??o 03 - Gerando arquivo ordenado...")
  for k in range(0, size):
    seek = file.seek(keys[k].RRN)
    register, _ = readRegister(file_name, seek)
    sort_file.write(register.encode() + "#".encode())

  file.close()
  os.remove(file_name + ".dat")
  sort_file.close()
  print(f"Tempo gasto para ordena????o: {time.perf_counter() - start}s")

def formatRegister(register: str, comparisons: int, time):
  if register is None:
    print("N??o foi encontrado nenhum funcion??rio com esse Id.")
    print(f"O total de compara????es foi {comparisons}, e o tempo gasto foi {time}s")
    return

  fields = register.split("|")
  id, name, cpf, birthday_date, salary = fields

  print("Funcion??rio encontrado:\n")
  print(
      f"C??digo: {int(id, 2)}"
      f"\nNome: {name}"
      f"\nCPF: {cpf}"
      f"\nData de Anivers??rio: {birthday_date}"
      f"\nSal??rio: {salary}"
      f"\nCompara????es: {comparisons}"
      f"\nTempo gasto: {time}s")
