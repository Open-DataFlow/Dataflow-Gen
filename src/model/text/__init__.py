# from .generator import *

import sys
from src.utils.lazyloader import LazyLoader

_import_structure = {
    'APIGenerator': ('src/model/text/generator/APIGenerator.py', 'APIGenerator'),
    
    'LocalModelGenerator': ('src/model/text/generator/LocalModelGenerator.py', 'LocalModelGenerator'),
}

sys.modules[__name__] = LazyLoader(__name__, "src/model/text", _import_structure)