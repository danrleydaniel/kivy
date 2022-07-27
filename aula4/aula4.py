from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Incrementador(BoxLayout):
	pass
	

#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		return Incrementador()

Test().run() #rodando a classe do aplicativo