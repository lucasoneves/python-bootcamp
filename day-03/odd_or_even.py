# CHeck Odd or Even

input_number = int(input("Digite um número qualquer: "))

type_number = "ímpar" if input_number % 2 == 0 else "par"

message = f"o número {input_number} é {type_number}"

if input_number % 2 == 0:
    print(f"o número {input_number} é par")
else: print(f"O número {input_number} é impar");