from random import randint
from dataclasses import dataclass, field
from typing import List
from prettytable import PrettyTable
from time import sleep

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
        iExibicao([f'{resultado+1}º JOGO'], [f'Digite os 6 numeros'])
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
        iExibicao([f'Numeros do {contador+1}º jogo: '], [f'{sorted(escolhido.numeros[contador])}'])


def Sorteio(escolhido: Numeros_Escolhido):
    resultado = 0
    iExibicao(["MEGA SENA"], ["SORTEIO"])
    while resultado < 6:
        number = randint(1, 60)
        if number in escolhido.sorteio_number:
            continue
        escolhido.sorteio_number.append(number)
        print(f'{len(escolhido.sorteio_number)}º numero sorteado: {number}')
        sleep(2)
        resultado += 1
    
    iExibicao(["Numeros Sorteados:"], [f'{sorted(escolhido.sorteio_number)}'])
    Acertou(escolhido)

def Apresentacao():
    numero = 0
    resultado = False
    iExibicao(["MEGA SENA"], ["Digite seu Nome: (somente com caracteres)"])
    while True:
        Nome = str(input("Qual seu Nome: ")).strip()
        if all(parte.isalpha() for parte in Nome.split()):
            escolhido.szNome = ' '.join(Nome.split()).title()
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
    resultado = 0
    iacerto = 0
    for resultado in range(len(escolhido.sorteado)):
        iacerto = len(escolhido.sorteado[resultado])
        sleep(0.5)
        if iacerto > 0:
            iExibicao([f'{resultado+1}º JOGO'], [f' Acertos: {escolhido.sorteado[resultado]}'])
            if iacerto == 4:
                iExibicao([f'{resultado+1}º JOGO'], ["Voce acertou a quadra"])
            elif iacerto == 5:
                iExibicao([f'{resultado+1}º JOGO'], ["Voce acertou a quina"])
            elif iacerto == 6:
                iExibicao([f'{resultado+1}º JOGO'], ["Voce acertou tudo"])
        elif iacerto == 0:
            iExibicao([f'{resultado+1}º JOGO'], ["Voce nao acertou nenhum numero nesse jogo"])


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

    iExibicao(["ESCOLHIDO"], ["BOLAO"])
    for k in range(0, len(escolhido.numeros)):
        print(f'{k+1}º: {escolhido.numeros[k]}')
        sleep(1)



def Escolha(numero):
    global quant_jogos
    resultado = 0
    iExibicao(["MENU"], ["1 - Fazer Jogo "], ["2 - Bolao (20 Jogos)"])
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
        resultado += 1

    Premio(escolhido)


def iExibicao(Apresentacao, text1, text2=None):
    Mensagem = PrettyTable()
    Mensagem.field_names = Apresentacao
    Mensagem.add_row(text1)
    if text2 is not None:
        Mensagem.add_row(text2)
    print(Mensagem)
    Mensagem.clear()