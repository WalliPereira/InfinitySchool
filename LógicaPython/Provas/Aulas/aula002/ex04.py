# Ex04. Faça um programa que peça a temperatura em celcius e mostre o valor em fahrenheit
# Formula: tf = tc * 1.8 + 32

temperatura_celcius = float(input('Digite a temperatura em º celcius: '))
temperatura_fahrenheit = temperatura_celcius * 1.8 + 32

print(f'Temperatura: {temperatura_fahrenheit}ºF')