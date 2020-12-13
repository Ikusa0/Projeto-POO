from classes.reserva import Reserva


def busca_binaria(target: Reserva, array: list, start: int, end: int, mode: str = "") -> int:
    if start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if target > array[mid]:
            return busca_binaria(target, array, mid + 1, end, mode)
        else:
            return busca_binaria(target, array, start, mid - 1, mode)
    return -1 if mode == "find" else start


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
                print("Choque de horário.")  # do contrário, informe a indisponibilidade
            return

        self.__lista.append(reserva)  # caso não existam reservas, basta reservar sem checagens
        print("Operação concluída.\n")

    def remover(self, reserva: Reserva) -> None:
        '''Remove uma reserva da lista.'''
        if not self.esta_vazia():
            # encontrar a posição da reserva
            index = self.encontrar_reserva(reserva)
            if index != -1:  # caso exista a reserva, remova-a
                self.__lista.pop(index)
                print("Operação concluída.\n")
            else:
                print("Reserva não encontrada.")  # do contrário, informe
            return
        print("Ainda não foram feitas reservas nesta sala.")  # se não houverem reservas feitas, informe

# ----------------------------------------------------------

# --------------------- Helper Methods ---------------------

    def esta_vazia(self) -> bool:
        '''Checa se a lista está sem reservas.'''
        return True if len(self.__lista) == 0 else False

    def esta_disponivel(self, reserva: Reserva, index: int) -> bool:
        '''Checa se existem choques nos horários entre 3 reservas consecutivas.'''
        if reserva.choque_de_horario(self.__lista[index - 1]):  # a reserva anterior dá choque
            return False
        try:
            if reserva.choque_de_horario(self.__lista[index]):  # há uma reserva no mesmo horário,
                return False                                    # ou a reserva posterior, se existir, dá choque
        except IndexError: pass
        return True  # não há choques de horários

    def encontrar_reserva(self, reserva: Reserva) -> int:
        '''Procura por uma reserva e, caso exista, retorna seu index.
        Do contrário, retorna -1.'''
        index = busca_binaria(reserva, self.__lista, 0, len(self.__lista) - 1, "find")
        if index != -1:  # existe reserva no horário
            if reserva.reservante == self.__lista[index].reservante:  # reserva foi feita pelo sócio correspondente
                return index
        return -1  # reserva não encontrada

    def existem_reservas_do_socio_no_horario(self, reserva: Reserva) -> bool:
        '''Checa se um Sócio possui uma reserva que dê choque com o horário informado.'''
        if self.esta_vazia():
            return False
        index = busca_binaria(reserva, self.__lista, 0, len(self.__lista) - 1)
        # checa se o choque foi na reserva anterior e verifica o Sócio
        if reserva.choque_de_horario(self.__lista[index - 1]):
            if self.__lista[index - 1].reservante == reserva.reservante:
                return True
        try:
            # checa se há uma reserva no mesmo horário,
            # ou se o choque foi na reserva posterior e verifica o Sócio
            if reserva.choque_de_horario(self.__lista[index]):
                if self.__lista[index].reservante == reserva.reservante:
                    return True
        except IndexError: pass
        return False

# ----------------------------------------------------------
