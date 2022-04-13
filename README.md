# Banko

A small pure Python library for randomly generating Banko-plader (Danish), also known as Bingo plates in the UK.

Dependencies:

- Python 3

How to install:

```bash
pip install banko
```

Usage:

```python
from banko.algorithms import Algorithm2
from banko.render import render_ascii

seed = 42
algo = Algorithm2(seed)
rows = algo.generate()
print(render_ascii(rows))
```

Output:

```
1    21 30          73 80
     22    41    66 74 82
  18 28    43 58       86
```

## Future work

Generate pretty images from array.
