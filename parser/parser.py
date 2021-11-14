from typing import List
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def _parse(self) -> List:
        pass

    class ParserError(Exception):
        pass

    def __init__(self) -> None:
        pass

    _list = []

    def get(self) -> List:
        return self._list.copy()


