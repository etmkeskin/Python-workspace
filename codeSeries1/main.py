print("\n----Task 1---- BMI Calculator")

name = input("Name: ").strip().title()
weight_in_kilograms = float(input("Weight (kg): "))
height_in_centimeters = float(input("Height (cm): "))

height_in_meters = float(height_in_centimeters) / 100
BMI = float(weight_in_kilograms / height_in_meters ** 2)

print("Name: {} Weight: {:.2f} Height [meters]: {:.2f} BMI: {:.2f} ".format(name, weight_in_kilograms, height_in_meters, BMI))

print("\n----Task 2---- Leetspeak Converter")

task2 = input("Type a long string: ").strip().upper().replace("T", "+").replace("A", "@").replace("E", "3").replace("I",
                                                                                                                    "|").replace(
    "B", "8").replace("O", "0").replace("C", "[").replace("S", "5")

print(task2)

print("\n----Task 3---- Flipping String")

str = input("Input a long string: ")
length_of_the_string = len(str)
middle_character = length_of_the_string // 2

start = str.upper()[middle_character:]
end = str.upper()[0:middle_character]
flipped_str = start + "|" + end

print(f"This string is {length_of_the_string} characters long. The middle character is \'{str[middle_character]}\'\nFlipped String\n{flipped_str}")

print("\n----Task 4---- Multiple numbers")

inputStr = input("Input numbers to multiply: ")

inputStr = inputStr.replace(" ", "")

separatorIndex = inputStr.find("*")
number1 = int(inputStr[:separatorIndex])
number2 = int(inputStr[separatorIndex + 1:])
outputStr = number1 * number2

print("Extracted numbers: " + inputStr[:separatorIndex] + " " + inputStr[separatorIndex + 1:])
print(f"{number1} * {number2} = {outputStr}")

input("Press enter to exit. ")  # input statement to pause code when finished
