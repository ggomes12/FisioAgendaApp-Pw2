import re


def validarCPF(cpf):
    cpf = re.sub('r/D', '', cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf in [str(i)*11 for i in range(10)]:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    secondDigit = (soma * 10 % 11) % 10
    if int(cpf[10]) != secondDigit:
        return False

    return True
