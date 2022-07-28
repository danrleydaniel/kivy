from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
	def __init__(self, tarefas, **kwargs):
		super().__init__(**kwargs)
		for tarefa in tarefas:
			self.ids.box.add_widget(Tarefa(text=tarefa))


class Tarefa(BoxLayout):
	def __init__(self, text='', **kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text


#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		return Tarefas(['Fazer compras', 'Buscar filho', 'Alimentar cachorro', 'Jogar', 'Ler a Bíblia'])

Test().run() #rodando a classe do aplicativo