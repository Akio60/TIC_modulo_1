# Desafio compras.py
# Rev 1.0
# Date 30/07/24
# Dev : Akio60 - Vitor Akio - vitorakoisawa@gmail.com
# 
#------------------------------------------------------------------------------------
#
# Funcionalidades
#
# Menu
# 1 - Adicionar
# 2 - Remover
# 3 - Pesquisar
# 4 - Sair
# 
# Controlde de Id gerado automaticamente e conferido se ha repeticoes
# Verificacao de elementos repetidos, somando ou variando somente sua quantidade
# Remocao do item por total
#------------------------------------------------------------------------------------
# Descricao dos produtos
# verificar unidades [kg, g, L, mL, u, m, cm] (*ainda nao foi aplicado a selecao unica dos tipos de unidade)
# Quantidade
#
#------------------------------------------------------------------------------------

# libraries
import random
import time

# Class def
class product:
    def __init__(self, id, name, quantity,  unit):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.name}, Quantidade: {self.quantity} {self.unit}"

# Function def

def verify_name():
    return input("Escreva o nome do produto:\n")

def verify_quantity():
    return int(input("Escreva a quantidade do produto a ser adicionada:\n"))

def verify_unit():
    return input("Escreva a unidade a ser inserida:\n")

def verify_id():
    return input("Escreva o id do produto a ser removido:\n")

def generate_id(products_list):
    new_id = random.randint(1,1000)
    id_miss_verify = verify_equal_id(products_list,id)
    if id_miss_verify:
        generate_id(products_list)
    else:
        return new_id

# False for non equal id in products_list, True for already existent Id
def verify_equal_id(products_list, new_id):
    for product in products_list:
        if new_id == product.id:
            return True
    return False
    
def show_list(products_list):
    if not products_list:
        print("---------------------------------------------\n")
        print("Lista vazia ou não encontrada\n")
        print("---------------------------------------------")
    else:
        print("---------------------------------------------\n")
        for product in products_list:
            print(product)
        print("\n---------------------------------------------")
    
def add2db(products_list):
    name = verify_name()
    for list in products_list:
            if name == list.name:
                time.sleep(1)
                print("---------------------------------------------\n")
                print("produto já existente na lista\n")
                print("---------------------------------------------")
                quantity = verify_quantity()
                list.quantity += quantity
                time.sleep(1)
                print("---------------------------------------------\n")
                print("produto",list.name,"atualizado\n")
                print("---------------------------------------------")
                time.sleep(1)
                return
    quantity = verify_quantity()
    unit     = verify_unit()
    new_id   = generate_id(products_list)
    new_product = product(id=new_id, name = name, quantity = quantity, unit = unit)
    products_list.append(new_product)
    time.sleep(1)
    print("---------------------------------------------\n")
    print("produto adicionado\n",new_product)
    print("---------------------------------------------")
    time.sleep(1)
    return   
               
def remove_in_list_id(products_list):
    id   = verify_id()
    for product in products_list:
            if int(id) == int(product.id):
                products_list.remove(product)
                time.sleep(1)   
                print("---------------------------------------------")
                print()
                print("Produto ",product.name," removido com sucesso")
                print()
                print("---------------------------------------------")
                time.sleep(2)   
                return
    print("---------------------------------------------")
    print()
    print("Produto não encontrado")
    print()
    print("---------------------------------------------")
    time.sleep(2)   
       
def search_in_list_name(products_list):
    name = verify_name()
    for product in products_list:
            if name == product.name:
                print(product)
                return
    print("---------------------------------------------")
    print()
    print("Produto não encontrado")
    print()
    print("---------------------------------------------")
    
def show_menu(list):
    print("Favor selecionar a opção desejada")
    print("---------------------------------------------")
    print("1 - > adicionar produtos")
    print("2 - > remover produtos por id")
    print("3 - > pesquisar produtos por nome")
    print("0 - > Sair e encerrar progama")
    print("---------------------------------------------")
    print("Lista de produtos atual :")
    show_list(list)
    print("---------------------------------------------")
   
def main():
    database=[]
    
    print("---------------------------------------------")
    print("Bem vindo ao sistema de logistica de produtos")
    print("---------------------------------------------")
    
    while True:
        print()
        show_menu(database)
        
        select_func = input("Selecione a opção desejada\n")
        
        match select_func:
            case "1": #adicionar
                add2db(database)
            case "2": #remover por id
                remove_in_list_id(database)
            case "3": #pesquisar por nome
                search_in_list_name(database)
            case "0": #sair
                return
            
            case _:
                print("Opção inválida, tente novamente")
                time.sleep(1)
            
# main
main()