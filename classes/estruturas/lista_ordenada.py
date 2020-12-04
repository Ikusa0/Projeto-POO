from classes.reserva import Reserva


def busca_binaria(target: Reserva, array: list, start: int, end: int) -> int:
    if start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return -1
        if target > array[mid]:
            return busca_binaria(target, array, mid + 1, end)
        else:
            return busca_binaria(target, array, start, mid - 1)
    return start


class ListaOrdenada:
    def __init__(self):
        self.__lista = []

# ------------------ Acesso aos Atributos ------------------

    @property
    def lista(self):
        return self.__lista

# ----------------------------------------------------------

# ----------------- Métodos de Modificações ----------------

    def adicionar(self, reserva: Reserva) -> None:
        '''Adiciona uma nova reserva à lista.'''
        if not self.esta_vazia():
            # encontrar uma posição onde possa inserir uma reserva mantendo a ordem de maior para menor
            index = busca_binaria(reserva, self.__lista, 0, len(self.__lista) - 1)
            if self.esta_disponivel(reserva, index):  # caso haja disponibilidade de horário, reserve
                self.__lista.insert(index, reserva)
            else:
                print("choque de horário")  # do contrário, informe a indisponibilidade
            return

        self.__lista.append(reserva)  # caso não existam reservas, basta reservar sem checagens

# ----------------------------------------------------------

# --------------------- Helper Methods ---------------------

    def esta_vazia(self) -> bool:
        '''Checa se a lista está sem reservas.'''
        return True if len(self.__lista) == 0 else False

    def esta_disponivel(self, reserva: Reserva, index: int) -> bool:
        '''Checa se existem choques nos horários entre 3 reservas consecutivas.'''
        if index == -1:  # há uma reserva no mesmo horário
            return False
        if reserva.choque_de_horario(self.__lista[index - 1]):  # a reserva anterior dá choque
            return False
        try:
            if reserva.choque_de_horario(self.__lista[index]):  # a reserva posterior, se existir, dá choque
                return False
        except IndexError: pass
        return True  # não há choques de horários

# ----------------------------------------------------------
