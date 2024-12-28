from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.image import AsyncImage

class ContadorApp(App):
    def build(self):
        self.contador = 0
        layout = BoxLayout(orientation='vertical')
        self.btn = Button(text='Clique aqui 300 vezes',background_color=(0,1,0,1), color=(5,15,36,1))
        self.lbl = Label(text='Você clicou 0 vezes')
        self.btn.bind(on_press=self.incrementar)
        self.img = AsyncImage(source='https://images.pexels.com/photos/29930436/pexels-photo-29930436.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 
        size_hint=(None, None), size=(800, 400))
        self.img.opacity = 0
        layout.add_widget(self.img)
        layout.add_widget(self.btn)
        layout.add_widget(self.lbl)

        return layout
    
    def incrementar(self, instance):
        self.contador += 1
        self.lbl.text = f'Você clicou {self.contador} vezes'
        if self.contador >= 300:
            self.btn = Button(text='Clique aqui',background_color=(6,320,324), color=(99,35,36,25))
            print('Parabéns')
            self.btn.disabled = True
            self.img.opacity = 1
            Clock.schedule_once(self.fade_in, 0.5)


    def fade_in(self, dt):
        self.img.opacity += 0.1
        if self.img.opacity < 1:
            Clock.schedule_once(self.fade_in, 0.05)


if __name__ == '__main__':
    ContadorApp().run()