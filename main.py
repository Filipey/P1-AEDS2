import time

from utils import *


def menu():
  print("Prova 01 - AEDS 2 (CSI104) - Filipe Augusto Santos de Moura (20.2.8079)")
  
  file = input("Questão 01 - Digite o nome para a base de dados: ")
  generateBinaryDatabase(file)
  search_id = int(input("Questão 02 - Digite um id para buscar um funcionário no arquivo, de forma sequencial: \n"))
  register, comparisons, timer = linearSearchEmployeeById(file, search_id)
  formatRegister(register, comparisons, timer)
  time.sleep(2)
  keySorting(file)
  time.sleep(2)
  print("\nQuestão 04 - Agora com o arquivo ordenado, será buscado o mesmo funcionário via Busca Binária: ")
  binary_register, binary_comparisons, binary_timer = binarySearch(file + "_ordenado", search_id)
  formatRegister(binary_register, binary_comparisons, binary_timer)

if __name__ == "__main__":
  menu()
