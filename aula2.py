from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		box = BoxLayout(orientation="vertical") #BoxLayout aglomerará todos os widgets que eu quiser colocar na tela.
		#O argumento 'orientation' diz em qual posição os widgets vão ficar (vertical, horizontal)

		button = Button(text="Botão 1") #criando um widget
		label = Label(text="Texto 1")

		box.add_widget(button) #acrescentando ao BoxLayout
		box.add_widget(label)

		box2 = BoxLayout() #BoxLayout aglomerará todos os widgets que eu quiser colocar na tela.
		#O argumento 'orientation' diz em qual posição os widgets vão ficar (vertical, horizontal)

		#ACRESCENTANDO UM BOX DENTRO DE UM BOX:
		button2 = Button(text="Botão 2")
		label2 = Label(text="Texto 2")

		box2.add_widget(button2)
		box2.add_widget(label2)

		box.add_widget(box2)

		return box #retorna a box em vez de um widget específico

Test().run() #rodando a classe do aplicativo