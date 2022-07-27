from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
	def __init__(self, tarefas):
		super().__init__()
		for tarefa in tarefas:
			self.add_widget(Label(text=tarefa))
		self.orientation='vertical'
	

#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		return Tarefas(['Fazer compras', 'Buscar filho', 'Alimentar cachorro', 'Jogar', 'Ler a Bíblia'])

Test().run() #rodando a classe do aplicativo