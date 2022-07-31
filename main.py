"""
Programa em Python 3 para converter Celsius para Kelvin e Fahrenheit
"""
from helpers import celsius_para_fahrenheit, celsius_para_kelvin

if __name__ == '__main__':
    while True:
        mensagem = "\nPor favor insira a temperatura em Celsius."
        mensagem += "\nSe desejar sair, pressione 'q': "

        try:
            celsius = input(mensagem)
            if celsius.lower() != 'q':
                print(f"\nTemperatura em Kelvin(K) = {celsius_para_kelvin(float(celsius))}")
                print(f"Temperatura em Fahrenheit(F) = {celsius_para_fahrenheit(float(celsius))}")
            else:
                print("\nAté a próxima")
                break
        except ValueError:
            print("\nVocê digitou um caracter inválido. \nPor favor insira um número ou a letra 'q'.")

