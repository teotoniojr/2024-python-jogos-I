import random

def jogar():
    

    print("**********************************************************************************************")
    print("""
        

    ▒█▀▀█ █▀▀ █▀▄▀█ 　 ▀█░█▀ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ 　 █▀▀█ █▀▀█ 　 ░░░▒█ █▀▀█ █▀▀▄ █▀▀█ 　 █▀▀▄ █▀▀ 
    ▒█▀▀▄ █▀▀ █░▀░█ 　 ░█▄█░ ▀█▀ █░░█ █░░█ █░░█ 　 █▄▄█ █░░█ 　 ░▄░▒█ █░░█ █░░█ █░░█ 　 █░░█ █▀▀ 
    ▒█▄▄█ ▀▀▀ ▀░░░▀ 　 ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ 　 ▀░░▀ ▀▀▀▀ 　 ▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀▀ 　 ▀▀▀░ ▀▀▀ 

    ░█▀▀█ █▀▀▄ ░▀░ ▀█░█▀ ░▀░ █▀▀▄ █░░█ █▀▀█ █▀▀ █▀▀█ █▀▀█ 
    ▒█▄▄█ █░░█ ▀█▀ ░█▄█░ ▀█▀ █░░█ █▀▀█ █▄▄█ █░░ █▄▄█ █░░█ 
    ▒█░▒█ ▀▀▀░ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀▀
        
            """)
    print("**********************************************************************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 20
    pontos = 1000



    print("Qual nível de dificuldade desejada?")
    print("(0) Fácil (1) Médio (2) Difícil (3) Muito Difícil (4) Extrema")

    nivel = int(input("Defina um nível:"))


    while (nivel < 0 or nivel > 4):
        print("Por favor, escolha um número entre 0 e 4.")
        nivel = int(input("Defina um nível:"))


    if(nivel == 0):
        total_de_tentativas = 20
        nivel = "Fácil"
    elif(nivel == 1):
        total_de_tentativas = 10
        nivel = "Média"
    elif(nivel == 2):
        total_de_tentativas = 5
        nivel = "Difícil"
    elif(nivel == 3):
        total_de_tentativas = 3
        nivel ="Muito Difícil"
    else:
        total_de_tentativas = 1
        nivel = "Extrema!"

    print(f"Você escolheu a dificuldade {nivel}.")
    print("**********************************************************************************************")     


    for rodada in range(1,total_de_tentativas + 1) :
            
            print(f"Tentativa {rodada} de {total_de_tentativas}")
            chute_str = input("Digite um número entre 1 e 100: ")
            print("Você digitou " , chute_str)
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100")
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print(f"Parabéns, você acertou! Conseguiu um total de {pontos} pontos! :)")
                break
            else:
                if(maior):
                    print("O seu chute foi maior do que o número secreto!")
                elif(menor):
                    print("O seu chute foi menor do que o número secreto!")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos     


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()