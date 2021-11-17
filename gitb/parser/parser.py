from typing import List
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def _parse(self) -> List:
        pass

    class ParserError(Exception):
        def __init__(self, msg) -> None:
            print(f"{msg}")

    def __init__(self) -> None:
        pass

    _list = []

    def get(self) -> List:
        return self._list.copy()


