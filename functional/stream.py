from typing import Callable, TypeVar, Generic, Tuple, Iterable

T = TypeVar('T')
U = TypeVar('U')


class AlreadyConsumedException(Exception):
    pass


class Consumable:

    def __init__(self):
        self.consumed = False

    def _consume(self):
        if self.consumed:
            raise AlreadyConsumedException()
        self.consumed = True


class Stream(Generic[T], Consumable):

    def __init__(self, generator=None):
        super().__init__()
        self._generator = generator if generator else tuple()

    def map(self, mapper: Callable[[T], U]) -> 'Stream[U]':
        self._consume()
        return Stream((mapper(element) for element in self._generator))

    def flat_map(self, flat_mapper: Callable[[T], Iterable[U]]) -> 'Stream[U]':
        self._consume()
        return Stream((result for element in self._generator for result in flat_mapper(element)))


    def as_tuple(self) -> Tuple[T]:
        self._consume()
        return tuple(self._generator)

