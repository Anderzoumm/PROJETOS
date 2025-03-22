
import os
import json
import time

def limpar():
    os.system("cls")


usuarios = [{"usuario":"usuario","senha":"senha"},{"usuario":"usuario_de_crack","senha":"eusouviado123"}]

while True:
    limpar()
    try:
        home = int(input("[1] - Entrar \n [2] - Registrar \n >>"))
        if home == 1:
            limpar()
            print("Login")
            usuario = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha:")
            for informacoes in usuarios:
                if informacoes["usuario"] == usuario and informacoes["senha"] == senha:
                    print("Bem vindo de volta!")
                else:
                    print("Você não está cadastrado")
            time.sleep(5)

        elif home == 2:
            limpar()
            print("Registro")
            nome = input("Digite seu nome: ")
            senha = input("Digite sua Senha:")
            informacoes = {"usuario":nome,"senha":senha}
            usuarios.append(informacoes)
            print("Você foi adicionado com sucesso")
            time.sleep(5)
        else:
            print("Número Incorreto")
    except ValueError:
        print("Valor Inserido não corresponde aos pedidos")





