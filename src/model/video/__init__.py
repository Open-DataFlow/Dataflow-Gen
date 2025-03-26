# from .generator import *
# from .captioner import *

import sys
from src.utils.lazyloader import LazyLoader

_import_structure = {
    'QwenVLCaptioner': ('src/model/video/captioner/QwenVLCaptioner.py', 'QwenVLCaptioner'),
    'LLaVAOVCaptioner': ('src/model/video/captioner/LLaVAOVCaptioner.py', 'LLaVAOVCaptioner'),
    'LLaVANeXTVideoCaptioner': ('src/model/video/captioner/LLaVANeXTVideoCaptioner.py', 'LLaVANeXTVideoCaptioner'),
    
    'AnimateDiffGenerator': ('src/model/video/generator/AnimateDiffGenerator.py', 'AnimateDiffGenerator'),
    'ModelScopeT2VGenerator': ('src/model/video/generator/ModelScopeT2VGenerator.py', 'ModelScopeT2VGenerator'),
    'CogVideoXGenerator': ('src/model/video/generator/CogVideoXGenerator.py', 'CogVideoXGenerator'),
    'SVDGenerator': ('src/model/video/generator/SVDGenerator.py', 'SVDGenerator'),
    'I2VGenXLGenerator': ('src/model/video/generator/I2VGenXLGenerator.py', 'I2VGenXLGenerator'),
    'CogVideoXT2VGenerator': ('src/model/video/generator/CogVideoXT2VGenerator.py', 'CogVideoXT2VGenerator'),
    'AllegroGenerator': ('src/model/video/generator/AllegroGenerator.py', 'AllegroGenerator'),
}

sys.modules[__name__] = LazyLoader(__name__, "src/model/video", _import_structure)