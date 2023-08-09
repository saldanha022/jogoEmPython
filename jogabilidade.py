import random

def batalhar(personagem, inimigo):
    print(f"Você está enfrentando o {inimigo['nome']} - {inimigo['titulo']}")
   
    while personagem["vida"] > 0 and inimigo["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do {inimigo['nome']}: {inimigo['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            if personagem.get('espada', False):  # Verifica se o jogador tem uma espada
                player_attack_damage = random.randint(15, 25)  # Dano randomizado com espada
            else:
                player_attack_damage = random.randint(5, 15)  # Dano randomizado sem espada
            # Turno do jogador
            player_attack_damage = random.randint(5, 15)
            # Lógica de dano crítico
            is_critical = random.random() < 0.2  # 20% de chance de dano crítico
            if is_critical:
                player_attack_damage *= 2  # Dano crítico dobrado
                print("DANO CRÍTICO!")
            inimigo["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca {inimigo['nome']} e causa {player_attack_damage} de dano.")
            
            # Gera uma pequena chance de dropar um baú de moedas
            if random.random() < 0.05:  # 5% de chance de dropar um baú
                moedas_encontradas = random.randint(20, 50)
                print(f"Você encontrou um baú de moedas! Ganhou {moedas_encontradas} moedas!")
                personagem["dinheiro"] += moedas_encontradas
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, inimigo)  # Usar poção de sono
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if inimigo["vida"] <= 0:
            print(f"Você derrotou o {inimigo['nome']}!")
            moedas_ganhas = random.randint(10, 20)  # Recompensa aleatória de moedas
            print(f"Você ganhou {moedas_ganhas} moedas!")
            personagem["dinheiro"] += moedas_ganhas
            return True
       
        # Turno do inimigo
        if random.random() < 0.3:  # 30% de chance de erro do inimigo
            print(f"{inimigo['nome']} errou o ataque!")
        else:
            enemy_attack_damage = random.randint(8, 12)
            personagem["vida"] -= enemy_attack_damage
            print(f"{inimigo['nome']} ataca {personagem['nome']} e causa {enemy_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado!")
            return False

def batalhar_rei(personagem, rei):
    print(f"Você está enfrentando o Rei {rei['nome']} - {rei['titulo']}")
   
    while personagem["vida"] > 0 and rei["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do Rei {rei['nome']}: {rei['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            if personagem.get('espada', False):  # Verifica se o jogador tem uma espada
                player_attack_damage = random.randint(15, 25)  # Dano randomizado com espada
            else:
                player_attack_damage = random.randint(5, 15)  # Dano randomizado sem espada
            # Lógica de dano crítico
            is_critical = random.random() < 0.2  # 20% de chance de dano crítico
            if is_critical:
                player_attack_damage *= 2  # Dano crítico dobrado
                print("DANO CRÍTICO!")
            rei["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca o Rei {rei['nome']} e causa {player_attack_damage} de dano.")
        elif escolha == 2:
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, rei)  # Usar poção de sono
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rei["vida"] <= 0:
            print(f"Você derrotou o Rei {rei['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       
        # Turno do Rei
        rei_attack_damage = random.randint(50, 100)
        personagem["vida"] -= rei_attack_damage
        print(f"O Rei {rei['nome']} ataca {personagem['nome']} e causa {rei_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pelo Rei!")
            return False

def batalhar_rainha(personagem, rainha):
    print(f"Você está enfrentando a Rainha {rainha['nome']} - {rainha['titulo']}")
   
    while personagem["vida"] > 0 and rainha["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida da Rainha {rainha['nome']}: {rainha['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        input("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        print("[3] - Usar poção de sono")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == 1:
            if personagem.get('espada', False):  # Verifica se o jogador tem uma espada
                player_attack_damage = random.randint(15, 25)  # Dano randomizado com espada
            else:
                player_attack_damage = random.randint(5, 15)  # Dano randomizado sem espada
            # Lógica de dano crítico
            is_critical = random.random() < 0.2  # 20% de chance de dano crítico
            if is_critical:
                player_attack_damage *= 2  # Dano crítico dobrado
                print("DANO CRÍTICO!")
            rainha["vida"] -= player_attack_damage
            print(f"{personagem['nome']} ataca a Rainha {rainha['nome']} e causa {player_attack_damage} de dano.")
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        elif escolha == "3":
            usar_pocao_de_sono(personagem, rainha)  # Usar poção de sono
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rainha["vida"] <= 0:
            print(f"Você derrotou a Rainha {rainha['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       
        # Turno da Rainha
        rainha_attack_damage = random.randint(40, 80)
        personagem["vida"] -= rainha_attack_damage
        print(f"A Rainha {rainha['nome']} ataca {personagem['nome']} e causa {rainha_attack_damage} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pela Rainha!")
            return False
        
def usar_pocao_de_sono(personagem, inimigo):
    if personagem.get('poção_de_sono', False):
        print("Você usou a Poção de Sono e colocou o adversário para dormir!")
        inimigo['vida'] = 0
        del personagem['poção_de_sono']  # Remove a poção da mochila
    else:
        print("Você não tem uma Poção de Sono para usar.")

