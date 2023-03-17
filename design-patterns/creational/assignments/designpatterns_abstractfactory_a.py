"""
* Assignment: DesignPatterns Creational AbstractFactory
* Complexity: easy
* Lines of code: 70 lines
* Time: 21 min

English:
    1. Implement Abstract Factory pattern
    2. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Abstract Factory
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> main(Platform.iOS)
    iOS Textbox username
    iOS Textbox password
    iOS Button submit

    >>> main(Platform.Android)
    Android Textbox username
    Android Textbox password
    Android Button submit
"""
from dataclasses import dataclass
from enum import Enum


class Platform(Enum):
    iOS = 'iOS'
    Android = 'Android'


@dataclass
class Button:
    name: str

    def render(self, platform: Platform):
        if platform is platform.iOS:
            print(f'iOS Button {self.name}')
        elif platform is platform.Android:
            print(f'Android Button {self.name}')

@dataclass
class Textbox:
    name: str

    def render(self, platform: Platform):
        if platform is platform.iOS:
            print(f'iOS Textbox {self.name}')
        elif platform is platform.Android:
            print(f'Android Textbox {self.name}')


def main(platform: Platform):
    Textbox('username').render(platform)
    Textbox('password').render(platform)
    Button('submit').render(platform)


# Solution

#%% Interfaces
from abc import ABC, abstractmethod


class UIElement(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

@dataclass
class Button(UIElement):
    name: str

@dataclass
class Textbox(UIElement):
    name: str

class OS(ABC):
    @abstractmethod
    def create_button(self, name: str) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_textbox(self, name: str) -> Textbox:
        raise NotImplementedError


#%% Android
class AndroidButton(Button):
    def render(self) -> None:
        print(f'Android Button {self.name}')

class AndroidTextbox(Textbox):
    def render(self) -> None:
        print(f'Android Textbox {self.name}')

class Android(OS):
    def create_button(self, name: str) -> Button:
        return AndroidButton(name)

    def create_textbox(self, name: str) -> Textbox:
        return AndroidTextbox(name)


#%% iOS
class iOSButton(Button):
    def render(self) -> None:
        print(f'iOS Button {self.name}')

class iOSTextbox(Textbox):
    def render(self) -> None:
        print(f'iOS Textbox {self.name}')

class iOS(OS):
    def create_button(self, name: str) -> Button:
        return iOSButton(name)

    def create_textbox(self, name: str) -> Textbox:
        return iOSTextbox(name)


#%% Main
class Platform(Enum):
    iOS = iOS()
    Android = Android()


def main(platform: Platform):
    os = platform.value
    os.create_textbox('username').render()
    os.create_textbox('password').render()
    os.create_button('submit').render()
