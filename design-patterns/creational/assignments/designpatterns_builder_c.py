"""
* Assignment: DesignPatterns Creational BuilderTexture
* Complexity: easy
* Lines of code: 18 lines
* Time: 8 min

English:
    1. Create class `Texture`
    2. Use builder pattern to set:
        a. `file: str`
        b. `width: int` value greater than 0
        c. `height: int` value greater than 0
        d. `quality: int` from 1 to 100 percent
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Texture`
    2. Użyj wzorca builder, aby ustawić:
        a. `file: str`
        b. `width: int` wartość większa niż 0
        c. `height: int` wartość większa niż 0
        d. `quality: int` od 1 do 100 procent
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = (
    ...     Texture()
    ...     .with_file('img/dragon/alive.png')
    ...     .with_height(100)
    ...     .with_width(50)
    ...     .with_quality(75)
    ... )

    >>> vars(result)
    {'file': 'img/dragon/alive.png', 'height': 100, 'width': 50, 'quality': 75}
"""

class Texture:
    file: str
    width: int
    height: int
    quality: int


# Solution
class Texture:
    file: str
    width: int
    height: int
    quality: int

    def with_file(self, file):
        self.file = file
        return self

    def with_width(self, width):
        if width < 0:
            raise ValueError
        self.width = width
        return self

    def with_height(self, height):
        if height < 0:
            raise ValueError
        self.height = height
        return self

    def with_quality(self, quality):
        if not 1 <= quality < 100:
            raise ValueError
        self.quality = quality
        return self
