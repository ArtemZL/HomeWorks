def strip_leading_zeros(number):
    return number.lstrip('0') or '0'

def add_strings(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        carry = total // 10
        result.append(str(total % 10))

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


def subtract_strings(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    borrow = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        diff = int(num1[i]) - int(num2[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))

    return strip_leading_zeros(''.join(result[::-1]))


def multiply_strings(num1, num2):
    num1 = strip_leading_zeros(num1)
    num2 = strip_leading_zeros(num2)

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum_ = mul + result[i + j + 1]
            result[i + j + 1] = sum_ % 10
            result[i + j] += sum_ // 10

    result_str = ''.join(map(str, result)).lstrip('0')

    return result_str or '0'


def divide_strings(num1, num2):
    if num2 == '0':
        raise ZeroDivisionError("Division by zero")

    num1 = strip_leading_zeros(num1)
    num2 = strip_leading_zeros(num2)

    quotient = []
    remainder = '0'

    for digit in num1:
        remainder = strip_leading_zeros(remainder + digit)
        q_digit = 0
        while compare_strings(remainder, num2) >= 0:
            remainder = subtract_strings(remainder, num2)
            q_digit += 1
        quotient.append(str(q_digit))

    quotient_str = strip_leading_zeros(''.join(quotient))

    return quotient_str or '0'


def compare_strings(num1, num2):
    num1 = strip_leading_zeros(num1)
    num2 = strip_leading_zeros(num2)

    if len(num1) > len(num2):
        return 1
    if len(num1) < len(num2):
        return -1

    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return 1
        if num1[i] < num2[i]:
            return -1

    return 0


def add(num1, num2):
    if num1[0] == '-' and num2[0] == '-':
        return '-' + add_strings(num1[1:], num2[1:])
    elif num1[0] == '-':
        return subtract(num2, num1[1:])
    elif num2[0] == '-':
        return subtract(num1, num2[1:])
    else:
        return add_strings(num1, num2)


def subtract(num1, num2):
    if num1 == num2:
        return '0'
    if num1[0] == '-' and num2[0] == '-':
        return subtract(num2[1:], num1[1:])
    elif num1[0] == '-':
        return '-' + add_strings(num1[1:], num2)
    elif num2[0] == '-':
        return add(num1, num2[1:])
    else:
        if compare_strings(num1, num2) < 0:
            return '-' + subtract_strings(num2, num1)
        else:
            return subtract_strings(num1, num2)


def multiply(num1, num2):
    if (num1[0] == '-' and num2[0] != '-') or (num1[0] != '-' and num2[0] == '-'):
        return '-' + multiply_strings(num1.lstrip('-'), num2.lstrip('-'))
    else:
        return multiply_strings(num1.lstrip('-'), num2.lstrip('-'))


def divide(num1, num2):
    if num2 == '0':
        raise ZeroDivisionError("Division by zero")

    if (num1[0] == '-' and num2[0] != '-') or (num1[0] != '-' and num2[0] == '-'):
        return '-' + divide_strings(num1.lstrip('-'), num2.lstrip('-'))
    else:
        return divide_strings(num1.lstrip('-'), num2.lstrip('-'))


def compare(num1, num2):
    if num1[0] == '-' and num2[0] != '-':
        return -1
    if num1[0] != '-' and num2[0] == '-':
        return 1

    abs_num1 = num1.lstrip('-')
    abs_num2 = num2.lstrip('-')

    if num1[0] == '-':
        return -compare_strings(abs_num1, abs_num2)
    else:
        return compare_strings(abs_num1, abs_num2)

num1 = "123456789123456789"
num2 = "-987654321"

print("Додавання:", add(num1, num2))
print("Віднімання:", subtract(num1, num2))
print("Множення:", multiply(num1, num2))
print("Ділення:", divide(num1, num2))
print("Порівняння:", compare(num1, num2))
