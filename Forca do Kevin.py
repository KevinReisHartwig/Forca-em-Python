'''jogo da forca do Kevin, os desenhos eu peguei na internet e colori'''

import random
print("\33[37m*********************************")
print("***\33[m \33[31mBem vindo ao jogo da Forca do Kevin!\33[m \33[37m***")
print("*********************************\33[m")
t = True
chances = 6
erros = 0
palavras = []
print("\33[32mRegras do jogo:\33[m")
print("\33[30m1-Coloque palavras para iniciar o jogo, você pode colocar quantas você quiser\33[m")
print("\33[30m2-Só tem 6 chances.\33[m")
print("\33[30m3-A unica dica é a quantidade de letras.\33[m")
print("\33[30m4-Se aparecer o trofeu você ganhou e a caveira você perdeu.\33[m")
print("\33[30mBOM JOGO!\33[m")

while t == True:

    print("[1] digite para colocar palavras")
    print("[2] digite para jogar")
    print("[3] digite para sair")
    numero = int(input("\33[33mdigite um numero 1,2 ou 3:\33[m "))


    if numero == 3:
        t = False
        print("\33[31mvocê saiu do jogo!")
    while numero == 1 or numero == "S":
        palavra = str(input("digite uma palavra: ")).upper()
        if palavra in palavras:
            print("\33[31mjá tem essa palavra\33[m")
        else:
            palavras.append(palavra)
            numero = str(input("deseja por mais palavras? S/N: ")).upper()
    if numero==2 and palavras == []:
        print("\33[31mnão tem palavras para iniciar o jogo!\33[m")
        print("\33[31mcoloque palavras digitando \33[m(1)\33[31m, assim você pode iniciar o jogo!\33[m")
    else:
        while numero == 2:





            aleatorio = random.randrange(0, len(palavras))
            palavra_secreta = palavras[aleatorio].upper()




            palavra_escrita = ["_"] * len(palavra_secreta)
            print(palavra_escrita)

            while erros < chances and "_" in palavra_escrita:
                chute = str(input("\33[36mdigite uma letra: \33[m")).upper()

                if chute in palavra_secreta:
                    print("\33[32mAcertou a letra, você teve um total de {} erros\33[m".format(erros))
                    for i in range(len(palavra_secreta)):
                        if chute == palavra_secreta[i]:
                            palavra_escrita[i] = chute

                else:
                    erros = erros + 1
                    print("\33[31mVocê errou {} vez, só pode errar 6 vezes no total.\33[m".format(erros))
                    print("  _______     ")
                    print(" |/      |    ")

                    if (erros == 1):
                        print(" |      (_)   ")
                        print(" |            ")
                        print(" |            ")
                        print(" |            ")

                    if (erros == 2):
                        print(" |      (_)   ")
                        print(" |      \     ")
                        print(" |            ")
                        print(" |            ")

                    if (erros == 3):
                        print(" |      (_)   ")
                        print(" |      \|    ")
                        print(" |            ")
                        print(" |            ")

                    if (erros == 4):
                        print(" |      (_)   ")
                        print(" |      \|/   ")
                        print(" |            ")
                        print(" |            ")

                    if (erros == 5):
                        print(" |      (_)   ")
                        print(" |      \|/   ")
                        print(" |       |    ")
                        print(" |      /     ")

                    if (erros == 6):
                        print(" |      (_)   ")
                        print(" |      \|/   ")
                        print(" |       |    ")
                        print(" |      / \   ")

                    print(" |            ")
                    print("_|___         ")
                    print()

                print(palavra_escrita)
            if erros == chances:
                print("\33[31mVocê perdeu game over!\33[m")
                print("\33[34mA palavra era\33[m \33[32m{}\33[m!".format(palavra_secreta))
                print("    _______________         ")
                print("   /               \       ")
                print("  /                 \      ")
                print(" /                   \  ")
                print(" |   \33[31:41mXXXX\33[m    \33[31:41mXXXX\33[m    |    ")
                print(" |   \33[31:41mXXXX\33[m    \33[31:41mXXXX\33[m    |    ")
                print(" |   \33[31:41mXXX\33[m      \33[31:41mXXX\33[m    |      ")
                print(" |                   |      ")
                print(" \__      \33[37:47mXXX\33[m      __/     ")
                print("   |\     \33[37:47mXXX\33[m     /|       ")
                print("   | |           | |        ")
                print("   | \33[33:43mI I I I I I I\33[m |        ")
                print("   |  \33[33:43mI I I I I I\33[m  |        ")
                print("   \_             _/       ")
                print("     \_         _/         ")
                print("       \_______/           \33[m")
                numero = int(input('''selecione uma opção:
                        [1] Adcionar palavra
                        [2] jogar de novo
                        [3] Sair 
                        => '''))
            else:
                print("\33[32mVocê ganhou parabens!\33[m")
                print("       \33[33:43m___________\33[m      ")
                print("      \33[33:43m'._==_==_=_.'\33[m     ")
                print("      \33[33:43m.-\\:      /-.\33[m    ")
                print("     \33[33:43m| (|:.     |) |\33[m    ")
                print("      \33[33:43m'-|:.     |-'\33[m     ")
                print("        \33[33:43m\\::.    /\33[m      ")
                print("         \33[33:43m'::. .'\33[m        ")
                print("           \33[33:43m) (\33[m          ")
                print("         \33[33:43m_.' '._\33[m        ")
                print("        \33[33:43m'-------'\33[m       ")
                numero = int(input('''selecione uma opção:
                        [1] Adcionar palavra
                        [2] jogar de novo
                        [3] Sair 
                        => '''))






