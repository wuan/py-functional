import time

from functional import Stream


class Timer():
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('done')

    def checkpoint(self, name=''):
        print('{timer}: {checkpoint} in {elapsed:.3f} seconds'.format(
            timer=self.name,
            checkpoint=name,
            elapsed=self.elapsed,
        ).strip())


if __name__ == '__main__':
    iterations = 1000000

    lambda1 = lambda x: x * 2
    lambda2 = lambda x: x * x

    def func1(x): return x * 2
    def func2(x): return x * x

    with Timer('Stream'):
        result = Stream(range(iterations)) \
            .map(lambda1) \
            .map(lambda2) \
            .as_tuple()
        assert len(result) == iterations

    with Timer('List'):
        result = range(iterations)
        result = [x * 2 for x in result]
        result = [x * x for x in result]
        result = tuple(result)
        assert len(result) == iterations

    with Timer('List Labmda'):
        result = range(iterations)
        result = [lambda1(x) for x in result]
        result = [lambda2(x) for x in result]
        result = tuple(result)
        assert len(result) == iterations

    with Timer('Generator'):
        result = range(iterations)
        result = (x * 2 for x in result)
        result = (x * x for x in result)
        result = tuple(result)
        assert len(result) == iterations

    with Timer('Generator Lambda'):
        result = range(iterations)
        result = (lambda1(x) for x in result)
        result = (lambda2(x) for x in result)
        result = tuple(result)
        assert len(result) == iterations

    with Timer('Generator Function'):
        result = range(iterations)
        result = (func1(x) for x in result)
        result = (func2(x) for x in result)
        result = tuple(result)
        assert len(result) == iterations
