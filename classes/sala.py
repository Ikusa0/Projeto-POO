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

    def __reservas_todas(self) -> list:
        '''Retorna uma lista contendo todas as reservas.'''
        reservas = []
        for reserva in self.__reservas.lista:
            reservas.append(reserva)
        return reservas

    def __reservas_data(self, data: str) -> list:
        '''Retorna uma lista contendo todas as reservas de um dia específico.'''
        reservas = []
        for reserva in self.__reservas.lista:
            if reserva.str_data_inicio() == data:
                reservas.append(reserva)
        return reservas

    def reservas(self, data: str = None) -> list:
        '''Retorna uma lista contendo todas as reservas, ou as de um dia específico.'''
        if data is not None:
            return self.__reservas_data(data)
        return self.__reservas_todas()

    def __reservas_do_socio_data(self, reservante: Socio, data: str) -> list:
        '''Retorna uma lista contendo todas as reservas de um Sócio em determinada data.'''
        reservas = []
        for reserva in self.__reservas.lista:
            # Checa se há reservas do Sócio no dia.
            if reserva.str_data_inicio() == data and reserva.reservante == reservante:
                reservas.append(reserva)
        return reservas

    def __reservas_do_socio_todas(self, reservante: Socio) -> list:
        '''Retorna uma lista contendo todas as reservas de um Sócio.'''
        reservas = []
        for reserva in self.__reservas.lista:
            # Checa se há reservas do Sócio.
            if reserva.reservante == reservante:
                reservas.append(reserva)
        return reservas

    def reservas_do_socio(self, reservante: Socio, data: str = None) -> list:
        '''Retorna uma lista de reservas de determinado Sócio, podendo ter um dia específico.'''
        if data is not None:
            return self.__reservas_do_socio_data(reservante, data)
        return self.__reservas_do_socio_todas(reservante)

# ----------------------------------------------------------

# ----------------- Métodos de Modificações ----------------

    def reservar(self, reservante: Socio, data_hora: str, duracao: int) -> None:
        '''Faz uma nova reserva.'''
        self.__reservas.adicionar(Reserva(reservante, data_hora, duracao))

    def desfazer_reserva(self, reservante: Socio, data_hora: str):
        '''Remove uma reserva feita.'''
        self.__reservas.remover(Reserva(reservante, data_hora))

    def modificar_reservante(self, reservante_anterior: Socio, data_hora: str, novo_reservante: Socio) -> None:
        '''Muda o reservante de uma reserva feita.'''
        index = self.__reservas.encontrar_reserva(Reserva(reservante_anterior, data_hora))
        if index != -1:
            self.__reservas.lista[index].reservante = novo_reservante
            return
        print("Reserva não encontrada.")

    def modificar_horario(self, reservante: Socio, data_hora_anterior: str, novo_data_hora: str) -> None:
        '''Muda a data e horário de uma reserva feita.'''
        index = self.__reservas.encontrar_reserva(Reserva(reservante, data_hora_anterior))
        if index != -1:
            self.__reservas.lista[index].data_hora = novo_data_hora
            return
        print("Reserva não encontrada.")

# ----------------------------------------------------------

# --------------------- Magic Methods ----------------------

    def __str__(self):
        return f'''------------------------------
           [Sala Comum]
Nome: {self.__nome}
Vagas: {self.__vagas}
------------------------------'''

    def __repr__(self):
        return self.__str__()

# ----------------------------------------------------------

# --------------------- Helper Methods ---------------------

    def socio_reservou_horario(self, reservante: Socio, data_hora: str, duracao: int):
        '''Checa se um Sócio possui uma reserva que dê choque com o horário informado.'''
        return self.__reservas.existem_reservas_do_socio_no_horario(Reserva(reservante, data_hora, duracao))

    def reserva_existe(self, reservante: Socio, data_hora: str):
        '''Checa se existe uma reserva feita pelo sócio em dado horário.'''
        return True if self.__reservas.encontrar_reserva(Reserva(reservante, data_hora)) != -1 else False
# ----------------------------------------------------------
