from dataclasses import dataclass
from typing import Self
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self) -> None: ...

    @abstractmethod
    def clone(self) -> Self: ...


@dataclass
class Circle(Component):
    radius: int | None = None
    color: str | None = None

    def clone(self) -> Self:
        new = Circle()
        new.radius = self.radius
        new.color = self.color
        return new

    def render(self) -> None:
        print('Rendering circle')


if __name__ == '__main__':
    a = Circle(radius=3, color='red')
    b = a.clone()

    print(f'A: radius={a.radius}, color={a.color}')
    print(f'B: radius={b.radius}, color={b.color}')
    # A: radius=3, color=red
    # B: radius=3, color=red
