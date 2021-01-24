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


def _wrap(iterable):
    return Stream(iterable)


def _iterable(iterable):
    return iterable if iterable else ()


class Stream(Generic[T], Consumable):
    _generator: Iterable[T]

    def __init__(self, generator=None):
        super().__init__()
        self._generator = generator if generator else iter(())

    def map(self, mapper: Callable[[T], U]) -> 'Stream[U]':
        self._consume()
        return _wrap((mapper(element) for element in self._generator))

    def flat_map(self, flat_mapper: Callable[[T], Iterable[U]]) -> 'Stream[U]':
        self._consume()
        return _wrap((result for element in self._generator for result in _iterable(flat_mapper(element))))

    def as_tuple(self) -> Tuple[T, ...]:
        self._consume()
        return tuple(self._generator)
