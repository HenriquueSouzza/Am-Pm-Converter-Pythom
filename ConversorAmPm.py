#Desenvoldido por Henrique Souza para fins acadêmicos.
#Instagram: @henriquuesouzza.
#constantes e Funções não mexer !
ops = "## Oops! Algo deu errado..."
formatosAjuda = ["ajuda","AJUDA","Ajuda","/ajuda","help","/help","HELP","Help","/h","/H"]
formatosAm = ["am","Am","AM"]
formatosPm = ["pm","Pm","PM"]
formatos = ["pm","am","Pm","Am","PM","AM"]
espaco = "===================================================================================================================="
def contaPmAm(horaCalc):
    if horaCalc < 12:
        return "err"
    else:
        calc = horaCalc - 12
        resultado = str(calc)
        return resultado
def contaAmPm(horaCalc):
    if horaCalc > 12:
        return "err"
    else:
        calc = horaCalc + 12
        resultado = str(calc)
        return resultado
def bemVindo():
    print(" _____                                                   ______             ___             ")
    print("/  __ \                                                  | ___ \           / _ \            ")
    print("| /  \/  ___   _ __  __   __ ___  _ __  ___   ___   _ __ | |_/ /_ __ ___  / /_\ \ _ __ ___  ")
    print("| |     / _ \ | '_ \ \ \ / // _ \| '__|/ __| / _ \ | '__||  __/| '_ ` _ \ |  _  || '_ ` _ \ ")
    print("| \__/\| (_) || | | | \ V /|  __/| |   \__ \| (_) || |   | |   | | | | | || | | || | | | | |")
    print(" \____/ \___/ |_| |_|  \_/  \___||_|   |___/ \___/ |_|   \_|   |_| |_| |_|\_| |_/|_| |_| |_|")
    print("")
    print("## Bem-vindo!")
    print("# Para transformar a hora digite primeiro a hora que deseja transformar e depois o formato para qual deseja!")
    print("# A hora deve ser escrita nesta formatação \"XX:XX\"")
    print("# Qualquer duvida digite /h ou /help")
    print("# Desenvoldido por Henrique Souza para fins acadêmicos.")
    print("# Instagram: @henriquuesouzza.")
    print(espaco)
def ajuda():
    print(espaco)
    print("## Ajudinha")
    print("# Para transformar a hora digite primeiro a hora que deseja transformar e depois o formato para qual deseja!")
    print("# Formatação das horas -> HH:MM \"Ex: 07:50\"")
    print("# H = Horas")
    print("# M = Minutos")
    print("# Formato -> AM ou PM")
    print("# AM (Ante Meridiem) significa \"antes do meio-dia\"")
    print(" PM (Post Meridiem) significa \"após o meio-dia\"")
    print(espaco)
#começo da app
bemVindo()
#repete o codigo no final
while True:
    #inputs
    horas = input("Digite a hora: ")
    if horas in formatosAjuda:
        ajuda()
    else:
        formato = input("Digite o formato para qual deseja transformar (Am ou Pm): ")
        #verifica o formato
        if formato in formatos:
            #verifica o formato da hora e minutos
            try:
                hora = int(horas[0:2])
                minutos = int(horas[3:5])
                doisPontos = horas[2]
                #verifica hora e minutos
                if hora > 23:
                    print(espaco)
                    print(ops)
                    print("# Hora invalida...")
                    print(espaco)
                elif minutos > 59:
                    print(espaco)
                    print(ops)
                    print("# minutos invalidos...")
                    print(espaco)
                elif doisPontos != ":":
                    print(espaco)
                    print(ops)
                    print("# Formatação de hora invalida...")
                    print(espaco)
                else:
                    minutosCorrigido = horas[2:5]
                    #verifica o formato de novo e printa o resultado
                    if formato in formatosPm:
                        if contaAmPm(hora) == "err":
                            print(espaco)
                            print(ops)
                            print("# A hora já está em Pm")
                            print(espaco)
                        else:
                            print(espaco)
                            print("## A hora foi transformada de Am para Pm!")
                            print("# Resultado: "+contaAmPm(hora)+minutosCorrigido)
                    elif formato in formatosAm:
                        if contaPmAm(hora) == "err":
                            print(espaco)
                            print(ops)
                            print("# A hora já está em Am")
                            print(espaco)
                        else:
                            print(espaco)
                            print("## A hora foi transformada de Pm para Am!")
                            print("# Resultado: "+contaPmAm(hora)+minutosCorrigido)
                            print(espaco)
                    else:
                        print(espaco)
                        print(ops)
                        print("# Formato de invalido")
                        print("# Formato -> AM ou PM")
                        print(espaco)
            except ValueError:
                print(espaco)
                print(ops)
                print("# Formatação de hora invalida")
                print("# Formatação -> \"HH:MM\"")
                print("# H = Horas")
                print("# M = Minutos")
                print(espaco)
        else:
            print(espaco)
            print(ops)
            print("# Formato de invalido")
            print("# Formato -> AM ou PM")
            print(espaco)