import abc


class BaseState(abc.ABC):

    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def process(self):
        pass
