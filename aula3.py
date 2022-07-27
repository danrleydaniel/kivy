from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		box = BoxLayout(orientation="vertical") 

		#BOTÃO COM FUNCIONALIDADE:
		button = Button(text="Botão 1", font_size=30, on_release=self.incrementar) #argumento 'on_release' recebe a função que vai ser executada quando o botão for soltado
		label = Label(text="Texto 1", font_size=30)

		box.add_widget(button) 
		box.add_widget(label)

		box2 = BoxLayout()

		return box 

	def incrementar(self, button):
		button.text = "Soltei"

Test().run() #rodando a classe do aplicativo