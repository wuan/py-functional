from typing import Iterable

import pytest
from assertpy import assert_that
from pytest import raises

from functional import Stream
from functional.stream import Consumable, AlreadyConsumedException


def mapper(x: int) -> int:
    return x + 1


def flat_generator(x: int) -> Iterable[int]:
    return (x for _ in range(x))


def flat_list(x: int) -> Iterable[int]:
    return [x for _ in range(x)]


class TestConsumable:

    @pytest.fixture(name="uut")
    @staticmethod
    def uut(): return Consumable()

    def test_single_call_passes(self, uut):
        uut._consume()

    def test_second_call_raises(self, uut):
        uut._consume()

        with raises(AlreadyConsumedException):
            uut._consume()


class TestStream:

    @pytest.fixture
    def uut(self):
        return Stream([0, 1, 2])

    def test_map(self, uut):
        result = uut.map(mapper).as_tuple()

        assert_that(result).contains_only(1, 2, 3)

    def test_flat_map_generator(self, uut):
        result = uut.flat_map(flat_generator).as_tuple()

        assert_that(result).contains_only(1, 2, 2)

    def test_flat_map_none(self, uut):
        result = uut.flat_map(lambda x: None).as_tuple()

        assert_that(result).is_empty()

    def test_flat_map_list(self, uut):
        result = uut.flat_map(flat_list).as_tuple()

        assert_that(result).contains_only(1, 2, 2)
