# 1- Opção para o usuário "encode" ou "decode"
# 2- Usuário digita a mensagem
# 3- Usuário escolhe a quantidade de letras para codificar.
# 4- Retorna a palavra codificada.
# 5- O número de letras é contado a partir da letra do alfabeto: Ex: 4 letras e a letra é A -> (A, b, c, d, e): A nova letra é D

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operation = input("Digite 'encode' para codificar ou 'decode' para descodificar \n").lower()

def check_operation_valid():
  if operation != 'encode' and operation != 'decode':
    print("Operação não reconhecida!")
    return False

def encrypt(original_text, shift_amount):
  word_encrypt = ''
  
  for letter in original_text:
    index = alphabet.index(letter)
    new_index = index + shift_amount    
    word_encrypt += alphabet[new_index]
  
  return word_encrypt
  
if not check_operation_valid():
  user_message = input("Digite o texto desejado: \n").lower()
  shift_number = int(input("Quantas letras quer para contar? \n"))

    # should print 11 8 15 15 18
  print(encrypt(user_message, shift_number))