def mostrar_loja(personagem):
    print("Bem-vindo à loja!")
    print(f"Moedas possuídas: {personagem['dinheiro']}")
    print("Opções:")
    print("[1] - Comprar Espada (+10 de dano, 50 moedas)")
    print("[2] - Comprar Armadura (+20 de vida, 70 moedas)")
    print("[3] - Comprar Poção de Sono (1 uso, 100 moedas)")
    print("[4] - Sair da loja")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        if personagem['dinheiro'] >= 50:
            personagem['dinheiro'] -= 50
            print("Você comprou uma Espada! Seu dano aumentou em 10.")
            personagem['espada'] = True  # Define a variável 'espada' como True
        else:
            print("Você não tem moedas suficientes.")
    elif escolha == "2":
        if personagem['dinheiro'] >= 70:
            personagem['dinheiro'] -= 70
            print("Você comprou uma Armadura! Sua vida aumentou em 20.")
            personagem['vida'] += 20
        else:
            print("Você não tem moedas suficientes.")
    elif escolha == "3":
        if personagem['dinheiro'] >= 100:
            personagem['dinheiro'] -= 100
            print("Você comprou uma Poção de Sono! Use com sabedoria.")
            personagem['poção_de_sono'] = True
        else:
            print("Você não tem moedas suficientes.")
    elif escolha == "4":
        print("Saindo da loja.")
        print(f"Vida atual: {personagem['vida']}")
        if personagem['espada'] == True:
            print("Dano atual do personagem: 15 a 25")
        else:
            print("Dano atual do personagem: 5 a 15")
    else:
        print("Opção inválida!")




