from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window
from kivy.lang import Builder
from .lib.gestbd import Gestao


class Login(MDScreen):
    'Login'

class Central(MDScreen):
    'Central'

class Pontos(MDScreen):
    'Pontos'

class Relatorio(MDScreen):
    # def on_load(self):
    #     con = Gestao('localhost', 'root', 'bp@admin', 'bateponto')
    #     for dia in con.batidas_mes(1, '06'):
    #         self.root.ids.lista.add_widget(OneLineListItem(text='[size=9]'+str(dia)+'[/size]'))
    'Relatorio'

class GestorTelas(ScreenManager):
    """_summary_

    Args:
        ScreenManager (_type_): _description_
    """

class PontoCertoApp(MDApp):
    """_summary_

    Args:
        MDApp (_type_): _description_
    """
    def build(self):
        Window.size = [300, 600]
        scr_man = Builder.load_file('uix.kv')
        return Relatorio()
    
    def check_usuario(self, usuario, senha, card):
        """_summary_

        Args:
            usuario (_type_): _description_
            senha (_type_): _description_
            card (_type_): _description_
        """
        con = Gestao('localhost', 'root', 'bp@admin', 'bateponto')
        user = ''
        
        for usr in con.listar_usuarios():
            if usr[4] == usuario and usr[5] == senha:
                card.size_hint = 1, 1
                self.root.current = 'central'
                
            elif usr[4] != usuario and usr[5] != senha:
                pass
            elif usr[4] == usuario and usr[5] != senha:
                pass
        print(user)
    
    def tela_pontos(self):
        """_summary_
        """
        self.root.current = 'pontos'
        
    def tela_central(self):
        """_summary_
        """
        self.root.current = 'central'
    
    def tela_relatorio(self):
        """_summary_
        """
        self.root.current = 'relatorio'
    
    def tela_calendario(self):
        """_summary_
        """
        self.root.current = 'calendario'    
        
    def get_time_entrada(self, instance, time):
        """_summary_

        Args:
            instance (_type_): _description_
            time (_type_): _description_
        """
        self.root.get_screen('pontos').ids.btnEntrada.text = str(time.strftime('%H:%M:%S'))
        
    def get_time_saida_k3(self, instance, time):
        """_summary_

        Args:
            instance (_type_): _description_
            time (_type_): _description_
        """
        self.root.get_screen('pontos').ids.btnSaida_k3.text = str(time.strftime('%H:%M:%S'))
        
    def get_time_volta_k3(self, instance, time):
        """_summary_

        Args:
            instance (_type_): _description_
            time (_type_): _description_
        """
        self.root.get_screen('pontos').ids.btnVolta_k3.text = str(time.strftime('%H:%M:%S'))
        
    def get_time_saida(self, instance, time):
        """_summary_

        Args:
            instance (_type_): _description_
            time (_type_): _description_
        """
        self.root.get_screen('pontos').ids.btnSaida.text = str(time.strftime('%H:%M:%S'))
        
    def on_cancel(self, instance, time):
        """_summary_

        Args:
            instance (_type_): _description_
            time (_type_): _description_
        """
        pass
    
    def show_time_picker_entrada(self):
        """_summary_
        """
        time_dialog = MDTimePicker()
        time_dialog.title = 'Escolha o horário'
        time_dialog.bind(on_cancel = self.on_cancel, time = self.get_time_entrada)
        time_dialog.open()
    
    def show_time_picker_saida_k3(self):
        """_summary_
        """
        time_dialog = MDTimePicker()
        time_dialog.title = 'Escolha o horário'
        time_dialog.bind(on_cancel = self.on_cancel, time = self.get_time_saida_k3)
        time_dialog.open()
    
    def show_time_picker_volta_k3(self):
        """_summary_
        """
        time_dialog = MDTimePicker()
        time_dialog.title = 'Escolha o horário'
        time_dialog.bind(on_cancel = self.on_cancel, time = self.get_time_volta_k3)
        time_dialog.open()
    
    def show_time_picker_saida(self):
        """_summary_
        """
        time_dialog = MDTimePicker()
        time_dialog.title = 'Escolha o horário'
        time_dialog.bind(on_cancel = self.on_cancel, time = self.get_time_saida)
        time_dialog.open()
    
    
    def salva_ponto(self, entrada, saida_k3, volta_k3, saida):
        """_summary_
        Args:
            entrada (_type_): _description_
            saida_k3 (_type_): _description_
            volta_k3 (_type_): _description_
            saida (_type_): _description_
        """
        # Gestao.set_entrada(entrada.text,1, datetime.today().date())
        pass
    
    def on_start(self):
        con = Gestao('localhost', 'root', 'bp@admin', 'bateponto')
        for dia in con.batidas_mes(1, '06'):
            # self.root.get_screen('relatorio').ids.lista.add_widget(OneLineListItem(text=str(dia)))
            self.root.ids.lista.add_widget(OneLineListItem(text=str(dia)))
    
PontoCertoApp().run()