# mypytest
Testing the production of python packages.

# Installation

Open your conda/venv where you wish to install the package. From the command line, you can pip-install:

    pip install git+https://github.com/lindsay-forestell/mypytest.git

# Usage

```py
from mypytest import *

utils.guess_a_number()

test = ['a', 'b', 'c', 'd', 'e']
test_1 = random_list_chunk(test, 3)

print(test)
print(test_1)
```

NEW in version 0.0.2! Create a histogram from a list of data points. 

```py
from mypytest.utils import plot_histogram
import numpy as np

x = np.random.rand(100)
plot_histogram(x)
```

NEW in version 0.0.3! Create a madlibs about computers. 
```py
from mypytest.utils import mad_libs

mad_libs()
```
