from classes.sala import Sala
from classes.vip.ceo import CEO


class SalaVip(Sala):

# ----------------- Métodos de Modificações ----------------

    def reservar(self, reservante: CEO, data_hora: str, duracao: int) -> None:
        if type(reservante) == CEO:
            super().reservar(reservante, data_hora, duracao)
            return
        print("Reservas em salas VIP são permitidas apenas para Sócios CEO.")

    def modificar_reservante(self, reservante_anterior: CEO, data_hora: str, novo_reservante: CEO) -> None:
        if type(novo_reservante) == CEO:
            super().modificar_reservante(reservante_anterior, data_hora, novo_reservante)
            return
        print("Reservas em salas VIP são permitidas apenas para Sócios CEO.")

# ----------------------------------------------------------

# --------------------- Magic Methods ----------------------

    def __str__(self):
        return f'''------------------------------
           [Sala VIP]
Nome: {self.nome}
Vagas: {self.vagas}
------------------------------'''

    def __repr__(self):
        return self.__str__()

# ----------------------------------------------------------
