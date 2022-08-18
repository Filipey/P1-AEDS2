from funcionario import Funcionario, generateRandomValues

i = 0
idCounter = 0

while i < 5:
  f = Funcionario()
  generateRandomValues(f, idCounter)
  print(f"Id: {f.cod}\nNome: {f.nome}\nCPF: {f.cpf}\nData de nascimento: {f.data_nascimento}\nSalário: {f.salario}")
  print("-----------------------------------")
  i += 1
  idCounter += 1
