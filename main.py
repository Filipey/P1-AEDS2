import random

from funcionario import Funcionario, generateRandomValues

i = 0
ids = [i for i in range(100)]

while i < 100:
  f = Funcionario()
  id = random.choice(ids)
  ids.remove(id)
  generateRandomValues(f, id)
  i += 1
