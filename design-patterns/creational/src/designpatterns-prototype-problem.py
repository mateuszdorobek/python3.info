from abc import ABC, abstractmethod
from dataclasses import dataclass


class Component(ABC):
    @abstractmethod
    def render(self) -> None: ...


@dataclass
class Circle(Component):
    radius: int | None = None
    color: str | None = None

    def render(self) -> None:
        print('Rendering circle')


if __name__ == '__main__':
    a = Circle(radius=3, color='red')
    b = Circle(radius=a.radius, color=a.color)

    print(f'A: radius={a.radius}, color={a.color}')
    print(f'B: radius={b.radius}, color={b.color}')
    # A: radius=3, color=red
    # B: radius=3, color=red
