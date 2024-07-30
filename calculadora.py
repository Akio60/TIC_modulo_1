# calculadora.py
# Rev 1.0
# Date 30/07/24
# Dev : Akio60 - Vitor Akio - vitorakoisawa@gmail.com
# 
#------------------------------------------------------------------------------------
#
# App Description:
# Calculadora desenvolvida para aprendizado durante as aulas de phyton TIC em trilhas
# Funcoes utilizadas:
#  - Soma
#  - Subtração
#  - Divisão
#  - Produto
#
#------------------------------------------------------------------------------------
#
# Observações de aprendizado
#
# Meteodologia para deixar um progama rodando em todo o tempo sem utilizaçao do laço
# case _  para verificação de casos que não foram incluidos
# Uso da biblioteca Time para funcoes temporais
#
#------------------------------------------------------------------------------------

# Libraries
import time

# Functions Def

def calc_sum(primeiro_valor,segundo_valor):
    return int(primeiro_valor) + int(segundo_valor)

def calc_sub(primeiro_valor,segundo_valor):
    return int(primeiro_valor) - int(segundo_valor)

def calc_div(primeiro_valor,segundo_valor):
    if primeiro_valor == segundo_valor:
        return "ERROR"
    else:
        return int(primeiro_valor) / int(segundo_valor)
    
def calc_prod(primeiro_valor,segundo_valor):
    return int(primeiro_valor) * int(segundo_valor)


def calculadora():
    while True:
        print("----------------------------------------------------------")
        print("Mini Calculadora")
        print()
        print("1 -> Sum")
        print("2 -> Sub")
        print("3 -> div")
        print("4 -> Prod")
        print()
        print("0 -> ESC")
        print()
        print("----------------------------------------------------------")
        role_selected = input("Select uma das opçoes.\n")

        match role_selected:
            case "1":
                print("Na forma a + b , digite :")
                primeiro_valor = input("Digite o primeiro valor\n")
                segundo_valor = input("Digite o segundo valor\n")
                resultado = calc_sum(primeiro_valor,segundo_valor)
            case "2":
                print("Na forma a - b , digite :")
                primeiro_valor = input("Digite o primeiro valor\n")
                segundo_valor = input("Digite o segundo valor\n")
                resultado = calc_sub(primeiro_valor,segundo_valor)
            case "3":
                print("Na forma a / b , digite :")
                primeiro_valor = input("Digite o primeiro valor\n")
                segundo_valor = input("Digite o segundo valor\n")
                resultado = calc_div(primeiro_valor,segundo_valor)
            case "4":
                print("Na forma a * b , digite :")
                primeiro_valor = input("Digite o primeiro valor\n")
                segundo_valor = input("Digite o segundo valor\n")
                resultado = calc_prod(primeiro_valor,segundo_valor)
            case "0":
                resultado = "Desligando\n"
                print(resultado)
                time.sleep(1)
                print("----------------------------------------------------------")
                return
            # Caso para valores diferentes dos especificados
            case _:
                resultado = "Tente novamente, entrada não digitada corretamente \n"
        
        print("----------------------------------------------------------")
        print("O resultado obtido foi: ",resultado)
        time.sleep(2)
        print("----------------------------------------------------------")
        
# Main role
        
calculadora()