from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo Insuficiente')
    else:
        print('Cliente não encontrado!')
