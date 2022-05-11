# pytest
Testing the production of python packages.

# Installation

    pip install git+https://github.com/lindsay-forestell/pytest.git

# Usage

```py
from pytest import *

utils.guess_a_number()

test = ['a', 'b', 'c', 'd', 'e']
test_1 = random_list_chunk(test, 3)

print(test)
print(test_1)
```

NEW in version 0.0.2! Create a histogram from a list of data points. 

```py
from pytest.utils import plot_histogram
import numpy as np

x = np.random.rand(100)
plot_histogram(x)
```
