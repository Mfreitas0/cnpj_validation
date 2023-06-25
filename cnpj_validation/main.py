from validation_functions import check

def verification_cnpj(n):
    if check (n) == True:
        print(f'CNPJ: {n} é Válido')
    else:
        print(f'CNPJ: {n} é Inválido')

cnpj = input('Digite um CNPJ: ')
verification_cnpj(cnpj)

""" 
15.436.940/0001-03
71.506.168/0001-12
aaaaa """