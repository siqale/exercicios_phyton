"""
Sistema bancário 
Aceita depósitos, saques, emite extrato
Valida se o valor é positivo para depósito e /ou saque
Formata os valores para moeda com duas casas decimais

"""
menu = """
[s] = Saque
[d] = Deposito
[e] = Extrato
[q] = Sair

=> """

saldo = float(0)
limite = float(500)
deposito = float(0)
num_saque = 3
LIMITE_SAQUE = 3
extrato = ""


while True:
    print("Digite a opção desejada: \n")
    opcao = input(menu)
    if opcao == "s":
        print("Opção saque selecionada \n")
        valor = float(input("informe o  valor a sacar: \n"))
        if valor>0:
            if valor > 500:
                print("valor não permitido. \n")
            else:
                if num_saque <= 0:
                    print("Número de saques excedidos")
                elif valor > saldo:
                    print(f"saldo insuficiente. Saldo atual: R$ {saldo:_.2f}")
                else:
                    num_saque -= 1
                    saldo -= valor
                    extrato += f"Saque -R$ {valor:_.2f}\n"
                    print(saldo)
                    print(valor)
                    #print(f"Saque realizado com sucesso. Saldo atual: R${saldo:_.2f}")
                    #print(f"Quantidade de saques restantes: {num_saque}")
        else:
            print("Não é possível realizar saque de valor negativo")
    elif opcao == "d":
        print("Opção depósito selecionada \n")
        valor = float(input("informe o  valor a depositar: \n"))
        if valor>0:
            saldo += valor
            extrato += f"Depósito -R$ {valor:_.2f}\n"
            #print(f"saldo atual: R${saldo:_.2f}")
        else:
            print("Aceito somente valores positivos")
                
    elif opcao == "e":
        print("Opção extrato selecionada \n")
        print(extrato)
        print(f"Saldo - R$ {saldo:_.2f}")
    
    elif opcao == "q":
        print("Opção sair selecionada \n. Bye bye")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente uma opção válida \n")
        
