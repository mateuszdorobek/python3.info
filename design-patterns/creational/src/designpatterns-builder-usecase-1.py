class ReadCSV:
    filename: str
    delimiter: str
    encoding: str
    chunksize: int

    def __init__(self, filename):
        self.filename = filename

    def withChunksize(self, value):
        self.chunksize = value
        return self

    def withDelimiter(self, value):
        self.delimiter = value
        return self

    def withEncoding(self, value):
        self.encoding = value
        return self


if __name__ == '__main__':
    data = (
        ReadCSV('myfile.csv')
        .withChunksize(10_1000)
        .withDelimiter(',')
        .withEncoding('UTF-8')
    )
