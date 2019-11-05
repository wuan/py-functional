[![Build Status](https://travis-ci.org/wuan/py-functional.svg?branch=master)](https://travis-ci.org/wuan/py-functional)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/3a1a12ff1d9b4c24b63252f5b8b5b6d3)](https://www.codacy.com/manual/wuan/py-functional?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wuan/py-functional&amp;utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a1a12ff1d9b4c24b63252f5b8b5b6d3)](https://www.codacy.com/manual/wuan/py-functional?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wuan/py-functional&amp;utm_campaign=Badge_Grade)

# py-functional

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