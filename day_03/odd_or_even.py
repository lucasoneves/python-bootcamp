# CHeck Odd or Even

input_number = int(input("Digite um número qualquer: "))

type_number = "ímpar" if input_number % 2 == 0 else "par"

message = f"o número {input_number} é {type_number}"

print(message)