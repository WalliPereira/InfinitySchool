# Ex09. Faça um programa que peça um ano, e mostre na tela se o ano é bissexto ou não (divisivel por 4, sem ser divisivel por 100, exceto os divisiveis por 400)

ano = int(input('Digite um ano para saber se ele é bissexto: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')