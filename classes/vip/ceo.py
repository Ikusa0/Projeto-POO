from classes.socio import Socio


class CEO(Socio):

# ---------------- Magic Methods -----------------

    def __str__(self):
        return f'''------------------------------
             [CEO]            
Nome: {self.nome}
Cargo: {self.cargo}
Ramal: {self.ramal}
------------------------------'''

    def __repr__(self):
        return self.__str__()

# ------------------------------------------------
