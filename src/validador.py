import re

# Conjunto de REGEX para validação de entradas.

#def validar_email(email):
exprEmail = re.compile('/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/')
email = input("Digite um email): ")

if exprEmail.search(email):
  print(f"{email} é válido")
else:
  print(f"{email} é inválido")
  
#def validar_cep(cep):
exprCep = re.compile('/^[0-9]{5}-[0-9]{3}$/')
cep = input("Digite um CEP: ")

if exprCep.search(cep):
  print(f"{cep} é válido")
else:
  print(f"{cep} é inválido")
  
#def validar_cpf(cpf):
exprCpf = re.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
cpf = input("Digite um CPF válido (utilize pontos e traço): ")

if exprCpf.search(cpf):
  print(f"{cpf} é válido")
else:
  print(f"{cpf} é inválido")
  
#def validar_telefone(telefone):  
exprTel = re.compile('/[0-9]{2}-([0-9]{8}|[0-9]{9})$/')
tel = input("Digite um Telefone: ")

if exprTel.search(tel):
  print(f"{tel} é válido")
else:
  print(f"{tel} é inválido")
