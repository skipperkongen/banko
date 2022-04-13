# Banko

A small pure Python library for generating random Banko-plader (Danish), also known as Bingo plates in the UK.

Dependencies:

- Python 3

Usage:

```python
from banko import Algorithm2

seed = 42
algo = Algorithm2(seed)
algo.generate()
```

Output:

```python
[[0, None, 21, 30, None, None, None, 73, 80],
 [None, None, 28, None, 41, None, 66, 74, 82],
 [None, 19, 29, None, 43, 58, None, None, 86]]
```

## Future work

Generate pretty images from array.
