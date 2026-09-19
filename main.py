from kivy.app import App
from kivy.uix.label import Label

class CtlmApp(App):
    def build(self):
        return Label(text='Jaanega India Tabhi To Bachayega India')

if __name__ == '__main__':
    CtlmApp().run()
