"""
created by Daniel V.
june, 2023
python 3.10.6 64-bit
"""
from datetime import datetime as dt
import mysql.connector
from mysql.connector import errorcode

class Gestao:
    """Conector de BD
    """
    ip_address = ''
    usuario = ''
    senha = ''
    basedados = ''
    conector = None
    data = dt.today().strftime('%Y-%m-%d')

    def __init__(self, ip_addr, usuario, senha, basedados):
        """_summary_

        Args:
            ip_addr (_type_): _description_
            usuario (_type_): _description_
            senha (_type_): _description_
            basedados (_type_): _description_
        """
        self.ip_address = ip_addr
        self.usuario = usuario
        self.senha = senha
        self.basedados = basedados
     
    def connect(self):
        """_summary_
        Returns:
            connection: retorna a conexão
        """
        try:
            self.conector = mysql.connector.connect(
                host = self.ip_address,
                user = self.usuario,
                password = self.senha,
                database = self.basedados
            )
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Não existe essa Base de dados')
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuário ou senha errada')
            else:
                print('Erro')
        else:
            return self.conector

    def novo_dia(self, id_user):
        """_summary_
        Args:
            id (int): id do usuario
        """
        print(self.data)
        query = "INSERT INTO bateponto.Batidas (id_u, dia, entrada, almoco, volta, saida, inter_dia, intra_dia, ultrapassagem) Values(%s, %s, '00:00', '00:00', '00:00', '00:00', 0, 0, 0)"
        self.connect().cursor().execute(query,(id_user, self.data))
        self.conector.commit()

    def set_entrada(self, hora , id_user, dia):
        """_summary_
        Args:
            hora (string):  formato hh:mm
            id_user (int): id usuario
            dia (string): formato yyyy-mm-dd
        """
        query = 'UPDATE bateponto.Batidas SET entrada = %s WHERE id_u = %s and dia = %s'
        self.connect().cursor().execute(query,(hora, id_user, dia))
        self.conector.commit()

    def set_almoco(self, hora , id_user, dia):
        """_summary_
        Args:
            hora (string):  formato hh:mm
            id_user (int): id usuario
            dia (string): formato yyyy-mm-dd
        """
        query = 'UPDATE bateponto.Batidas SET almoco = %s WHERE id_u = %s and dia = %s'
        self.connect().cursor().execute(query,(hora, id_user, dia))
        self.conector.commit()

    def set_volta(self, hora , id_user, dia):
        """_summary_
        Args:
            hora (string):  formato hh:mm
            id_user (int): id usuario
            dia (string): formato yyyy-mm-dd
        """
        query = 'UPDATE bateponto.Batidas SET volta = %s WHERE id_u = %s and dia = %s'
        self.connect().cursor().execute(query,(hora, id_user, dia))
        self.conector.commit()


    def set_saida(self, hora , id_user, dia):
        """_summary_
        Args:
            hora (string):  formato hh:mm
            id_user (int): id usuario
            dia (string): formato yyyy-mm-dd
        """
        query = 'UPDATE bateponto.Batidas SET saida = %s WHERE id_u = %s and dia = %s'
        self.connect().cursor().execute(query,(hora, id_user, dia))
        self.conector.commit()

    def batidas_dia(self, id_user, dia, mes):
        """_summary_
        Args:
            id_user (int): id usuario
            dia (string): formato yyyy-mm-dd
        Returns:
            list: objeto(lista) com dados das batidas do usuario especificado no dia e mês 
        """
        cursor =self.connect().cursor()
        query = 'SELECT * FROM bateponto.Batidas WHERE id_u = %s and DAYOFMONTH(dia) = %s and MONTH(dia) = %s'
        cursor.execute(query,(id_user, dia, mes))
        resultado = list(cursor.fetchall()[0])
        resultado[1] = str(resultado[1].day)+'-'+str(resultado[1].month)+'-'+str(resultado[1].year)
        resultado[2] = str(resultado[2])
        resultado[3] = str(resultado[3])
        resultado[4] = str(resultado[4])
        resultado[5] = str(resultado[5])
        return resultado
    
    def batidas_mes(self, id_user, mes):
        """_summary_
        Args:
            id_user (int): id usuario
            mes (string): mes do ano atual

        Returns:
            list: Lista de todas as batidas no mês pelo usuario especificado
        """
        cursor =self.connect().cursor()
        query = 'SELECT * from bateponto.Batidas where id_u = %s and MONTH(dia) = %s'
        cursor.execute(query,(id_user, mes))
        resultado = list(cursor.fetchall())
        pos = 0
        for res in resultado:
            resultado[pos] = list(res)
            resultado[pos][1] = str(resultado[pos][1].day)+'-'+str(resultado[pos][1].month)+'-'+str(resultado[pos][1].year)
            resultado[pos][2] = str(resultado[pos][2])
            resultado[pos][3] = str(resultado[pos][3])
            resultado[pos][4] = str(resultado[pos][4])
            resultado[pos][5] = str(resultado[pos][5])
            pos+=1
        return resultado

    def criar_usuario(self, nome, sobrenome, cpf, usuario, senha):
        """_summary_
        Args:
            nome (string): nome do usuario
            sobrenome (string): sobrenome do usuario
            cpf (string): cpf do usuario
            usuario (string): apelido do usuario
            senha (bytes): senha do usuario
        """
        cursor =self.connect().cursor()
        query = 'INSERT INTO bateponto.Usuario (nome, sobrenome, cpf, usuario, senha, status) Values(%s, %s, %s,%s, %s,1)'
        try:
            cursor.execute(query,(nome, sobrenome, cpf, usuario, senha))
            self.conector.commit()
        except mysql.connector.Error:
            print('CPF ou apelido já cadastrado na base de dados, impossível criar usuario')
        
    def mudar_senha(self, id_user, usuario, nova_senha):
        """_summary_
        Args:
            id_user (int): id do usuário
            usuario (string): apelido do usuário
            nova_senha (bytes): nova senha
        """
        cursor =self.connect().cursor()
        query = 'UPDATE bateponto.Usuario set senha=%s where id = %s and usuario = %s'
        cursor.execute(query,(nova_senha, id_user, usuario))
        self.conector.commit()

    def apagar_usuario(self, id_user):
        """_summary_
        Args:
            id_user (int): id do usuário
        """
        cursor =self.connect().cursor()
        query = 'UPDATE bateponto.Usuario set status = 0 WHERE id = %s'
        cursor.execute(query,(id_user))
        self.conector.commit()

    def listar_usuarios(self):
        """_summary_
        Returns:
            list: usuarios na base de dados
        """
        cursor =self.connect().cursor()
        query = 'SELECT * from bateponto.Usuario'
        cursor.execute(query)
        resultado = list(cursor.fetchall())
        pos = 0
        for res in resultado:
            resultado[pos] = list(res)
            pos += 1
        return resultado
    
    
    def close(self):
        """_summary_
            Fechar conexão com BD
        """
        self.connect().close()

    def Testing(self):
        print('Olá Daniel')

con = Gestao('localhost', 'root', 'bp@admin', 'bateponto')
print(con.batidas_mes(1,'06'))
con.close()