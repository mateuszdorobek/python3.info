from typing import Self
from dataclasses import dataclass, field


@dataclass
class Shape:
    name: str

    def render(self) -> None:
        print(f'Render {self.name}')

    def move(self) -> None:
        print(f'Move {self.name}')


@dataclass
class Group:
    objects: list[Shape | Self] = field(default_factory=list)

    def add(self, obj: Shape | Self) -> None:
        self.objects.append(obj)

    def render(self) -> None:
        for obj in self.objects:
            obj.render()

    def move(self) -> None:
        for obj in self.objects:
            obj.move()


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
