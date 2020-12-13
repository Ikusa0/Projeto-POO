from classes.morais_coworking import MoraisCoworking
from classes.sala import Sala
from classes.vip.sala_vip import SalaVip
from classes.socio import Socio
from classes.vip.ceo import CEO
import sys

morais_coworking = MoraisCoworking()


# ---------------- Auxiliadores -----------------

def sim_NAO():
    escolha = input()
    return (escolha[0] == 's' or escolha[0] == 'S') if escolha else False


def SIM_nao():
    escolha = input()
    return (escolha[0] == 's' or escolha[0] == 'S') if escolha else True

# -----------------------------------------------


# ------------------ Operações ------------------

def cadastrar_nova_sala():
    print('---------- Cadastrar nova sala ----------')
    nome = input("Nome: ")
    vagas = int(input("Vagas: "))

    print("Sala VIP? [s/N]: ", end='')
    vip = sim_NAO()

    sala = SalaVip(nome, vagas) if vip else Sala(nome, vagas)

    print("\nDeseja cadastrar a sala:", sala, "[S/n]", sep='\n', end='')
    cadastrar = SIM_nao()
    if cadastrar:
        morais_coworking.cadastrar_sala(sala)
    else:
        print("Operação cancelada.\n")


def cadastrar_novo_socio():
    print('--------- Cadastrar novo sócio ----------')
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    ramal = int(input("Ramal: "))

    print("Sócio é CEO? [s/N]: ", end='')
    ceo = sim_NAO()

    socio = CEO(nome, cargo, ramal) if ceo else Socio(nome, cargo, ramal)

    print("\nDeseja cadastrar o sócio:", socio, "[S/n]", sep='\n', end='')
    cadastrar = SIM_nao()
    if cadastrar:
        morais_coworking.cadastrar_socio(socio)
    else:
        print("Operação cancelada.")


def fazer_nova_reserva():
    print('---------- Fazer nova reserva -----------')
    sala = input("Sala que irá reservar (nome): ")
    socio = int(input("Sócio reservante (ramal): "))
    data_hora = input("Data e hora da reunião: ")
    duracao = int(input("Duração (min): "))

    morais_coworking.fazer_reserva(sala, socio, data_hora, duracao)


def desfazer_reserva():
    print('----------- Desfazer reserva ------------')
    sala = input("Sala reservada (nome): ")
    socio = int(input("Sócio reservante (ramal): "))
    data_hora = input("Data e hora da reunião: ")

    morais_coworking.desfazer_reserva(sala, socio, data_hora)


def alterar_reserva():
    print('------------ Alterar reserva ------------')
    sala = input("Sala reservada (nome): ")
    socio = int(input("Sócio reservante (ramal): "))
    data_hora = input("Data e hora da reunião: ")

    if not morais_coworking.reserva_existe(sala, socio, data_hora):
        return

    print("O que deseja alterar?",
          "1 - Reservante",
          "2 - Data e Hora", sep='\n')
    escolha = input()
    if escolha == '1':
        novo_socio = int(input("Novo reservante (ramal): "))
        morais_coworking.mudar_reservante(sala, socio, novo_socio, data_hora)
    elif escolha == '2':
        novo_data_hora = input("Novas data e hora da reunião: ")
        morais_coworking.mudar_data_hora(sala, socio, data_hora, novo_data_hora)
    else:
        print("Opção Inválida.\n")


def inspecionar_socio():
    print('----------- Inspecionar sócio -----------')
    socio = morais_coworking.buscar_socio(int(input("Sócio (ramal): ")))
    if socio is not None:
        print(socio, '\n')
        print(f'Deseja ver as reservas feitas por {socio.nome.split()[0]}? [S/n] ', end='')
        deseja = SIM_nao()
        if deseja:
            data = input("Digite uma data (opcional): ")
            print(f'Reservas de {socio.nome}', f' no dia {data}' if data else '', ':', sep='', end='\n\n')
            morais_coworking.reservas_do_socio(socio, data)
        return
    print('Sócio inexistente.\n')


def inspecionar_sala():
    print('----------- Inspecionar sala ------------')
    sala = morais_coworking.buscar_sala(input("Sala (nome): "))
    if sala is not None:
        print(sala, '\n')
        print(f'Deseja ver as reservas feitas na sala {sala.nome}? [S/n] ', end='')
        deseja = SIM_nao()
        if deseja:
            data = input("Digite uma data (opcional): ")
            print(f'Reservas de {sala.nome}', f' no dia {data}' if data else '', ':', sep='', end='\n\n')
            morais_coworking.reservas_da_sala(sala, data)
        return
    print('Sala inexistente.\n')


def lista_de_salas():
    morais_coworking.lista_de_salas()


def lista_de_socios():
    morais_coworking.lista_de_socios()

# -----------------------------------------------


# ---------------- Tela Inicial -----------------

def switch_tela_inicial(escolha):
    switch = {'1': cadastrar_nova_sala,
              '2': cadastrar_novo_socio,
              '3': fazer_nova_reserva,
              '4': desfazer_reserva,
              '5': alterar_reserva,
              '6': inspecionar_socio,
              '7': inspecionar_sala,
              '8': lista_de_salas,
              '9': lista_de_socios,
              'exit': sys.exit}
    return switch.get(escolha, "Opção Inválida.\n")


def tela_inicial():
    print("O que deseja fazer?\n")
    print("1 - Cadastrar nova sala",
          "2 - Cadastrar novo sócio",
          "3 - Fazer nova reserva",
          "4 - Desfazer reserva",
          "5 - Alterar reserva",
          "6 - Inspecionar sócio",
          "7 - Inspecionar sala",
          "8 - Lista de salas",
          "9 - Lista de sócios", sep='\n')
    escolha = switch_tela_inicial(input())
    try: escolha()
    except TypeError: print(escolha)

# -----------------------------------------------


def main():
    while True:
        try:
            tela_inicial()
            input()
        except (TypeError, ValueError) as Error:
            print("Inválido.\n")


if __name__ == '__main__':
    main()
