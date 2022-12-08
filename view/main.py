import kivy
from kivy.app import App
from gerenciamentoTelas import GerenciaTelas

kivy.require('2.1.0')

__version__ = "1.0"

class telasCrud(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root

if __name__ == '__main__':
    telasCrud().run()