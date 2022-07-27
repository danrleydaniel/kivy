from kivy.app import App
from kivy.uix.button import Button

#essa classe será meu aplicativo
class Test(App):
	def build(self): #esse método irá construir tudo que meu aplicativo tiver
		return Button(text="Hello, World!") #por enquanto, apenas um botão

Test().run() #rodando a classe do aplicativo