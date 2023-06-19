import re


def no_characters(x):
    x = list(re.sub(r'[^0-9]', '', x))
    x = [int(i) for i in x]
    return x


def first_digit(is_cnpj):
    is_cnpj = no_characters(is_cnpj)
    sequence_number = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    sequential_sum_and_cnpj = [(is_cnpj[i] * s)for i, s in enumerate(sequence_number)]
    formula_result = (11 - (sum(sequential_sum_and_cnpj) % 11))
    return 0 if formula_result > 9 else formula_result


def second_digit(is_cnpj):
    first_d = first_digit(is_cnpj)
    is_cnpj = no_characters(is_cnpj[0:-2])
    is_cnpj.append(first_d)
    
    sequence_number = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sequential_sum_and_cnpj = [(is_cnpj[i] * s)for i, s in enumerate(sequence_number)]
    formula_result = (11 - (sum(sequential_sum_and_cnpj) % 11))
    return 0 if formula_result > 9 else formula_result


def check(is_cnpj):
    try:
        first_d = first_digit(is_cnpj)
        second_d = second_digit(is_cnpj)
        is_cnpj = no_characters(is_cnpj)

        cnpj_with_verified_digits = is_cnpj[0:-2]
        cnpj_with_verified_digits.append(first_d), cnpj_with_verified_digits.append(second_d)
        return False if not cnpj_with_verified_digits == is_cnpj else True
    except:
        return False