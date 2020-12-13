from classes.sala import Sala
from classes.reserva import Reserva
from classes.socio import Socio
from classes.vip.sala_vip import SalaVip
from classes.vip.ceo import CEO


class MoraisCoworking:

    def __init__(self):
        self.__socios = []
        self.__salas = []

# ------------------ Acesso a Informações ------------------

    def reservas_do_socio(self, reservante: Socio, data: str = ''):
        for sala in self.__salas:
            reservas = sala.reservas_do_socio(reservante, data if data else None)
            if reservas:
                print(f'Sala: {sala.nome}')
                for reserva in reservas:
                    print(f'• Início: {reserva.str_inicio()}',
                          f'• Duração: {reserva.duracao} min',
                          sep='\n')
        print("Operação concluída.\n")

    def reservas_da_sala(self, sala: Sala, data: str = ''):
        for reserva in sala.reservas(data if data else None):
            print(reserva)
        print("Operação concluída.\n")

    def lista_de_salas(self):
        print(*self.__salas, sep='\n')
        print("Operação concluída.\n")

    def lista_de_socios(self):
        print(*self.__socios, sep='\n')
        print("Operação concluída.\n")

# ----------------------------------------------------------

# ----------------- Métodos de Modificações ----------------

    def cadastrar_sala(self, sala: Sala) -> None:
        sala.nome = sala.nome.upper()
        if self.__sala_existe(sala):
            print('Sala já existente.\n')
            return
        self.__salas.append(sala)
        self.__salas.sort(key=lambda x: x.nome)
        print("Operação concluída.\n")

    def cadastrar_socio(self, socio: Socio) -> None:
        if self.__socio_existe(socio):
            print('Sócio já existente.\n')
            return
        self.__socios.append(socio)
        self.__socios.sort(key=lambda x: x.ramal)
        print("Operação concluída.\n")

    def fazer_reserva(self, nome_sala: str, reservante_ramal: int, data_hora: str, duracao: int):
        sala = self.buscar_sala(nome_sala)
        if sala is None:
            print('Sala inexistente.\n')
            return
        reservante = self.buscar_socio(reservante_ramal)
        if reservante is None:
            print('Sócio inexistente.\n')
            return
        for s in self.__salas:
            if s.socio_reservou_horario(reservante, data_hora, duracao):
                print(f'Choque de horário com reserva na sala {s.nome}.\n')
                return
        sala.reservar(reservante, data_hora, duracao)

    def desfazer_reserva(self, nome_sala: str, reservante_ramal: int, data_hora: str):
        sala = self.buscar_sala(nome_sala)
        if sala is None:
            print('Sala inexistente.\n')
            return
        reservante = self.buscar_socio(reservante_ramal)
        if reservante is None:
            print('Sócio inexistente.\n')
            return
        sala.desfazer_reserva(reservante, data_hora)

    def mudar_reservante(self, nome_sala: str, reservante_ramal: int, novo_reservante_ramal: int, data_hora: str):
        novo_reservante = self.buscar_socio(novo_reservante_ramal)
        if novo_reservante is None:
            print('Sócio inexistente.\n')
            return
        sala = self.buscar_sala(nome_sala)
        reservante = self.buscar_socio(reservante_ramal)
        sala.modificar_reservante(reservante, data_hora, novo_reservante)
        print("Operação concluída.\n")

    def mudar_data_hora(self, nome_sala: str, reservante_ramal: int, data_hora: str, novo_data_hora: str):
        sala = self.buscar_sala(nome_sala)
        reservante = self.buscar_socio(reservante_ramal)
        sala.modificar_horario(reservante, data_hora, novo_data_hora)
        print("Operação concluída.\n")

# ----------------------------------------------------------

# --------------------- Helper Methods ---------------------

    def __socio_existe(self, socio: Socio):
        for s in self.__socios:
            if s.ramal == socio.ramal:
                return True
        return False

    def __sala_existe(self, sala: Sala):
        for s in self.__salas:
            if s.nome == sala.nome:
                return True
        return False

    def buscar_socio(self, socio_ramal: int) -> Socio:
        for s in self.__socios:
            if s.ramal == socio_ramal:
                return s

    def buscar_sala(self, nome_sala: str) -> Sala:
        nome_sala = nome_sala.upper()
        for s in self.__salas:
            if s.nome == nome_sala:
                return s

    def reserva_existe(self, nome_sala: str, socio_ramal: int, data_hora: str):
        sala = self.buscar_sala(nome_sala)
        if sala is None:
            print('Sala inexistente.\n')
            return False
        socio = self.buscar_socio(socio_ramal)
        if socio is None:
            print('Sócio inexistente.\n')
            return False
        if sala.reserva_existe(socio, data_hora):
            return True
        print("Reserva não encontrada.")
        return False

# ----------------------------------------------------------
