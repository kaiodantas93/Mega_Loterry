def Apresentacao():
    print("MEGA SENA")
    while True:
        szNome = str(input("Qual seu Nome: ")).lower().capitalize()
        try:
            if szNome.isalpha():
                print(f'Seja Bem Vindo {szNome}')
                Mega_Sena()
                return True
        except:
            continue


def Mega_Sena():
   #Iniciando
