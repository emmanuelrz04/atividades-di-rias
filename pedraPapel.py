pontosg = 0
pontos1 = 0
pontos2 = 0

while pontosg < 3:
    jogador1 = int(input("Digite: \n[1] Para pedra\n[2] Para papel\n[3] Para tesoura\n(Jogador 1): "))
    jogador2 = int(input("Digite: \n[1] Para pedra\n[2] Para papel\n[3] Para tesoura\n(Jogador 2): "))

    if jogador1 == jogador2:
        print("Empate! Vamos tentar novamente.")
    elif jogador1 == 1 and jogador2 == 3:
        pontos1 += 1
    elif jogador1 == 2 and jogador2 == 1:
        pontos1 += 1
    elif jogador1 == 3 and jogador2 == 2:
        pontos1 += 1
    else:
        pontos2 += 1
    pontosg += 1

if pontos1 > pontos2:
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")

