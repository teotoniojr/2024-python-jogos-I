
def jogar():
    import random

    print("**********************************************************************************************")
    print("""
            
    ██████╗░███████╗███╗░░░███╗  ██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░  ░█████╗░░█████╗░
    ██╔══██╗██╔════╝████╗░████║  ██║░░░██║██║████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗
    ██████╦╝█████╗░░██╔████╔██║  ╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║  ███████║██║░░██║
    ██╔══██╗██╔══╝░░██║╚██╔╝██║  ░╚████╔╝░██║██║╚████║██║░░██║██║░░██║  ██╔══██║██║░░██║
    ██████╦╝███████╗██║░╚═╝░██║  ░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝  ██║░░██║╚█████╔╝
    ╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░  ╚═╝░░╚═╝░╚════╝░

    ░░░░░██╗░█████╗░██████╗░░█████╗░  ██████╗░░█████╗░  ███████╗░█████╗░██████╗░░█████╗░░█████╗░
    ░░░░░██║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░░░░░██║██║░░██║██║░░██║██║░░██║  ██║░░██║███████║  █████╗░░██║░░██║██████╔╝██║░░╚═╝███████║
    ██╗░░██║██║░░██║██║░░██║██║░░██║  ██║░░██║██╔══██║  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║
    ╚█████╔╝╚█████╔╝██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║
    ░╚════╝░░╚════╝░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
    """)
    print("**********************************************************************************************")

    palavras = ["cachorro", "gato", "peixe", "passarinho", "coelho", "cavalo", "zebra", "hipopotamo"]
    indice = random.randint(0, len(palavras) - 1)
    palavra_secreta = palavras[indice]
    letras_acertadas = ["_" for _ in range(len(palavra_secreta))]
    letras_erradas = []
    tentativas = 1
    numero_de_tentativas = 8

    def imprime_mensagem_vencedor(palavra_secreta):
        print(f"Parabéns, você ganhou! A palavra chave era {palavra_secreta}")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    
    def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()


    while True:
        if(tentativas < numero_de_tentativas):
            print("Palavra: ", " ".join(letras_acertadas))
            print("Letras erradas: ", " ".join(letras_erradas))

            letra = input("Digite uma letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, digite apenas uma letra válida.")
            elif letra in letras_acertadas or letra in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
            elif letra in palavra_secreta.lower():
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i].lower() == letra:
                        letras_acertadas[i] = palavra_secreta[i]
            else:
                letras_erradas.append(letra)
                desenha_forca(tentativas)
                tentativas = tentativas + 1

            if "".join(letras_acertadas).lower() == palavra_secreta.lower():
                imprime_mensagem_vencedor(palavra_secreta)
                break
        else:
            print("Não foi dessa vez");
            imprime_mensagem_perdedor(palavra_secreta)
            break


    


if(__name__ == "__main__"):
    jogar()
