from abc import ABC, abstractmethod
from dataclasses import dataclass


class Device(ABC):
    @abstractmethod
    def set_channel(self, number: int) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def turn_on(self) -> None:
        pass


@dataclass
class RemoteControl:
    device: Device

    def turn_on(self) -> None:
        self.device.turn_on()

    def turn_off(self) -> None:
        self.device.turn_off()


class AdvancedRemoteControl(RemoteControl):
    def set_channel(self, number: int) -> None:
        self.device.set_channel(number)


class SonyTV(Device):
    def set_channel(self, number: int) -> None:
        print('Sony set channel')

    def turn_off(self) -> None:
        print('Sony turn off')

    def turn_on(self) -> None:
        print('Sony turn on')


class SamsungTV(Device):
    def set_channel(self, number: int) -> None:
        print('Samsung set channel')

    def turn_off(self) -> None:
        print('Samsung turn off')

    def turn_on(self) -> None:
        print('Samsung turn on')


if __name__ == '__main__':
    remote_control = RemoteControl(SonyTV())
    remote_control.turn_on()

    remote_control = AdvancedRemoteControl(SonyTV())
    remote_control.turn_on()

    remote_control = RemoteControl(SamsungTV())
    remote_control.turn_on()
