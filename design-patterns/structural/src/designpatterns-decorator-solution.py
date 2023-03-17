from abc import ABC, abstractmethod
from dataclasses import dataclass
from hashlib import sha256


class Stream(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass


class CloudStream(Stream):
    def write(self, data: str) -> None:
        print(f'Storing: "{data}"')


@dataclass
class EncryptedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        encrypted: str = self._encrypt(data)
        self.stream.write(encrypted)

    def _encrypt(self, data: str) -> str:
        return sha256(data.encode()).hexdigest()


@dataclass
class CompressedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        compressed: str = self._compress(data)
        self.stream.write(compressed)

    def _compress(self, data: str) -> str:
        return data[0:9]


if __name__ == '__main__':
    credit_card = '1234-1234-1234-1234'

    cloud = CloudStream()
    cloud.write(credit_card)
    # Storing: "1234-1234-1234-1234"

    cloud = EncryptedCloudStream(CloudStream())
    cloud.write(credit_card)
    # Storing: "3eada3ce701aea4c21f117e1e95b32b2acd0a01dd03e7e57b02d141f5f9c7808"

    cloud = EncryptedCloudStream(CompressedCloudStream(CloudStream()))
    cloud.write(credit_card)
    # Storing: "3eada3ce7"
