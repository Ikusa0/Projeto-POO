from classes.estruturas.lista_ordenada import ListaOrdenada
from classes.reserva import Reserva
from classes.socio import Socio


class Sala:
    def __init__(self, nome: str, vagas: int):
        self.__nome = nome
        self.__vagas = vagas
        self.__reservas = ListaOrdenada()

# ------------------ Acesso aos Atributos ------------------

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome: str):
        self.__nome = novo_nome

    def get_vagas(self):
        return self.__vagas

    def set_vagas(self, novo_vagas: str):
        self.__vagas = novo_vagas

    nome = property(get_nome, set_nome)
    vagas = property(get_vagas, set_vagas)

# ----------------------------------------------------------

# ------------------ Acesso a Informações ------------------

    def reservas(self) -> str:
        '''Retorna uma string contendo todas as reservas.'''
        reservas_str = []
        for reserva in self.__reservas.lista:
            reservas_str.append(str(reserva))
        return '\n'.join(reservas_str)

# ----------------------------------------------------------

# ----------------- Métodos de Modificações ----------------

    def reservar(self, reservante: Socio, data_hora: str, duracao: int) -> None:
        '''Faz uma nova reserva.'''
        self.__reservas.adicionar(Reserva(reservante, data_hora, duracao))

# ----------------------------------------------------------
