from abc import ABC, abstractmethod

class Runner(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
