menu = """
    ###CONTA BANCÁRIA###
                  
        [1] Saque
        [2] Depósito
        [3] Extrato
        [4] Sair
                  
        Escolha a opção: """

#Operação Saque
numeros_saques = 0
conta = 2000.00
extrato = ""


while True:
    opcao = int(input(menu))
    
    if opcao==1:

        if valorsaque>0:

            valorsaque = float(input('Digite o valor que deseja sacar : R$ '))
            extrato += f'Os saques relizados foram de R$ {valorsaque}, '
            conta -= valorsaque
            numeros_saques +=1

        if numeros_saques>=3:
            print("Não pode Realizar mais saques!")
            break

        elif valorsaque>500:
            print('Não pode realizar Saque acima de R$ 500,00 ')
        
        elif valorsaque>conta:
            print('Saldo insuficiente!')


    elif opcao==2:
        valordeposito= float(input('Digite o valor do Depósito: R$ '))

        if valordeposito>0:
            conta+= valordeposito
            extrato += f" Os depósito feito na conta foi no valor de R$ {valordeposito:.2f}"
        else:
            print('Não é possível realizar essa operação!')

    elif opcao==3:
        print("#####EXTRATO#####")
        print(extrato.center)
        print(f'O saldo final da conta foi R$ {conta:.2f}')

    elif opcao==4:
        break

    else:
        print('Desculpe mas não exite esse tipo de Operção!')