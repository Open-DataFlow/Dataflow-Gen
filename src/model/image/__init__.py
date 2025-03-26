# from .captioner import *
# from .generator import *

import sys
from src.utils.lazyloader import LazyLoader

_import_structure = {
    'LLaVACaptioner': ('src/model/image/captioner/LLaVACaptioner.py', 'LLaVACaptioner'),
    'LLaVANeXTCaptioner': ('src/model/image/captioner/LLaVANeXTCaptioner.py', 'LLaVANeXTCaptioner'),
    'LLaVAOneVisionCaptioner': ('src/model/image/captioner/LLaVAOneVisionCaptioner.py', 'LLaVAOneVisionCaptioner'),
    'BLIPCaptioner': ('src/model/image/captioner/BLIPCaptioner.py', 'BLIPCaptioner'),
    'QwenVLCaptioner': ('src/model/image/captioner/QwenVLCaptioner.py', 'QwenVLCaptioner'),
    'MLLamaCaptioner': ('src/model/image/captioner/MLLamaCaptioner.py', 'MLLamaCaptioner'),
    'Phi3VCaptioner': ('src/model/image/captioner/Phi3VCaptioner.py', 'Phi3VCaptioner'),
    'GPTCaptioner': ('src/model/image/captioner/GPTCaptioner.py', 'GPTCaptioner'),
    
    'FLUXGenerator': ('src/model/image/generator/FLUXGenerator.py', 'FLUXGenerator'),
    'StableDiffusionGenerator': ('src/model/image/generator/StableDiffusionGenerator.py', 'StableDiffusionGenerator'),
}

sys.modules[__name__] = LazyLoader(__name__, "src/model/image", _import_structure)