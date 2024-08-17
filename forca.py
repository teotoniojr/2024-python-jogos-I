
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

    palavra_secreta = "Teotonio"
    letras_acertadas = ["_" for _ in range(len(palavra_secreta))]
    letras_erradas = []

    while True:
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

        if "".join(letras_acertadas).lower() == palavra_secreta.lower():
            print("Parabéns, você ganhou! A palavra era:", palavra_secreta)
            break


    


if(__name__ == "__main__"):
    jogar()
