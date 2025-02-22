#Write a function that takes a temperature in Celsius and converts it to Fahrenheit using the formula: 𝐹 = (𝐶×9/5)+32

def farenheit_calculator(celsius):
	return f"{celsius}C is equal to {(celsius * 9 / 5) + 32}F"

result = farenheit_calculator(100)
print(result)

