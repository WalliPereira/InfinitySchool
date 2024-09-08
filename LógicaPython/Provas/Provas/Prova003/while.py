# Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas.
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

numeroCorreto = 5
tentativasMaximas = 3
tentativas = 0

while tentativas < tentativasMaximas:
    tentativa = int(input('Adivinhe o número (entre 1 e 10): '))

    if tentativa == numeroCorreto:
        print('Parabens! Você acertou o número!')
        break
    else:
        tentativas += 1
        tentativasRestantes = tentativasMaximas - tentativas
        if tentativasRestantes > 0:
            print(f'Errado! Mas você ainda pode acertar em mais {tentativasRestantes} tentativas restantes.')
        else:
            print('Errado! Você não tem mais tentativas.')
else:
    print(f'Teve 3 tentativas e não acertou, burro! O número correto era {numeroCorreto}.')
