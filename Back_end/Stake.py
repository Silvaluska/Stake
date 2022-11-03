from cgitb import text
from turtle import onrelease
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import mods
import os
from time import sleep

class teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        botao = Button(text='Botão!!', font_size=30, on_release=self.incrementar)
        self.label = Label(text='0', font_size=30)
        box.add_widget(botao)
        box.add_widget(self.label)
        return box
    
    def incrementar(self, botao):
        novo_label =int(self.label.text) + 1 
        self.label.text = str(novo_label)

teste().run()

'''while True:
    r = mods.menu()
    if r == '1':
        mods.spt()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '2':
        mods.diametro()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '3':
        mods.solos()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '4':
        tipo = mods.tipo()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '5':
        mods.calculo()
    elif r == '6':
        break
    else:
        r = input('Escolha uma opção: ')
    sleep(2)'''