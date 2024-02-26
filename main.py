global saldo
saldo = 0
operacoes = [[],[]]
limsaque = 0

def depositar(valor):
    global saldo
    if valor < 0:
        print("Operação Inválida")
    else:
        operacoes[0].append(valor)
        saldo += valor
        print(f"Depósito de R${valor}")
    return saldo 

def sacar(valor):
    global saldo
    global limsaque
    if valor < 0:
        print("Operação Inválida")
    elif valor > 500:
        print("Operação Inválida")
    elif limsaque > 2:
        print("Limite de Saque atingido")
    elif saldo < valor:
        print("Saldo Insuficiente")
    else:
        operacoes[1].append(valor)
        saldo -= valor
        limsaque += 1
        print(f"Saque de R${valor}")

def extrato():
    print("=========EXTRATO=========")
    if len(operacoes[0]) == 0 and len(operacoes[1]) == 0:
        print("Sem operações registradas")
    for c in operacoes[0]:
        print(f"Depósito de R${c}")      
    for c in operacoes[1]: 
        print(f"Saque de R${c}")
    print("==========TOTAL==========") 
    print(f"R${sum(operacoes[0])-sum(operacoes[1])}")       
    print("===========FIM===========")       

def menu():
    resp = input("Digite a opção: ")
    if resp == 'd':
        valor = int(input("Digite o Valor: "))
        depositar(valor)
    elif resp == 's':
        valor = int(input("Digite o Valor: "))
        sacar(valor)
    elif resp == 'e':
        extrato()       
    elif resp == "q":
        return False
    else:
        print("Digite uma opção válida")
        
while True:
    if menu() == False:
        break
    