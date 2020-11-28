from datetime import datetime, timedelta

from classes.socio import Socio


class Reserva:
    def __init__(self, reservante: Socio, data_hora: str, duracao: int):
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

    def inicio(self) -> str:
        return self.__data_hora.strftime("%d/%m/%Y %H:%M")

    def termino(self) -> str:
        return (self.__data_hora + timedelta(minutes=self.__duracao)).strftime("%d/%m/%Y %H:%M")

# ----------------------------------------------------------

# ----------------- Métodos de Modificações ----------------

# ----------------------------------------------------------

# --------------------- Métodos Helper ---------------------

# ----------------------------------------------------------
