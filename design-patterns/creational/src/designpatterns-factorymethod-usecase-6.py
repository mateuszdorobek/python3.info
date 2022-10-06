from abc import ABCMeta, abstractproperty, abstractmethod
from dataclasses import dataclass


@dataclass
class ConfigParser(metaclass=ABCMeta):
    _filename: str

    @abstractproperty
    @property
    def _extension(self):
        pass

    def show(self):
        content = self.__read()
        return self._parse(content)

    @abstractmethod
    def _parse(self, content: str) -> dict:
        return NotImplementedError

    def __read(self):
        with open(self._filename) as file:
            return file.read()

    def __new__(cls, filename, *args, **kwargs):
        _, extension = filename.split('.')
        for parser in cls.__subclasses__():
            if parser._extension == extension:
                instance = super().__new__(parser)
                instance.__init__(filename)
                return instance
        else:
            raise NotImplementedError('Parser for given file type not found')


class ConfigParserINI(ConfigParser):
    _extension = 'ini'

    def _parse(self, content: str) -> dict:
        print('Parsing INI file')


class ConfigParserCSV(ConfigParser):
    _extension = 'csv'

    def _parse(self, content: str) -> dict:
        print('Parsing CSV file')


class ConfigParserYAML(ConfigParser):
    _extension = 'yaml'

    def _parse(self, content: str) -> dict:
        print('Parsing YAML file')


class ConfigFileJSON(ConfigParser):
    _extension = 'json'

    def _parse(self, content: str) -> dict:
        print('Parsing JSON file')


class ConfigFileXML(ConfigParser):
    _extension = 'xml'

    def _parse(self, content: str) -> dict:
        print('Parsing XML file')


if __name__ == '__main__':
    # iris.csv or *.csv, *.json *.yaml...
    # filename = input('Type filename: ')
    config = ConfigParser('/tmp/myfile.json')
    config.show()
