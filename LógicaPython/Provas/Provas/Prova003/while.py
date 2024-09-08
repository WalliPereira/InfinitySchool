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
            print(f'Errado! Você ainda tem {tentativasRestantes} tentativas restantes.')
        else:
            print('Errado! Você não tem mais tentativas.')
else:
    print(f'Você esgotou suas tentativas. O número correto era {numeroCorreto}')