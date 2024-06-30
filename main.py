# Controle de Horário de Ponto

# Dicionário para armazenar os funcionários e seus horários de ponto
funcionarios = {}

def cadastrar_funcionario(nome, cpf, hora_entrada, hora_saida):
    """Cadastra um funcionário e seus horários de ponto"""
    funcionarios[cpf] = {"nome": nome, "hora_entrada": hora_entrada, "hora_saida": hora_saida}
    print(f"Funcionário {nome} cadastrado com sucesso!")

def registrar_ponto(cpf, hora_atual):
    """Registra o ponto do funcionário"""
    if cpf in funcionarios:
        funcionario = funcionarios[cpf]
        if hora_atual < funcionario["hora_entrada"]:
            print(f"Erro: Funcionário {funcionario['nome']} não pode registrar ponto antes da hora de entrada!")
        elif hora_atual > funcionario["hora_saida"]:
            print(f"Erro: Funcionário {funcionario['nome']} não pode registrar ponto após a hora de saída!")
        else:
            print(f"Ponto registrado com sucesso para o funcionário {funcionario['nome']}!")
    else:
        print(f"Erro: Funcionário não encontrado!")

def consultar_ponto(cpf):
    """Consulta o ponto do funcionário"""
    if cpf in funcionarios:
        funcionario = funcionarios[cpf]
        print(f"Ponto do funcionário {funcionario['nome']}:")
        print(f"  Hora de entrada: {funcionario['hora_entrada']}")
        print(f"  Hora de saída: {funcionario['hora_saida']}")
    else:
        print(f"Erro: Funcionário não encontrado!")

def main():
    while True:
        print("Menu:")
        print("  1. Cadastrar funcionário")
        print("  2. Registrar ponto")
        print("  3. Consultar ponto")
        print("  4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            cpf = input("Digite o CPF do funcionário: ")
            hora_entrada = input("Digite a hora de entrada (HH:MM): ")
            hora_saida = input("Digite a hora de saída (HH:MM): ")
            cadastrar_funcionario(nome, cpf, hora_entrada, hora_saida)
        elif opcao == "2":
            cpf = input("Digite o CPF do funcionário: ")
            hora_atual = input("Digite a hora atual (HH:MM): ")
            registrar_ponto(cpf, hora_atual)
        elif opcao == "3":
            cpf = input("Digite o CPF do funcionário: ")
            consultar_ponto(cpf)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()