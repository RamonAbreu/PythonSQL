from conexao import SQLPython
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


Window.size = 300, 500



my_conn = SQLPython()
#my_conn.cursor.execute(my_conn.selecionar())
my_conn.cursor.execute(my_conn.sel)
print("Conexão bem sucedida")
valor = my_conn.cursor.fetchone()
#valor = str(my_conn.cursor(my_conn.dados_conn()).fetchone)
print(valor)




class PainelInicial(Screen):
    pass
    #def on_kv_post(self, base_widget):
    #    print(self.parent.ids.painel_inicial.ids)
class Eldorado(Screen):
    pass
class CidadeIndustrial(Screen):
    pass
class VilaOeste(Screen):
    pass
class Gameleira(Screen):
    pass
class Calafate(Screen):
    pass
class CarlosPrates(Screen):
    pass
class Lagoinha(Screen):
    pass

class PainelCentral(Screen):

    def on_enter(self, *args):
        self.parent.ids.painel_central.ids.id_uctv1.text = ("Trem sentido vilarinho: \n\n "+"Tempo: \r"+str(valor[0])+"min"
                                                            +"\n Carros: 8\n"+"Ar Condicionado: Não")
        self.parent.ids.painel_central.ids.id_uctv2.text = "Trem sentido Eldorado: \n"+str(valor[1])+"min"

    def seta_press(self):
        self.ids.id_seta.source = 'seta_press.jfif'
        #print(self.parent.ids.painel_central.ids)
    def seta_release(self):
        self.ids.id_seta.source = 'seta.jfif'
    def abrir_imagem(self):
        self.ids.id_imgcaf.source = 'seta.jfif'

class SantaEfigenia(Screen):
    pass
class SantaTereza(Screen):
    pass
class Horto(Screen):
    pass
class SantaInes(Screen):
    pass
class JoseCandido(Screen):
    pass
class MinasShopping(Screen):
    pass
class SaoGabriel(Screen):
    pass
class PrimeiroDeMaio(Screen):
    pass
class WaldomiroLobo(Screen):
    pass
class Floramar(Screen):
    pass
class PainelVilarinho(Screen):
    pass

class PainelPrincipal(ScreenManager):
    pass

GUI = Builder.load_file("meupainel.kv")

class MeuPainel(App):

    def build(self):
        return GUI


if __name__ == "__main__":
    MeuPainel().run()
