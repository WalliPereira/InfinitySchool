# Ex03. Faça um programa para o calculo de juros, peça o valor inicial, taxa de juros em porcentagem (sem o % e considere que a taxa é ao mês) e quantidade de tempo em meses. Ao final mostre o valor total
# Formula: total_juros = valor_inicial * taxa * tempo 

valorInicial = float(input('Digite um valor: '))
taxa = float(input('Digite um valor para a taxa: '))
tempMeses = int(input('Digite um mes: '))

total_juros = valorInicial * (taxa / 100) * tempMeses
valor_total = valorInicial + total_juros

print(f'Seu investimento rendeu R${total_juros:.2f} e você receberá {valor_total:.2f} ')