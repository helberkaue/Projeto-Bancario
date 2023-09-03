def saque(conta, extrato, numeros_saques):
    valorsaque = float(input('Digite o valor que deseja sacar: R$ '))

    if valorsaque <= 0:
        print('Valor inválido. O saque deve ser maior que zero.')
        return conta, extrato, numeros_saques

    if valorsaque > 500:
        print('Não pode realizar saque acima de R$ 500,00.')
    elif valorsaque > conta:
        print('Saldo insuficiente!')
    else:
        extrato += f'Os saques realizados foram de R$ {valorsaque:.2f}, '
        conta -= valorsaque
        numeros_saques += 1

    if numeros_saques >= 3:
        print('Não pode realizar mais saques!')

    return conta, extrato, numeros_saques


def deposito(conta, extrato):
    valordeposito = float(input('Digite o valor do depósito: R$ '))

    if valordeposito <= 0:
        print('Valor inválido. O depósito deve ser maior que zero.')
        return conta, extrato

    conta += valordeposito
    extrato += f'Os depósitos feitos na conta foram no valor de R$ {valordeposito:.2f}, '

    return conta, extrato


def extrato_bancario(conta, extrato):
    print("#####EXTRATO#####")
    print(extrato)
    print(f'O saldo final da conta é R$ {conta:.2f}')


def main(menu):
    conta = 2000.00
    extrato = ""
    numeros_saques = 0

    while True:
        opcao = input(menu)

        if opcao == '1':
            conta, extrato, numeros_saques = saque(conta, extrato, numeros_saques)
        elif opcao == '2':
            conta, extrato = deposito(conta, extrato)
        elif opcao == '3':
            extrato_bancario(conta, extrato)
        elif opcao == '4':
            break
        else:
            print('Desculpe, mas essa opção não existe!')

if __name__ == "__main__":
    menu = """
    ###CONTA BANCÁRIA###
                  
        [1] Saque
        [2] Depósito
        [3] Extrato
        [4] Sair
                  
        Escolha a opção: """
    main(menu)



# Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. 
# O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. 
# Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. 
# Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

