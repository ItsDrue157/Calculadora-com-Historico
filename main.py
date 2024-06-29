import time
import os
import pandas as pd
global resultado
global resultado_adicao

resultado = []
def Exibir_menu():
    Limpar_tela()
    escolha = input('''
Hello!!!, SEJA-BEMVINDO
                    
Digite 1 para fazer operacoes pelo metodo de adicao: 
Digite 2 para fazer operacoes pelo metodo de subtracao: 
digite 3 para fazer operacoes pelo metodo de divisao: (nao funcionando ainda)
''')     
    match escolha:
            case '1':
                Fazer_operacao_Adicao()
            case '2':
                Fazer_operacao_subtracao()





def Fazer_operacao_Adicao():
    Limpar_tela()
    numero1 = float(input("Digite o primeiro numero: "))
    
    numero2 = float(input("Digite o segundo numero: "))
    
    resultado_adicao = numero1 + numero2
    print(f"Resultado da adicao: {resultado_adicao}")
    
    Escrever_no_historico(resultado_adicao)
    
    escolha_adicao_menu = input("Deseja voltar ao menu? s/n ")
    
    if escolha_adicao_menu == 's':
        Voltar_ao_menu() 
    else:
        exit()

def Fazer_operacao_subtracao():
    Limpar_tela()
    numero1 = float(input("Digite o primeiro numero: "))
    
    numero2 = float(input("Digite o segundo numero: "))
    
    resultado_subtracao = numero1 - numero2
    if numero1 < 0:
        print("O primeiro valor eh menor ao segundo ")
        print('Voltando ao menu')
        time.sleep(2)
        Exibir_menu()
    
    print(f"Resultado da subtracao: {resultado_subtracao}")
    
    Escrever_no_historico(resultado_subtracao)
    
    escolha_voltar_menu = input("Deseja voltar ao menu? s/n ")
    if escolha_voltar_menu == 's':
        Voltar_ao_menu() 
    else:
        exit()
    

def Escrever_no_historico(resultado):
    with open("historico.txt", "a") as file:
        print("salvo com exito")
        file.write(f'O seu resultado da sua ultima operacao foi escrito com sucesso. e como resultado foi  {resultado}\n ')

def Voltar_ao_menu():
    print("Voltando ao menu ")
    os.system('cls')
    Exibir_menu()


def Limpar_tela():
    os.system('cls')
Exibir_menu()