
from validation_functions import check, second_digit

def verification_cnpj(n):
    if check (n) == True:
        print(f'CNPJ: {n} é Válido')
    else:
        print(f'CNPJ: {n} é Inválido')


verification_cnpj('15.436.940/0001-03')
verification_cnpj('71.506.168/0001-12')
verification_cnpj('aaaaa')