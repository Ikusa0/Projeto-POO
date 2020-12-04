from classes.socio import Socio
from classes.vip.sala_vip import SalaVip
from classes.vip.ceo import CEO


def main():
    meu_chegado = Socio("Irineu Pereira da Silva", "Técnico de T.I.", "003")
    meu_chefe = CEO("Elon Musk", "CEO de uns troço aí", "101")
    sala = SalaVip("Sala foderosa", 30)

    sala.reservar(meu_chegado, "20/11/2020 08:00", 50)
    sala.reservar(meu_chefe, "20/11/2020 08:00", 50)

    print(sala.reservas())


if __name__ == '__main__':
    main()
