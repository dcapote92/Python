"""
created by Daniel V.
june, 2023
python 3.10.6 64-bit
"""

from datetime import datetime, timedelta
class Horarios:
    """_summary_

    Returns:
        _type_: _description_
    """
    carga_horaria = timedelta(hours=7,minutes=20)
    batidas = []
    def __init__(self, *args):
        """
            parametros:
                args: lista de horas batidas
                (entrada, almoço, volta, saida)
            return:
                inicializaçãon
        """
        for arg in args:
            self.batidas.append(datetime.strptime(arg, '%H:%M'))

    def calcular_saida(self):
        """
        Returns:
            datetime : Hora de saida certa
        """
        primeiro_bloco = self.batidas[1] - self.batidas[0]
        result = hor.carga_horaria - primeiro_bloco
        return datetime.strftime(self.batidas[2] + result,'%H:%M')

    def calcular_horas_extra(self):
        """
        Returns:
            deltatime: horas extra
        """
        primeiro_bloco = self.batidas[1] - self.batidas[0]
        resto_a_trabalhar = hor.carga_horaria - primeiro_bloco
        saida_teorica = resto_a_trabalhar + self.batidas[2]
        extra = self.batidas[3] - saida_teorica
        if str(extra)[0] == '-':
            return False
        else:
            return extra
        
    def intra_jornada(self):
        """
        Returns:
            boolean: tem ou não intra jornada.
        """
        intra_jornada = False
        almoco = timedelta(hours = 1)
        if self.batidas[2] - self.batidas[1] < almoco:
            intra_jornada = True
        return intra_jornada
    
    def calcular_ultrapassagem_hora_extra(self):
        """_summary_
        Returns:
            deltatime : ultrapassagem_hora_extra     
        """
        maximo_permitido = timedelta(hours = 2)
        if self.calcular_horas_extra() is False:
            return False
        else:
            if self.calcular_horas_extra() > maximo_permitido:
                return  self.calcular_horas_extra() - maximo_permitido

hor = Horarios('07:00', '11:00','12:00','18:20')


        
print(hor.calcular_saida())
print(hor.calcular_horas_extra())
print(hor.intra_jornada())
print(hor.calcular_ultrapassagem_hora_extra())

