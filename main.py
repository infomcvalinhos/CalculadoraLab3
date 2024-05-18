def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def mult(x,y):
  return x * y

def div(x,y):
  return x / y

print("Selecione uma operação.")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha uma opção (1,2,3,4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))

if escolha == '1':
  print(f"{n1} + {n2} = {add(n1,n2)}")

if escolha == '2':
  print(f"{n1} - {n2} = {sub(n1,n2)}")

if escolha == '3':
  print(f"{n1} * {n2} = {mult(n1,n2)}")

if escolha == '4':
  if n2 != 0:
    print(f"{n1} / {n2} = {div(n1,n2)}")
  else:
    print("Erro: divisão por zero.")

else:
  print("Escolha inválida. Por favor, escolha entre 1 a 4")