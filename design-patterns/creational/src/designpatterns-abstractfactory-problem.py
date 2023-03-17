from abc import ABC, abstractmethod
from enum import Enum


#%% Interfaces
class Widget(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

class Button(Widget):
    pass

class Textbox(Widget):
    pass


#%% Material Theme
class MaterialButton(Button):
    def render(self) -> None:
        print('Material Button')

class MaterialTextbox(Textbox):
    def render(self) -> None:
        print('Material Textbox')


#%% Flat Theme
class FlatButton(Button):
    def render(self) -> None:
        print('Flat Button')

class FlatTextbox(Textbox):
    def render(self) -> None:
        print('Flat Textbox')


#%% Main
class Theme(Enum):
    MATERIAL = 1
    FLAT = 2


class ContactForm:
    def render(self, theme: Theme) -> None:
        match theme:
            case Theme.MATERIAL:
                MaterialTextbox().render()
                MaterialButton().render()
            case Theme.FLAT:
                FlatTextbox().render()
                FlatButton().render()


if __name__ == '__main__':

    ContactForm().render(Theme.FLAT)
    # Flat Textbox
    # Flat Button

    ContactForm().render(Theme.MATERIAL)
    # Material Textbox
    # Material Button
