from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Component(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass


@dataclass
class Shape(Component):
    name: str

    def move(self) -> None:
        print(f'Move {self.name}')

    def render(self) -> None:
        print(f'Render {self.name}')


@dataclass
class Group(Component):
    components: list[Component] = field(default_factory=list)

    def add(self, component: Component) -> None:
        self.components.append(component)

    def render(self) -> None:
        for component in self.components:
            component.render()

    def move(self) -> None:
        for component in self.components:
            component.move()


if __name__ == '__main__':
    group1 = Group()
    group1.add(Shape('square'))
    group1.add(Shape('rectangle'))

    group2 = Group()
    group2.add(Shape('circle'))
    group2.add(Shape('ellipse'))

    everything = Group()
    everything.add(group1)
    everything.add(group2)

    everything.render()
    # Render square
    # Render rectangle
    # Render circle
    # Render ellipse

    everything.move()
    # Move square
    # Move rectangle
    # Move circle
    # Move ellipse
