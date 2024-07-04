input_number = input("Binary Number: ")
length_input_number = len(input_number)
final_number = 0

for x in range(length_input_number):
    now_number = input_number[-1 - x]
    now_number_int = int(now_number)
    final_number += now_number_int * (2 ** x)

print("Decimal Number:", final_number)