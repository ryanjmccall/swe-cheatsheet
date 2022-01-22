
from typing import TypeVar, Generic


T = TypeVar('T')


class LoggerVar(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, new: T) -> None:
        self.value = new

