[![Build Status](https://travis-ci.org/wuan/py-functional.svg?branch=master)](https://travis-ci.org/wuan/py-functional)

# pyfunc

Simple python framework wrapping generators into a Stream class for chained processing

## Example

```python
    Stream([1, 2, 3])\
       .map(lambda x: x-1)\
       .flat_map(lambda x: [x for _ in range(x)])\
       .map(lambda x: str(x))\
       .as_tuple()
```

yields

```python
    ('1', '2', '2')
```