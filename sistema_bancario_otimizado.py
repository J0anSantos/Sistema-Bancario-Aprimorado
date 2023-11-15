def realizar_deposito(saldo, valor_deposito, extrato, /):
    saldo += valor_deposito
    print("Depósito realizado com sucesso!")
    extrato += f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!\n"
    
    return saldo, extrato

def realizar_saque(*, saldo, extrato, limite_saques, limite, numero_saques):

    if(numero_saques == limite_saques):
        print("Limite diário de saque excedido! Tente novamente amanhã")
        return saldo, extrato, numero_saques
    
    valor_saque = float(input("Insira o valor a ser sacado: "))
    if(valor_saque > limite):
        print(f"Limite de operação excedido, não é possivel realizar um saque maior que R$ {LIMITE:.2f}. Tente realizar uma nova operação.")
    
    elif(valor_saque > saldo):
        print("Saldo insuficiente! Tente novamente.")    

    else:
        saldo -= valor_saque
        print("Saque realizado com sucesso!")
        extrato += f"Saque de R$ {valor_saque:.2f} realizado com sucesso!\n"
        numero_saques += 1

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("================ EXTRATO =================")
    if not extrato:
        print(f"Não foram realizadas movimentações!\n")
    else:
        print(extrato)
        
    print(f"Saldo em conta: R$ {saldo:.2f}")
    print("===========================================")

def criar_usuario(nome, data_nasc, cpf, ender):
    novo_cliente = {"nome" : nome, "data_nasc": data_nasc, "endereco" : ender}
    return novo_cliente

def criar_conta_corrente(dados, numero_conta, agencia):
    print("\nConta criada com sucesso!")
    return dados, numero_conta, agencia

def listar_contas(contas):
    
    for indice in range(len(contas)):
        print("====================================")
        print(f"Número da conta: {contas[indice][1]}  Agência: {contas[indice][2]}")
        print("Dados do Cliente\n\n")
        print(f"Nome: {contas[indice][0]["nome"]}\nEndereço: {contas[indice][0]["endereco"]}\n")
    print("====================================")



menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] cadastrar usuário
[cc] criar conta corrente
[lc] listar contas
[q] Sair


=> """

LIMITE_SAQUES = 3
LIMITE = 500.0
saldo = 0.0
extrato = ""
numero_saques = 0
usuarios = list()
contas = list()
numero_conta = 1
AGENCIA = "0001"

while True:

    opcao = input(menu)

    if(opcao == "d"):
        valor_deposito = float(input("Insira a quantidade que vai ser depositada: "))
        if(valor_deposito > 0):
            saldo, extrato = realizar_deposito(saldo, valor_deposito, extrato)
        else:
            print("Valor de depósito inválido! Tente novamente.")

    elif(opcao == "s"):
            saldo, extrato, numero_saques = realizar_saque(saldo=saldo, extrato=extrato, limite_saques = LIMITE_SAQUES, limite=LIMITE, numero_saques = numero_saques)
    
    elif(opcao == "e"):
        exibir_extrato(saldo, extrato=extrato)
    
    elif(opcao == "c"):
        nome = input("\nInsira o nome do Cliente: ")
        data_nasc = input("Insira a data de nascimento do Cliente (dd/mm/yyyy): ")
        cpf = input("Insira o CPF do Cliente: ")
        ender = input("Insira o endereço do Cliente: ")

        
        if len(usuarios) != 0:
            if cpf not in usuarios[0].keys():
                usuarios[0][cpf] = criar_usuario(nome, data_nasc, cpf, ender)
                print("\nO usuário foi cadastrado com sucesso!")
            else:
                print("\nUsuário já cadastrado! Tente novamente.")
        else:
            dict_aux = {cpf: criar_usuario(nome, data_nasc, cpf, ender)}
            usuarios.append(dict_aux)
            print("\nO usuário foi cadastrado com sucesso!")

    elif(opcao == "cc"):
        cpf = input("\nInsira o CPF do usuário que vai ter sua conta criada: ")
        casos = 0

        if len(usuarios) == 0:
            print("Usuário não encontrado, tente novamente.")
        else:
            for chave, valor in usuarios[0].items():
                if chave == cpf:
                    contas.append(criar_conta_corrente(valor, numero_conta, AGENCIA))
                    numero_conta += 1
                    casos += 1
                    break
            if(casos == 0):
                print("Usuário não encontrado, tente novamente.")
        

    elif(opcao == "lc"):
        print("\nListando contas...\n")
        listar_contas(contas)  

    elif(opcao == "q"):
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")