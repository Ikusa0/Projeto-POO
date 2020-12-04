from datetime import datetime, timedelta

from classes.socio import Socio


class Reserva:
    def __init__(self, reservante: Socio, data_hora: str, duracao: int):
        '''data_hora ex.: 20/11/2020 14:30
           duração em minutos.'''
        self.__reservante = reservante
        self.__data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        self.__duracao = duracao

# ------------------ Acesso aos Atributos ------------------

    def get_reservante(self):
        return self.__reservante

    def set_reservante(self, novo_reservante: Socio):
        self.__reservante = novo_reservante

    def get_data_hora(self):
        return self.__data_hora

    def set_data_hora(self, novo_data_hora: str):
        self.__data_hora = novo_data_hora

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, novo_duracao: Socio):
        self.__duracao = novo_duracao

    reservante = property(get_reservante, set_reservante)
    data_hora = property(get_data_hora, set_data_hora)
    duracao = property(get_duracao, set_duracao)

# ----------------------------------------------------------

# ------------------ Acesso a Informações ------------------

    def inicio(self) -> datetime:
        '''Retorna o datetime de início da reserva.'''
        return self.__data_hora

    def termino(self) -> datetime:
        '''Retorna o datetime de término da reserva.'''
        return self.__data_hora + timedelta(minutes=self.__duracao)

    def str_inicio(self) -> str:
        '''Retorna a data e hora de início da reserva.'''
        return self.__data_hora.strftime("%d/%m/%Y %H:%M")

    def str_termino(self) -> str:
        '''Retorna a data e hora de término da reserva.'''
        return (self.__data_hora + timedelta(minutes=self.__duracao)).strftime("%d/%m/%Y %H:%M")

    def choque_de_horario(self, other) -> bool:
        '''Checa se há choque de horário entre esta e outra reserva.'''
        if self.termino() >= other.inicio():
            if self.termino() <= other.termino():
                return True

        if self.inicio() <= other.termino():
            if self.termino() >= other.termino():
                return True

        return False

# ----------------------------------------------------------

# --------------------- Magic Methods ----------------------

    def __eq__(self, other):
        return self.__data_hora == other.__data_hora

    def __lt__(self, other):
        return self.__data_hora < other.__data_hora

    def __gt__(self, other):
        return self.__data_hora > other.__data_hora

    def __str__(self):
        return f'''------------------------------
Reservante: {self.__reservante}
Inicio: {self.str_inicio()}
Término: {self.str_termino()}
------------------------------'''

# ----------------------------------------------------------
