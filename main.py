KAPREKARS_CONSTANT = 6174
file_name = "kaprekars_routine.txt"
summary = "summary.txt"
file_it_1 = "iterations_1.txt"
file_it_2 = "iterations_2.txt"
file_it_3 = "iterations_3.txt"
file_it_4 = "iterations_4.txt"
file_it_5 = "iterations_5.txt"
file_it_6 = "iterations_6.txt"
file_it_7 = "iterations_7.txt"
less_than_4_digits = "all_numbers_with_less_than_4_digits.txt"
def get_bigger_number(numbers):
    number_digits_copy = numbers.copy()
    descending_order = []
    while True:
        if not number_digits_copy:
            break
        biggest_number = max(number_digits_copy)
        descending_order.append(biggest_number)
        number_digits_copy.remove(biggest_number)
    if len(descending_order) < 4:
        descending_order.append(0)
    bigger_number = ""
    for number in descending_order:
        bigger_number += str(number)
    return int(bigger_number)
def get_smaller_number(numbers):
    number_digits_copy = numbers.copy()
    ascending_order = []
    while True:
        if not number_digits_copy:
            break
        smallest_number = min(number_digits_copy)
        ascending_order.append(smallest_number)
        number_digits_copy.remove(smallest_number)
    smaller_number = ""
    for number in ascending_order:
        smaller_number += str(number)
    return int(smaller_number)

iterations_result_is_0 = 0
iterations_1 = 0
iterations_2 = 0
iterations_3 = 0
iterations_4 = 0
iterations_5 = 0
iterations_6 = 0
iterations_7 = 0
numbers_less_than_4_digits = 0
iterations_more = 0
with open(file_name, "w") as f:
    number = 1000
    while number <= 9999:
        with open(less_than_4_digits, "a") as l:
            l.write(f"Observing number:{number}:\n")
        iterations = 0
        number_digits = []
        copy = number 
        while copy != 0:
            digit = copy % 10
            number_digits.append(digit)
            copy //= 10
        f.write(f"Observing number: {number}\n")
        result = 0
        is_result_zero = False
        bigger_number = get_bigger_number(number_digits)
        smaller_number = get_smaller_number(number_digits)
        while True:
            result = bigger_number - smaller_number
            f.write(f"{bigger_number} - {smaller_number} = {result}\n")
            if result < 1000:
                numbers_less_than_4_digits += 1
                with open(less_than_4_digits, "a") as l:
                    l.write(f"{bigger_number} - {smaller_number} = {result}\n")
            if result == KAPREKARS_CONSTANT:
                iterations += 1
                break
            if result == 0:
                iterations += 1
                is_result_zero = True
                break
            result_digits = []
            while result != 0:
                digit = result % 10
                result_digits.append(digit)
                result //= 10
            bigger_number = get_bigger_number(result_digits)
            smaller_number = get_smaller_number(result_digits)
            iterations += 1
        if is_result_zero:
            f.write(f"Iterations to get to 0: {iterations}\n\n")
            iterations_result_is_0 += 1
        else:
            f.write(f"Iterations to get to {KAPREKARS_CONSTANT}: {iterations}\n\n")
            if iterations == 1:
                with open(file_it_1, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_1 += 1
            elif iterations == 2:
                with open(file_it_2, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_2 += 1
            elif iterations == 3:
                with open(file_it_3, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_3 += 1
            elif iterations == 4:
                with open(file_it_4, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_4 += 1
            elif iterations == 5:
                with open(file_it_5, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_5 += 1
            elif iterations == 6:
                with open(file_it_6, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_6 += 1
            elif iterations == 7:
                with open(file_it_7, "a") as g:
                    g.write(f"{number}\n\n")
                iterations_7 += 1
            else:
                iterations_more += 1
        number += 1
iterations_6_copy = iterations_6
iterations_1_copy = iterations_1
iterations_7_copy = iterations_7
iterations_4_copy = iterations_4
counter = 0
while True:
    counter += 1
    iterations_6_copy -= 1
    iterations_1_copy -= 1
    iterations_7_copy -= 1
    iterations_4_copy -= 1
    if iterations_6_copy == 0 or iterations_1_copy == 0 or iterations_7_copy == 0 or iterations_4_copy == 0:
        break
with open(summary, "w") as f:
    f.write("SUMMARY ON KAPREKAR'S ROUTINE:\n")
    f.write(f"Amount of numbers that did not reach Kaprekar's Constant (result is zero): {iterations_result_is_0}\n")
    f.write(f"Amount of numbers that took 1 iteration to reach Kaprekar's Constant: {iterations_1}\n")
    f.write(f"Amount of numbers that took 2 iterations to reach Kaprekar's Constant: {iterations_2}\n")
    f.write(f"Amount of numbers that took 3 iterations to reach Kaprekar's Constant: {iterations_3}\n")
    f.write(f"Amount of numbers that took 4 iterations to reach Kaprekar's Constant: {iterations_4}\n")
    f.write(f"Amount of numbers that took 5 iterations to reach Kaprekar's Constant: {iterations_5}\n")
    f.write(f"Amount of numbers that took 6 iterations to reach Kaprekar's Constant: {iterations_6}\n")
    f.write(f"Amount of numbers that took 7 iterations to reach Kaprekar's Constant: {iterations_7}\n")
    f.write(f"Amount of numbers that took 8 or more iterations to reach Kaprekar's Constant: {iterations_more}\n\n")
    f.write(f"Results during the Kaprekar's Routine that are not 4 digit numbers: {numbers_less_than_4_digits}\n")
    f.write(f"Out of the given number of iterations, we can write theKaprekar's Constant {counter} times.\n")
