input_number = input("Decimal Number: ")
test_number = 1
num_binary = 0
ready = False
final_binary = ""
on_run = True

while on_run:
    if not ready:
        if int(input_number) > test_number or int(input_number) == test_number:
            test_number = test_number * 2
            num_binary += 1
        else:
            ready = True

    if ready:

        if input_number != 0:
            if test_number != 1:
                test_number = test_number / 2
            if int(input_number) >= test_number:
                input_number = int(input_number) - test_number
                final_binary = final_binary + "1"
            else:
                final_binary = final_binary + "0"
        else:
            if len(final_binary) == num_binary:
                print(final_binary)
                on_run = False
            else:
                for i in range(num_binary - len(final_binary)):
                    final_binary = final_binary + "0"
                    print(f"Binary Number: {final_binary}")