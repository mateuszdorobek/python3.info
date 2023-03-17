"""
* Assignment: Protocol Descriptor Simple
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define descriptor class `Kelvin`
    2. Temperature must always be positive
    3. Use descriptors to check boundaries at each value modification
    4. All tests must pass
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę deskryptor `Kelvin`
    2. Temperatura musi być zawsze być dodatnia
    3. Użyj deskryptorów do sprawdzania zakresów przy każdej modyfikacji
    4. Wszystkie testy muszą przejść
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> class Temperature:
    ...     kelvin = Kelvin()

    >>> t = Temperature()
    >>> t.kelvin = 1
    >>> t.kelvin
    1
    >>> t.kelvin = -1
    Traceback (most recent call last):
    ValueError: Negative temperature
"""


# Solution
class Kelvin:
    def __get__(self, parent, parent_type):
        return parent._value

    def __set__(self, parent, new_value):
        if new_value < 0:
            raise ValueError('Negative temperature')
        parent._value = new_value


