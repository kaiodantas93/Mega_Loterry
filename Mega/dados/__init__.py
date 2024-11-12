from random import randint
from dataclasses import dataclass, field
from typing import List

class Numeros_Escolhido:
    def __init__(self):
        self.szNome = str
        self.numeros = {}
        self.sorteado = {}
        self.sorteio_number = []

quant_jogos = 0
escolhido = Numeros_Escolhido()


def Mega_Sena(escolhido: Numeros_Escolhido):
    resultado = 0
    Digitado = 0
    while resultado < len(escolhido.numeros):
        print(f'Digite os 6 numeros do {resultado+1}º jogo')
        jogo = 0
        while jogo < 6:
            try:
                Digitado = int(input(f'Digite o {jogo+1}º numero de 1 a 60: '))
                if 0 < Digitado <= 60:
                    if not NumerosIguais(escolhido, Digitado, resultado):
                        escolhido.numeros[resultado].append(Digitado)
                        jogo += 1
                else:
                    print("Digite entre 1 e 60")

            except ValueError:
                print("Digite digitou errado, digite entre (1, 60)")

        resultado += 1
        
    for contador in range(0 , len(escolhido.numeros)):
        print(f'Os numeros do {contador+1}º jogo foram: {sorted(escolhido.numeros[contador])}')


def Sorteio(escolhido: Numeros_Escolhido):
    resultado = 0
    while resultado < 6:
        number = randint(1, 60)
        if number in escolhido.sorteio_number:
            continue
        escolhido.sorteio_number.append(number)
        print(f'{len(escolhido.sorteio_number)}º numero sorteado: {number}')
        resultado += 1
    
    print(f'Os numeros sorteados foram {sorted(escolhido.sorteio_number)}')
    Acertou(escolhido)

def Apresentacao():
    numero = 0
    resultado = False
    print("MEGA SENA")
    print("Digite seu Nome: (somente com caracteres)")
    while True:
        escolhido.szNome = str(input("Qual seu Nome: ")).lower().capitalize()
        if escolhido.szNome.isalpha():
            print(f'Seja Bem Vindo {escolhido.szNome}')
            resultado = True
            if Escolha(numero) == 2:
                Bolao()
            else:
                Mega_Sena(escolhido)
        else:
            print("Digite corretamente")

        if resultado:
            Sorteio(escolhido)
            return True


def NumerosIguais(escolhido: Numeros_Escolhido, iDigitado, contador):
    if iDigitado in escolhido.numeros[contador]:
        print("Voce digitou o mesmo numero duas vezes")
        return True


def Premio(escolhido: Numeros_Escolhido):
    for k in range(len(escolhido.sorteado)):
        if len(escolhido.sorteado[k]) == 4:
            print("Voce acertou a quadra")
        elif len(escolhido.sorteado[k]) == 5:
            print("Voce acertou a quina")
        else:
            print("Voce acertou tudo")


def Bolao():
    resultado = 0
    while resultado < len(escolhido.numeros):
        for _ in range(6):
            while True:
                number = randint(1, 60)
                if number not in escolhido.numeros[resultado]:
                    escolhido.numeros[resultado].append(number)
                else:
                    continue
                break
        resultado += 1

    print("BOLAO")
    for k in range(0, len(escolhido.numeros)):
        print(f'{k+1}º: {escolhido.numeros[k]}')



def Escolha(numero):
    global quant_jogos
    resultado = 0
    print("MENU")
    print("1 - Fazer Jogo ")
    print("2 - Bolao (20 Jogos)")
    while not resultado:
        try:
            numero = int(input("Digite a opcao: "))
            if not 0 < numero < 3:
                print("Digite a opcao corretamente")
                continue
            else:
                if numero == 2:
                    quant_jogos = 20
                    resultado = True
                    break
                while True:
                    try:
                        quant_jogos = int(input("Deseja fazer quantos jogos? (Limite 20): "))
                        if 0 < quant_jogos < 21:
                            resultado = True
                            break
                        else:
                            print("Digite de 1 a 20")
                            
                    except ValueError:
                        print("Digite um numero")
        except ValueError:
            print("Digite a opcao corretamente")

    for i in range(quant_jogos):
        escolhido.numeros[i] = []
        escolhido.sorteado[i] = []
    return numero


def Acertou(escolhido: Numeros_Escolhido):
    resultado = 0
    while resultado < len(escolhido.numeros):
        for k in range(0, 6):
            if escolhido.sorteio_number[k] in escolhido.numeros[resultado]:
                escolhido.sorteado[resultado].append(escolhido.sorteio_number[k])

        if len(escolhido.sorteado[resultado]) > 3:
            Premio(escolhido.sorteado)
        resultado += 1
        
    
