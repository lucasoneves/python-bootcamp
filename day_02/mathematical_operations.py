# Calculate the BMI

user_height = float(input("Type your height: "));
user_weight = float(input("Type your weight: "));
user_height_converted = float(user_height ** 2);

bmi = round(user_weight / user_height_converted, 2);
message = "Your bmi is " + str(bmi); 
print(message);