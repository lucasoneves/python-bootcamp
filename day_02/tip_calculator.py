# Tip Calculator

# 1-Pegar o valor total da conta
# 2-Qual a porcentagem da gorjeta?
# 3-Quantas pessoas vão dividir a conta?
# 4-Imprimir quanto cada pessoa vai pagar

greeting = "Welcome to the tip calculator";
print(greeting);

total_price = float(input("Digite o total da conta: "));
tip_percentage = float(input("Digite a porcentagem da gorjeta: "));
total_people = int(input("Quantas pessoas vão dividir a conta: "));

final_price = total_price;
tip_final_price = tip_percentage / 100
final_price += round(total_price * tip_final_price, 2)
price_per_person = round(final_price / total_people, 2);


print(f"Preço final: ${final_price}")
print(f"Valor por pessoa: ${price_per_person}")
