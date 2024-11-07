from random import randint
from dataclasses import dataclass, field
from typing import List

class Numeros_Escolhido:
    szNome = str
    numeros = []
    sorteado = []
    listaSorteio = []


escolhido = Numeros_Escolhido()


def Mega_Sena(escolhido: Numeros_Escolhido):
    resultado = 0
    Digitado = 0
    while resultado < 6:
        try:
            Digitado = int(input(f'Digite o {resultado+1}º numero de 1 a 60: ')) 
            if 0 < Digitado <= 60:
                if not NumerosIguais(escolhido, Digitado):
                    escolhido.numeros.append(Digitado)
                    resultado += 1                    
            else:
                print("Digite entre 1 e 60")

        except ValueError:
            print("Digite digitou errado, digite entre (1, 60)")

    print(f'Os numeros escolhidos foram {sorted(escolhido.numeros)}')
    Sorteio(escolhido)


def Sorteio(escolhido: Numeros_Escolhido):
    for numero in range(1, 7):
        while True:
            number = randint(1, 60)
            for jogado in escolhido.listaSorteio:
                if jogado == number:
                    continue
            escolhido.listaSorteio.append(number)
            print(f'{len(escolhido.listaSorteio)} numero sorteado: {number}')
            break
        if NumerosIguais(escolhido, number):
            print(f'Voce acertou o numero {number}')    
            escolhido.sorteado.append(number)

    print(f'Os numeros sorteados foram {sorted(escolhido.listaSorteio)}')
    if len(escolhido.sorteado) == 0:
        print("Voce nao acertou nenhum numero")
    elif len(escolhido.sorteado) > 3:
        Premio(escolhido.sorteado)
    else:
        print(f'Voce acertou {len(escolhido.sorteado)} numeros {sorted(escolhido.sorteado)}')


def Apresentacao():
    print("MEGA SENA")
    while True:
        Nome = str(input("Qual seu Nome: ")).lower().capitalize()
        escolhido.szNome = Nome
        if Nome.isalpha():
            print(f'Seja Bem Vindo {escolhido.szNome}')
            Mega_Sena(escolhido)
            return True
        else:
            print("Digite corretamente")


def NumerosIguais(escolhido: Numeros_Escolhido, iDigitado):
    for k in escolhido.numeros:
        if k == iDigitado:
            print("Voce digitou o mesmo numero duas vezes")
            return True
        

def Premio(escolhido: Numeros_Escolhido):
    if escolhido.listaSorteio == 4:
        print("Voce acertou a quadra")
    elif escolhido.listaSorteio == 5:
        print("Voce acertou a quina")
    else:
        print("Voce acertou tudo")
    