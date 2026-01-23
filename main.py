KAPREKARS_CONSTANT = 6174
iterations = 0
number = 1111

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

number_digits = []
copy = number 
while copy != 0:
    digit = copy % 10
    number_digits.append(digit)
    copy //= 10

result = 0
is_result_zero = False
bigger_number = get_bigger_number(number_digits)
smaller_number = get_smaller_number(number_digits)
while True:
    result = bigger_number - smaller_number
    print(f"{bigger_number} - {smaller_number} = {result}")
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
    print(f"Iterations to get to 0: {iterations}")
else:
    print(f"Iterations to get to {KAPREKARS_CONSTANT}: {iterations}")
