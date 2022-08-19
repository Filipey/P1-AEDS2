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
            if i == 0:
                print("criou id 33")
                id = 33
            generateRandomValues(f, id)
            file.write(bin(f.cod).encode())
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
    print("Base de dados gerada com sucesso!")
    file.close()


def searchLinearEmployeeById(id: int, file_name):
    file = open(file_name + ".dat")
    byte = file.read(1)
    savedRegister = []

    while byte:
        if byte != "#":
            savedRegister.append(byte)
        if byte == bin(id):
            break
        byte = file.read(1)


if __name__ == "__main__":
    file = input("Digite o nome do arquivo binário\n")
    generateBinaryDatabase(file)
    searchLinearEmployeeById(33, file)
