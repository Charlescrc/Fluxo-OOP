
#Parte 1 - Menu

def menu():
    print("<<<<Sistema de Transporte>>>>\n")
    print("Menu de opções:\n")
    print("1 - Criar")
    print("2 - Mostrar")
    print("3 - Assignar")
    print("4 - Adicionar")
    print("5 - Alterar")
    print("6 - Deletar")
    print("7 - Sair\n")
    opcao = int(input("Qual a opção desejada?"))
    return opcao
    

def selecao(menu):
    selection = str(input("Deseja fazer a seleção?"))
    motorista = ["Eduardo", "Lucas", "Mateus"]
    fiscal = ["Magno", "Leticia"]
    onibus = ["KZX-896","FDD-5981", "FLA2000"]
    ponto = ["estação1", "estação2", "estação3"]
    rota = ["ZonaSul", "ZonaNorte","ZonaOeste"]
    while selection == "sim":
        if menu == 1:
            print("\nDa Opção 1, você deseja:\n")
            print("1 - Criar ônibus")
            print("2 - Criar ponto de parada")
            print("3 - Criar motorista")
            print("4 - Criar fiscal")
            opcao1 = int(input("\nQual a opção?"))
            if opcao1 == 1:
                resp = str(input("Deseja adicionar algum onibus?"))
                while resp == "sim":
                    num = str(input("Qual a placa do ônibus?"))
                    num = "Ônibus "+num
                    onibus.append(num)
                    print("Os onibus são:",onibus)
                    resp = str(input("Deseja adicionar onibus?"))
                    onibus = onibus.append(num)
            if opcao1 == 2:
                resp = str(input("Deseja adicionar algum ponto de parada?"))
                while resp == "sim":
                    point = str(input("Qual o nome do ponto? "))
                    ponto.append(point)
                    print("Os pontos são:",ponto)
                    resp = str(input("Deseja adicionar algum ponto?"))
                return 
            if opcao1 == 3:
                resp = str(input("Deseja adicionar algum motorista?"))
                while resp == "sim":
                    nome = str(input("Qual o nome do motorista?"))
                    motorista.append(nome)
                    print("Os motoristas são:",motorista)
                    resp = str(input("Deseja adicionar motorista?"))
                return 
            elif opcao1 == 4:
                resp = str(input("Deseja adicionar algum fiscal?"))
                while resp == "sim":
                    name = str(input("Qual o nome do fiscal?"))
                    fiscal.append(name)
                    print("Os fiscais são:",fiscal)
                    resp = str(input("Deseja adicionar fiscal?"))
        if menu == 2:
            print("\nDa Opção 2, você deseja:\n")
            print("1 - Mostrar ônibus")
            print("2 - Mostrar rotas")
            print("3 - Mostrar motoristas")
            print("4 - Mostrar fiscais")
            opcao2 = int(input("\nQual a opção?"))
            if opcao2 == 1:
                return print(onibus)
            if opcao2 == 2:
                return print(ponto)
            if opcao2 == 3:
                return print(motorista)
            if opcao2 == 4:
                return print(fiscal)
        if menu == 3:
            print("\nDa Opção 3, você deseja:\n")
            print("1 - Assignar motorista ao ônibus")
            print("2 - Assignar fiscal ao ônibus")
            opcao3 = int(input("\nQual opção deseja assignar?"))
            if opcao3 == 1:
                driver = str(input("Qual motorista?"))
                bus = str(input("Qual onibus?"))
                print("O motorista ",driver,"agora está assignado ao veiculo ",bus) 
            elif opcao3 == 2:
                fisc = str(input("Qual fiscal?"))
                bus = str(input("Qual onibus?"))
                print("O fiscal ",fisc,"agora está assignado ao veiculo ",bus)
            return
        if menu == 4:
            print("<<<Adicionar ponto de parada ao ônibus")
            bus = str(input("Qual o õnibus?"))
            parada = str(input("Qual o ponto de parada deseja adicionar?"))
            print("A partir de agora, o veiculo ",bus,"terá ponto de parada em ",parada)
        if menu == 5:
            print("\nDa Opção 5, você deseja:\n")
            print("1 - Alterar dados do ônibus")
            print("2 - Alterar dados da parada")
            print("3 - Alterar dados do motorista")
            print("4 - Alterar dados do fiscal")
            print("5 - Alterar rota do ônibus")
            opcao5 = int(input("\nQual dado deseja alterar?"))
            if opcao5 == 1:
                print(onibus)
                pos = int(input("Qual posição deseja alterar?"))
                dados = str(input("Agora qual placa deseja inserir?"))
                print("Agora, o veiculo",onibus[pos-1],"foi alterado para",str(dados))
                onibus[pos-1] = dados
                print(onibus)
            if opcao5 == 2:
                print(ponto)
                pos = int(input("Qual posição deseja alterar?"))
                dados = str(input("Agora qual parada deseja inserir?"))
                print("Agora, a parada",ponto[pos-1],"foi alterado para",str(dados))
                ponto[pos-1] = dados
                print(ponto)
            if opcao5 == 3:
                print(motorista)
                pos = int(input("Qual posição deseja alterar?"))
                dados = str(input("Agora qual parada deseja inserir?"))
                print("Agora, o motorista",motorista[pos-1],"foi alterado para",str(dados))
                motorista[pos-1] = dados
                print(motorista)
            if opcao5 == 4:
                print(fiscal)
                pos = int(input("Qual posição deseja alterar?"))
                dados = str(input("Agora qual parada deseja inserir?"))
                print("Agora, o fiscal",fiscal[pos-1],"foi alterado para",str(dados))
                fiscal[pos-1] = dados
                print(fiscal)
            if opcao5 == 5:
                print(rota)
                pos = int(input("Qual posição deseja alterar?"))
                dados = str(input("Agora qual parada deseja inserir?"))
                print("Agora, a rota",rota[pos-1],"foi alterado para",str(dados))
                rota[pos-1] = dados
                print(rota) 
        if menu == 6:
            print("\nDa Opção 6, você deseja:\n")
            print("1 - Deletar ônibus")
            print("2 - Deletar ponto de parada")
            print("3 - Deletar motorista")
            print("4 - Deletar fiscal")
            opcao6 = int(input("\nQual dado deseja deletar?"))
            if opcao6 == 1:
                print(onibus)
                pos = int(input("Qual posição deseja deletar?"))
                print("Agora, o veiculo",onibus[pos-1],"foi deletado")
                del onibus[pos-1]
                print(onibus)
            if opcao6 == 2:
                print(ponto)
                pos = int(input("Qual posição deseja deletar?"))
                print("Agora, o ponto",ponto[pos-1],"foi deletado")
                del ponto[pos-1]
                print(ponto)
            if opcao6 == 3:
                print(motorista)
                pos = int(input("Qual posição deseja deletar?"))
                print("Agora, o motorista",motorista[pos-1],"foi deletado")
                del motorista[pos-1]
                print(motorista)
            elif opcao6 == 4:
                print(fiscal)
                pos = int(input("Qual posição deseja deletar?"))
                print("Agora, o fiscal",fiscal[pos-1],"foi deletado")
                del fiscal[pos-1]
                print(fiscal)
        elif menu == 7:
            return print("Você saiu do programa!")
        else:
            print("Atualização feita com sucesso!")
            return
    return
    print("Os motoristass até o momento são:",motorista)
    print("Os ônibus até o momento são:",onibus)
    print("Os pontos até o momento são:",ponto)
    print("Os fiscais até o momento são:",fiscal)


#Parte 2 - Organização de elementos


menu = menu()
print(selecao(menu))
print
