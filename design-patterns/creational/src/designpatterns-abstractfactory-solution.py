#%% Interfaces
from abc import ABC, abstractmethod


class Widget(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

class Button(Widget):
    pass

class Textbox(Widget):
    pass

class Theme(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_textbox(self) -> Textbox:
        raise NotImplementedError


#%% Material Theme
class MaterialButton(Button):
    def render(self) -> None:
        print('Material Button')

class MaterialTextbox(Textbox):
    def render(self) -> None:
        print('Material Textbox')

class MaterialTheme(Theme):
    def create_button(self) -> Button:
        return MaterialButton()

    def create_textbox(self) -> Textbox:
        return MaterialTextbox()


#%% Flat Theme
class FlatButton(Button):
    def render(self) -> None:
        print('Flat Button')

class FlatTextbox(Textbox):
    def render(self) -> None:
        print('Flat Textbox')

class FlatTheme(Theme):
    def create_button(self) -> Button:
        return FlatButton()

    def create_textbox(self) -> Textbox:
        return FlatTextbox()


#%% Main
class ContactForm:
    def render(self, theme: Theme) -> None:
        theme.create_textbox().render()
        theme.create_button().render()


if __name__ == '__main__':

    theme = FlatTheme()
    ContactForm().render(theme)
    # Flat Textbox
    # Flat Button

    theme = MaterialTheme()
    ContactForm().render(theme)
    # Material Textbox
    # Material Button
