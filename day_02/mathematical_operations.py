# Calculate the BMI

user_height = float(input("Type your height: "));
user_weight = float(input("Type your weight: "));
user_height_converted = float(user_height ** 2);

bmi = round(user_weight / user_height_converted, 2);
message = f"Your bmi is {bmi}"; 
print(message);