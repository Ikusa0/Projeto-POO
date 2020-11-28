from classes.sala import Sala
from classes.socio import Socio


def main():
    salinha1 = Sala("Sala de Reuniões 1", 10)
    meu_chegado1 = Socio("Irineu Pereira da Silva", "Técnico de T.I.", "003")

    salinha1.reservar(meu_chegado1, "20/11/2020 08:00", 50)
    salinha1.reservar(meu_chegado1, "27/11/2020 13:30", 50)

    print(salinha1.reservas())


if __name__ == '__main__':
    main()
