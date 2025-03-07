"""
Code trong file __init__.py sẽ được thực thi khi package được import

# Ví dụ trong __init__.py
from .module1 import function1, Class1
from .module2 import function2

# Sẽ cho phép người dùng sử dụng
# from my_package import function1, Class1, function2

Định nghĩa __all__: Biến __all__ trong file này xác định những gì được import khi sử dụng from package import *

/path1/
└── mynamespace/
    └── module1.py

/path2/
└── mynamespace/
    └── module2.py
"""
import bigo
import sys

print(sys.path)
