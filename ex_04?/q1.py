# 15/10/25 - Validar o numero do cpf informado.


def calc_produtos(cpf_parts):
    lista_produtos = []
    for i,v in enumerate(cpf_parts):
        lista_produtos.append(int(v) * (len(cpf_parts) + 1 - i))
    return lista_produtos


def calc_digito_verificador(soma):
    resto_por_11 = soma % 11
    if resto_por_11 < 2:
        return 0
    else:
       return int(11 - resto_por_11)


while True:
    CPF = input("Digite o seu CPF: ").replace('.', '').replace('-', '')
    if len(CPF) != 11:
        print("Quantia de digitos invalida!")
        continue

    cpf_parts = list(CPF)[:-2]

    lista_produtos = calc_produtos(cpf_parts)

    digito_verificador_1 = calc_digito_verificador(sum(lista_produtos))

    cpf_parts.append(str(digito_verificador_1))

    lista_produtos = calc_produtos(cpf_parts)

    digito_verificador_2 = calc_digito_verificador(sum(lista_produtos))
    cpf_parts.append(str(digito_verificador_2))

    if list(CPF) == cpf_parts:
        print('CPF é valido!')
    else:
        print('CPF inválido!')




