cpf = input('Digite seu CPF: ')

while len(cpf) > 11 or len(cpf) < 11:
    print('CPF INVÁLIDO!!!')

    cpf = input('\nDigite seu CPF: ')

num1 = ((int(cpf[0]) * 10)
        + (int(cpf[1]) * 9)
        + (int(cpf[2]) * 8)
        + (int(cpf[3]) * 7)
        + (int(cpf[4]) * 6)
        + (int(cpf[5]) * 5)
        + (int(cpf[6]) * 4)
        + (int(cpf[7]) * 3)
        + (int(cpf[8]) * 2))

r1 = (num1 * 10) % 11

num2 = ((int(cpf[0]) * 11)
        + (int(cpf[1]) * 10)
        + (int(cpf[2]) * 9)
        + (int(cpf[3]) * 8)
        + (int(cpf[4]) * 7)
        + (int(cpf[5]) * 6)
        + (int(cpf[6]) * 5)
        + (int(cpf[7]) * 4)
        + (int(cpf[8]) * 3)
        + (int(cpf[9]) * 2))

r2 = (num2 * 10) % 11

# print(r1, r2)

if r1 == int(cpf[9]) and r2 == int(cpf[10]):
    print('O CPF é válido!!')
else:
    print('O CPF é inválido!!')
